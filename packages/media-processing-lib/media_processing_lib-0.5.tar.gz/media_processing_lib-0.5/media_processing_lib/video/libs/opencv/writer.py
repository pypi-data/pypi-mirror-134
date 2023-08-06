import cv2
import numpy as np
from typing import Callable
from ...mpl_video import MPLVideo
from ....logger import drange

def video_write(video: MPLVideo, path: str, apply_fn: Callable[[MPLVideo, int], np.ndarray], **kwargs):
	width, height = video.shape[2], video.shape[1]
	fourcc = kwargs["fourcc"] if "fourcc" in kwargs else "mp4v"
	writer = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*fourcc), video.fps, (width, height))

	N = len(video)
	for i in drange(N, desc="[OpenCV::writeVideo]"):
		frame = apply_fn(video, i)
		frame = frame[..., ::-1]
		writer.write(frame)
