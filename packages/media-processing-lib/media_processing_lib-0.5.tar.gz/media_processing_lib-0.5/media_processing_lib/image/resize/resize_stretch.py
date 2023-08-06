import numpy as np
from typing import Callable
from ...logger import logger

def image_resize_stretch(data: np.ndarray, height: int, width: int, interpolation: str, resize_fn: Callable, **kwargs):
	current_height, current_width = data.shape[0], data.shape[1]
	# If we provide width only, height is infered to keep image scale
	assert (height is None) + (width is None) < 2, "Both width and height cannot be infered. Provide at least one."
	if height is None:
		assert not width is None
		height = current_height / current_width * width
		if height != int(height):
			logger.debug(f"Converting infered height from {height:.2f} to {int(height)}")
		height = int(height)

	if width is None:
		assert not height is None
		width = current_height / current_width * height
		if width != int(width):
			logger.debug(f"Converting infered width from {width:.2f} to {int(width)}")
		width = int(width)

	return resize_fn(data, height, width, interpolation, **kwargs)
