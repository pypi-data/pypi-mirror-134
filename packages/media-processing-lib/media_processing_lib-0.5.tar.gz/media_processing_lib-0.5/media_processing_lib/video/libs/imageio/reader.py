import numpy as np
from imageio import get_reader
from typing import Tuple, List, Optional
from ....logger import logger

ReadReturnType = Tuple[np.ndarray, int, List[int], int]

def video_read(path: str, n_frames: Optional[int]) -> ReadReturnType:
	reader = get_reader(path)
	metadata = reader.get_meta_data()

	n_frames = 1<<31 if n_frames is None else n_frames
	logger.debug(f"Reading raw data. Path: {path}. N frames: {n_frames}")
	fps = metadata["fps"]
	
	# Make this smarter
	video = []
	for i, frame in enumerate(reader):
		if i == n_frames:
			break
		video.append(frame)
	video = np.array(video)
	n_frames = len(video)
	video = video[..., 0 : 3]

	return video, fps, video.shape, n_frames
