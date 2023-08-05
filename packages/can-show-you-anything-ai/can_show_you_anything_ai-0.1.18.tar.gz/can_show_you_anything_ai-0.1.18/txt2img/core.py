import fire
import torch as th
from IPython.display import display,Image

#from PIL import Image
import sys
from importlib import reload  # Python 3.4+
import time
import os
from numpy import random
import os
import IPython
from matplotlib import pyplot as plt
import matplotlib



from glide_text2im.download import load_checkpoint
from glide_text2im.model_creation import (
    create_model_and_diffusion,
    model_and_diffusion_defaults,
    model_and_diffusion_defaults_upsampler,
)


from IPython.display import Image
from IPython.core.display import HTML
from IPython.core.display import display
import numpy as np



# This notebook supports both CPU and GPU.
# On CPU, generating one sample may take on the order of 20 minutes.
# On a GPU, it should be under a minute.
has_cuda = th.cuda.is_available()
device = th.device("cpu" if not has_cuda else "cuda")
is_in_colab = 'google.colab' in sys.modules

if not has_cuda:
    print("Warning: No cuda gpu avalible:")
    if is_in_colab:
        print("Select a gpu runtime by clicking,")
        print("\t 'Runtime' > 'Change runtime type' > 'Hardware accelerator' > 'GPU'")

def _create_base_model(options):
    """

    Args:
      options:

    Returns:

    """
    # Create base model.
    options["use_fp16"] = has_cuda
    # use 100 diffusion steps for fast sampling
    options["timestep_respacing"] = "100"
    model, diffusion = create_model_and_diffusion(**options)
    model.eval()
    if has_cuda:
        model.convert_to_fp16()
    model.to(device)
    model.load_state_dict(load_checkpoint("base", device))
    print("total base parameters", sum(x.numel() for x in model.parameters()))
    return model, diffusion


def _create_upsampler_model(options_up):
    """

    Args:
      options_up:

    Returns:

    """
    # Create upsampler model.

    options_up["use_fp16"] = has_cuda
    options_up[
        "timestep_respacing"
    ] = "fast27"  # use 27 diffusion steps for very fast sampling
    model_up, diffusion_up = create_model_and_diffusion(**options_up)
    model_up.eval()
    if has_cuda:
        model_up.convert_to_fp16()
    model_up.to(device)
    model_up.load_state_dict(load_checkpoint("upsample", device))
    print("total upsampler parameters", sum(x.numel() for x in model_up.parameters()))
    return model_up, diffusion_up



def generate_guidance_sampling_function(model, guidance_scale):
    """

    Args:
      model:
      guidance_scale:

    Returns:

    """

    def guidance_sampling_function(x_t, ts, **kwargs):
        """

        Args:
          x_t:
          ts:
          **kwargs:

        Returns:

        """
        # Create a classifier-free guidance sampling function
        half = x_t[: len(x_t) // 2]
        combined = th.cat([half, half], dim=0)
        model_out = model(combined, ts, **kwargs)
        eps, rest = model_out[:, :3], model_out[:, 3:]
        cond_eps, uncond_eps = th.split(eps, len(eps) // 2, dim=0)
        half_eps = uncond_eps + guidance_scale * (cond_eps - uncond_eps)
        eps = th.cat([half_eps, half_eps], dim=0)
        return th.cat([eps, rest], dim=1)

    return guidance_sampling_function


# @title Sample from the base model
def sample_from_base_model(
    prompt,
    batch_size: int = 1,
    guidance_scale: float = 3.0,
):
    """

    Args:
      prompt: str
      batch_size: int
      guidance_scale: float

    Returns:

    """

    ##############################
    # Sample from the base model #
    ##############################

    options = model_and_diffusion_defaults()
    model, diffusion = _create_base_model(options)

    # Create the text tokens to feed to the model.
    tokens = model.tokenizer.encode(prompt)
    tokens, mask = model.tokenizer.padded_tokens_and_mask(tokens, options["text_ctx"])

    # Create the classifier-free guidance tokens (empty)
    full_batch_size = batch_size * 2
    uncond_tokens, uncond_mask = model.tokenizer.padded_tokens_and_mask(
        [],
        options["text_ctx"],
    )

    # Pack the tokens together into model kwargs.
    model_kwargs = dict(
        tokens=th.tensor(
            [tokens] * batch_size + [uncond_tokens] * batch_size,
            device=device,
        ),
        mask=th.tensor(
            [mask] * batch_size + [uncond_mask] * batch_size,
            dtype=th.bool,
            device=device,
        ),
    )

    model_fn = generate_guidance_sampling_function(model, guidance_scale)

    # Sample from the base model.
    model.del_cache()
    samples = diffusion.p_sample_loop(
        model_fn,
        (full_batch_size, 3, options["image_size"], options["image_size"]),
        device=device,
        clip_denoised=True,
        progress=True,
        model_kwargs=model_kwargs,
        cond_fn=None,
    )[:batch_size]
    model.del_cache()
    return samples


# @title Upsample the 64x64 samples
##############################
# Upsample the 64x64 samples #
##############################


def upsample_the_64x64_samples(
    samples,
    prompt: str,
    batch_size,
    upsample_temp: float = 0.997,
):
    """Upsample the 64x64 samples #

    Args:
      samples:
      prompt: str:
      batch_size:
      upsample_temp: float:  (Default value = 0.997)

    Returns:

    """

    options_up = model_and_diffusion_defaults_upsampler()
    model_up, diffusion_up = _create_upsampler_model(options_up)
    tokens = model_up.tokenizer.encode(prompt)
    tokens, mask = model_up.tokenizer.padded_tokens_and_mask(
        tokens,
        options_up["text_ctx"],
    )

    # Create the model conditioning dict.
    model_kwargs = dict(
        # Low-res image to upsample.
        low_res=((samples + 1) * 127.5).round() / 127.5 - 1,
        # Text tokens
        tokens=th.tensor([tokens] * batch_size, device=device),
        mask=th.tensor(
            [mask] * batch_size,
            dtype=th.bool,
            device=device,
        ),
    )

    # Sample from the base model.
    model_up.del_cache()
    up_shape = (batch_size, 3, options_up["image_size"], options_up["image_size"])
    up_samples = diffusion_up.ddim_sample_loop(
        model_up,
        up_shape,
        noise=th.randn(up_shape, device=device) * upsample_temp,
        device=device,
        clip_denoised=True,
        progress=True,
        model_kwargs=model_kwargs,
        cond_fn=None,
    )[:batch_size]
    model_up.del_cache()
    return up_samples



def pillow_is_updated():
    try:
        import PIL
        from PIL.TiffTags import IFD
        assert PIL.__version__ == '9.0.0'
        return True
    except:
        return False



def check_pillow_import():
    if not pillow_is_updated():
        warning = "An old version of Pillow is already imported. You need to restart the runtime: \n"
        answer = input(f"{warning}. Restart runtime? [y/N]")
        if answer in ['y','Y','yes','Yes', 'YES'] or answer is None:
            print("Restarting runtime. You will need to reimport any packages you were using. ")
            for i in range(5):
                os.kill(os.getpid(), 9)
                time.sleep(1)


def core(
    prompt,
    batch_size: int,
    guidance_scale: float,
    upsample_temp: float,
):
    """Run image generation.

    Args:
      prompt: str:  (Default value = "an oil painting of a corgi")
      batch_size: int:  (Default value = 1)
      guidance_scale: float:  (Default value = 3.0)
      upsample_temp: float:  (Default value = 0.997)

    Returns:

    """
    #check_pillow_import()
    print(f"Generate image of '{prompt}':")
    samples = sample_from_base_model(prompt, batch_size, guidance_scale)
    up_samples = upsample_the_64x64_samples(samples, prompt, batch_size, upsample_temp)
    return up_samples





def get_unique_file_path(out_dir,file_name,suffix):

  file_path = f'{out_dir}/{file_name}.{suffix}'
  if not os.path.isfile(file_path):
    return file_path
  i = 1
  while os.path.isfile(f'{out_dir}/{file_name} [{i}].{suffix}'):
    i+=1
  return  f'{out_dir}/{file_name} [{i}].{suffix}'


def save_numpy_image(data,out_path):
    matplotlib.image.imsave(out_path, data)
    

def save_tensor_image(batch: th.Tensor, out_path:str ):
    scaled = ((batch + 1) * 127.5).round().clamp(0, 255).to(th.uint8).cpu()
    reshaped = scaled.permute(2, 0, 3, 1).reshape([batch.shape[2], -1, 3])
    img_array = reshaped.numpy()
    save_numpy_image(img_array,out_path)

def display_image(file_path):
    display( Image(file_path))



#check_pillow_import()




'''
def show_images(batch: th.Tensor):
    """Display a batch of images inline.

    Args:
      batch: th.Tensor:

    """
    scaled = ((batch + 1) * 127.5).round().clamp(0, 255).to(th.uint8).cpu()
    reshaped = scaled.permute(2, 0, 3, 1).reshape([batch.shape[2], -1, 3])
    img_array = reshaped.numpy()
    
    display(Image.fromarray(img_array))


def save_images(batch: th.Tensor, out_path):
    """Display a batch of images inline.

    Args:
      batch: th.Tensor:
      out_path:

    Returns:

    """
    scaled = ((batch + 1) * 127.5).round().clamp(0, 255).to(th.uint8).cpu()
    reshaped = scaled.permute(2, 0, 3, 1).reshape([batch.shape[2], -1, 3])
    Image.fromarray(reshaped.numpy()).save(out_path)
'''
