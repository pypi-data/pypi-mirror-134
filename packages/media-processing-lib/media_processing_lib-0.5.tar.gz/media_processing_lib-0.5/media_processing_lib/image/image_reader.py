import numpy as np
from pathlib import Path
from ..logger import logger

def image_read(path:str, img_lib: str="opencv", count: int=5) -> np.ndarray:
	assert img_lib in ("opencv", "PIL", "pillow", "lycon")
	if img_lib == "opencv":
		from .libs.opencv import image_read as f
	elif img_lib in ("PIL", "pillow"):
		from .libs.pil import image_read as f
	elif img_lib == "lycon":
		from .libs.lycon import image_read as f
	else:
		assert False, f"Unknown library: {img_lib}"

	path = str(path) if isinstance(path, Path) else path

	i = 0
	while True:
		try:
			return f(path)
		except Exception as e:
			logger.debug(f"Path: {path}. Exception: {e}")
			i += 1

			if i == count:
				raise Exception(e)
