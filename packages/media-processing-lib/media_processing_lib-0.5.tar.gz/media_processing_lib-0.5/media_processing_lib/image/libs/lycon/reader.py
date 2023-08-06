import numpy as np
import lycon

def image_read(path: str) -> np.ndarray:
	image = lycon.load(path)[..., 0 : 3].astype(np.uint8)
	return image
