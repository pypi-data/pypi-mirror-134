import cv2
import numpy as np
from typing import Tuple, List, Optional
from pathlib import Path
from ....logger import logger

ReadReturnType = Tuple[np.ndarray, int, List[int], int]

def video_read(path:str, n_frames: Optional[int]) -> ReadReturnType:
	path = str(path) if isinstance(path, Path) else path
	cap = cv2.VideoCapture(path)
	fps = cap.get(cv2.CAP_PROP_FPS)
	n_frames = 1<<31 if n_frames is None else n_frames
	logger.debug(f"Reading raw data. Path: {path}. n_frames: {n_frames}")

	data = []
	i = 0
	while cap.isOpened():
		if i == n_frames:
			break

		i += 1
		ret, frame = cap.read()
		if not ret:
			break

		frame = frame[..., ::-1]
		data.append(frame)
	cap.release()

	video = np.array(data)
	n_frames = len(video)
	video = video[..., 0 : 3]

	return video, fps, video.shape, n_frames
