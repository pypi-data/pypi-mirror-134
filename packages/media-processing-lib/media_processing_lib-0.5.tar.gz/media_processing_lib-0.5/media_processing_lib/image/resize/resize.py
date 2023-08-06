import numpy as np
from ...logger import logger

# @brief Generic function to resize ONE 2D image of shape (H, W) or 3D of shape (H, W, D) into (height, width [, D])
# @param[in] data Image (or any 2D/3D array)
# @param[in] height Desired resulting height
# @param[in] width Desired resulting width
# @param[in] interpolation Interpolation method. Valid choices are specific to the library used for the resizing.
# @param[in] mode Whether to stretch the image or apply black bars around it to preserve scaling.
# @param[in] resize_lib The library used for resizing
# @param[in] only_uint8 If true, only [0-255] images are allowed. Otherwise, let the resize_lib work the provided dtype.
# @return Resized image.
def image_resize(data: np.ndarray, height: int, width: int, interpolation: str="bilinear", \
		mode: str="stretch", resize_lib: str="opencv", only_uint8: bool=True, **kwargs) -> np.ndarray:
	assert len(data.shape) in (2, 3)
	if data.shape[0] == height and data.shape[1] == width:
		logger.debug("Width and height are already to the desired shape. Returning early.")
		return data.copy()
	if only_uint8 == True:
		assert data.dtype == np.uint8, f"Data dtype: {data.dtype}. Use only_uint8=False."

	if mode == "stretch":
		from .resize_stretch import image_resize_stretch
		resize_fn = image_resize_stretch
	elif mode == "black_bars":
		from .resize_black_bars import image_resize_black_bars
		resize_fn = image_resize_black_bars
	else:
		assert False, mode

	if resize_lib == "skimage":
		from ..libs.skimage import image_resize as f
	elif resize_lib == "lycon":
		from ..libs.lycon import image_resize as f
	elif resize_lib in ("pillow", "PIL"):
		from ..libs.pil import image_resize as f
	elif resize_lib == "opencv":
		from ..libs.opencv import image_resize as f
	else:
		assert False, resize_lib

	resizedData = resize_fn(data, height, width, interpolation, f, **kwargs)
	return resizedData

# @brief Generic function to resize a batch of images of shape BxHxW(xD) to a desired shape of BxdWxdH(xD)
# @param[in] data batch of images (or any 2D/3D array)
# @param[in] height Desired resulting height
# @param[in] width Desired resulting width
# @param[in] interpolation Interpolation method. Valid choices are specific to the library used for the resizing.
# @param[in] mode Whether to stretch the image or apply black bars around it to preserve scaling.
# @param[in] resize_lib The library used for resizing
# @param[in] only_uint8 If true, only [0-255] images are allowed. Otherwise, let the resize_lib work the provided dtype.
# @return Resized batch of images.
def image_resize_batch(data: np.ndarray, height: int, width: int, interpolation: str="bilinear", \
		mode: str="stretch", resize_lib: str="opencv", only_uint8: bool=True, **kwargs) -> np.ndarray:
	N = len(data)
	assert N > 0

	# Let the imgResize infer the height/width if not provided (i.e. autosclaing for imgResize)
	first_result = image_resize(data[0], height=height, width=width, interpolation=interpolation, \
		mode=mode, resize_lib=resize_lib, only_uint8=only_uint8, **kwargs)
	new_data = np.zeros((N, *first_result.shape), dtype=data[0].dtype)
	new_data[0] = first_result
	for i in range(1, N):
		result = image_resize(data[i], height=height, width=width, interpolation=interpolation, \
			mode=mode, resize_lib=resize_lib, only_uint8=only_uint8, **kwargs)
		new_data[i] = result
	return new_data
