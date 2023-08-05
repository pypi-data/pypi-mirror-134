"""
Various utilities for neural networks.
"""

import math

import torch as th
import torch.nn as nn
import torch.nn.functional as F


class GroupNorm32(nn.GroupNorm):
    """ """

    def __init__(self, num_groups, num_channels, swish, eps=1e-5):
        super().__init__(num_groups=num_groups, num_channels=num_channels, eps=eps)
        self.swish = swish

    def forward(self, x):
        """

        Args:
          x:

        Returns:

        """
        y = super().forward(x.float()).to(x.dtype)
        if self.swish == 1.0:
            y = F.silu(y)
        elif self.swish:
            y = y * F.sigmoid(y * float(self.swish))
        return y


def conv_nd(dims, *args, **kwargs):
    """Create a 1D, 2D, or 3D convolution module.

    Args:
      dims:
      *args:
      **kwargs:

    Returns:

    """
    if dims == 1:
        return nn.Conv1d(*args, **kwargs)
    elif dims == 2:
        return nn.Conv2d(*args, **kwargs)
    elif dims == 3:
        return nn.Conv3d(*args, **kwargs)
    raise ValueError(f"unsupported dimensions: {dims}")


def linear(*args, **kwargs):
    """Create a linear module.

    Args:
      *args:
      **kwargs:

    Returns:

    """
    return nn.Linear(*args, **kwargs)


def avg_pool_nd(dims, *args, **kwargs):
    """Create a 1D, 2D, or 3D average pooling module.

    Args:
      dims:
      *args:
      **kwargs:

    Returns:

    """
    if dims == 1:
        return nn.AvgPool1d(*args, **kwargs)
    elif dims == 2:
        return nn.AvgPool2d(*args, **kwargs)
    elif dims == 3:
        return nn.AvgPool3d(*args, **kwargs)
    raise ValueError(f"unsupported dimensions: {dims}")


def zero_module(module):
    """Zero out the parameters of a module and return it.

    Args:
      module:

    Returns:

    """
    for p in module.parameters():
        p.detach().zero_()
    return module


def scale_module(module, scale):
    """Scale the parameters of a module and return it.

    Args:
      module:
      scale:

    Returns:

    """
    for p in module.parameters():
        p.detach().mul_(scale)
    return module


def normalization(channels, swish=0.0):
    """Make a standard normalization layer, with an optional swish activation.

    Args:
      channels: number of input channels.
      swish:  (Default value = 0.0)

    Returns:
      an nn.Module for normalization.

    """
    return GroupNorm32(num_channels=channels, num_groups=32, swish=swish)


def timestep_embedding(timesteps, dim, max_period=10000):
    """Create sinusoidal timestep embeddings.

    Args:
      timesteps: a 1-D Tensor of N indices, one per batch element.
    These may be fractional.
      dim: the dimension of the output.
      max_period: controls the minimum frequency of the embeddings. (Default value = 10000)

    Returns:
      an [N x dim] Tensor of positional embeddings.

    """
    half = dim // 2
    freqs = th.exp(
        -math.log(max_period) * th.arange(start=0, end=half, dtype=th.float32) / half,
    ).to(device=timesteps.device)
    args = timesteps[:, None].float() * freqs[None]
    embedding = th.cat([th.cos(args), th.sin(args)], dim=-1)
    if dim % 2:
        embedding = th.cat([embedding, th.zeros_like(embedding[:, :1])], dim=-1)
    return embedding
