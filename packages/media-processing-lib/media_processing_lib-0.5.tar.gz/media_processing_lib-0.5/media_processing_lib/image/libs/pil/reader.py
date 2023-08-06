import numpy as np
from PIL import Image

def image_read(path: str) -> np.ndarray:
	image = np.array(Image.open(path), dtype=np.uint8)[..., 0 : 3]
	return image
