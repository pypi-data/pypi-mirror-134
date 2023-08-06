import pims
import numpy as np
from typing import Tuple, List, Optional
from ....logger import logger

ReadReturnType = Tuple[np.ndarray, int, List[int], int]

def video_read(path:str, n_frames:Optional[int]) -> ReadReturnType:
	video = pims.Video(path)
	fps = video.frame_rate
	data = video
	if n_frames == None:
		n_frames = len(video)
	logger.debug(f"Reading raw data. Path: {path}. n_frames: {n_frames}")
	shape = (n_frames, *video.frame_shape)
	return data, fps, shape, n_frames
