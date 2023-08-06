import numpy as np
from ..logger import logger

def image_write(file: np.ndarray, path: str, img_lib: str="opencv", count: int=5) -> None:
	path = str(path) if not isinstance(path, str) else path
	assert img_lib in ("opencv", "PIL", "pillow", "lycon")
	if img_lib == "opencv":
		from .libs.opencv import image_write as f
	elif img_lib in ("PIL", "pillow"):
		from .libs.pil import image_write as f
	elif img_lib == "lycon":
		from .libs.lycon import image_write as f

	i = 0
	while True:
		try:
			return f(file, path)
		except Exception as e:
			logger.debug(f"Path: {path}. Exception: {e}")
			i += 1

			if i == count:
				raise Exception
