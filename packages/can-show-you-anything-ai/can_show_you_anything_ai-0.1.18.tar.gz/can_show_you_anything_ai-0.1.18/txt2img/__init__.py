import sys
import fire
from txt2img.core import core, save_tensor_image, display_image,get_unique_file_path
from PIL import TiffTags
import sys


def save(
    *args,
    batch_size: int = 1,
    guidance_scale: float = 3.0,
    upsample_temp: float = 0.997,
):
    """Save image.

    Args:
      *args:
      batch_size: int:  (Default value = 1)
      guidance_scale: float:  (Default value = 3.0)
      upsample_temp: float:  (Default value = 0.997)

    Returns:

    """

    if len(args) > 1:
        prompt = " ".join(args)
    else:
        prompt = args[0]
    
    prompt= prompt.strip().replace("  ",' ')
    tf_img = core(prompt, batch_size, guidance_scale, upsample_temp)
    name = prompt.replace(" ", "_").strip()
    out_path = get_unique_file_path('.',name,'png')
    save_tensor_image(tf_img, out_path)


def show_me(
    prompt,
    batch_size: int = 1,
    guidance_scale: float = 3.0,
    upsample_temp: float = 0.997,
):
    """Display image in jupyter notebook.

    Args:
      prompt:
      batch_size: int:  (Default value = 1)
      guidance_scale: float:  (Default value = 3.0)
      upsample_temp: float:  (Default value = 0.997)

    """

    tf_img = core(prompt, batch_size, guidance_scale, upsample_temp)
    name = prompt.replace(" ", "_").strip()
    out_path = get_unique_file_path('.',name,'png')
    save_tensor_image(tf_img, out_path)
    display_image(out_path)

# function alias
show_a = show_me
show = show_me


def cli():
    """ """
    fire.Fire(save)
