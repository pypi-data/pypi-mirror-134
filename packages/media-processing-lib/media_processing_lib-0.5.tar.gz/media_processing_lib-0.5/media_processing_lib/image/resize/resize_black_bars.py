import numpy as np
from typing import Callable

def image_resize_black_bars(data: np.ndarray, height: int, width: int, interpolation: str, \
		resize_fn: Callable, return_coordinates: bool=False, **kwargs) -> np.ndarray:
	desired_shape = (height, width) if len(data.shape) == 2 else (height, width, data.shape[-1])

	img_h, img_w = data.shape[0 : 2]
	desired_h, desired_w = desired_shape[0 : 2]

	# Find the rapports between the img_h/desired_h and img_w/desired_w
	rH, rW = img_h / desired_h, img_w / desired_w

	# Find which one is the highest, that one will be used
	maxRapp = max(rH, rW)
	assert maxRapp != 0, f"Cannot convert data of shape {data.shape} to ({height}, {width})"

	# Compute the new dimensions, based on the highest rapport
	scaledH, scaledW = int(img_h / maxRapp), int(img_w / maxRapp)
	assert scaledH != 0 and scaledW != 0, f"Cannot convert data of shape {data.shape} to ({height}, {width})"

	resizedData = resize_fn(data, scaledH, scaledW, interpolation, **kwargs)
	# Also, find the half, so we can insert the other dimension from the half
	# Insert the resized image in the original image, halving the larger dimension and keeping half black bars in
	#  each side
	new_data = np.zeros(desired_shape, dtype=data.dtype)
	half_h, half_w = int((desired_h - scaledH) / 2), int((desired_w - scaledW) / 2)
	new_data[half_h : half_h + scaledH, half_w : half_w + scaledW] = resizedData

	if return_coordinates:
		x0, y0, x1, y1 = half_w, half_h, half_w + scaledW, half_h + scaledH
		return new_data, (x0, y0, x1, y1)
	else:
		return new_data
