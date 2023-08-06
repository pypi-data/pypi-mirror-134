import numpy as np
import lycon

def image_write(file: np.ndarray, path: str):
	assert file.min() >= 0 and file.max() <= 255
	lycon.save(path, file.astype(np.uint8))
