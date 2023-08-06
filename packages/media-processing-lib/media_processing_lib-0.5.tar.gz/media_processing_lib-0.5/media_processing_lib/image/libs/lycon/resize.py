import numpy as np
from lycon import resize, Interpolation

# @brief Lycon based image resizing function
# @param[in] height Desired resulting height
# @param[in] width Desired resulting width
# @param[in] interpolation method. Valid options: bilinear, nearest, cubic, lanczos, area
# @return Resized image.
def image_resize(data: np.ndarray, height: int, width: int, interpolation: str, **kwargs) -> np.ndarray:
	assert interpolation in ("bilinear", "nearest", "bicubic", "lancsoz", "area")
	assert isinstance(height, int) and isinstance(width, int)

	# As per: https://github.com/ethereon/lycon/blob/046e9fab906b3d3d29bbbd3676b232bd0bc82787/perf/benchmark.py#L57
	interpolation_types = {
		"bilinear" : Interpolation.LINEAR,
		"nearest" : Interpolation.NEAREST,
		"bicubic" : Interpolation.CUBIC,
		"lanczos" : Interpolation.LANCZOS,
		"area" : Interpolation.AREA
	}

	interpolation_type = interpolation_types[interpolation]
	img_resized = resize(data, height=height, width=width, interpolation=interpolation_type, **kwargs)
	return img_resized.astype(data.dtype)
