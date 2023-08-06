import numpy as np
from pathlib import Path
from typing import Optional

from .utils import is_rotated_90
from .mpl_video import MPLVideo
from ..logger import logger

def video_read(path:str, vid_lib: str="imageio", count: int=5, n_frames: Optional[int]=None, **kwargs) -> MPLVideo:
	path = Path(path).resolve()
	extension = path.suffix.lower()[1 :]
	assert extension in ("gif", "mp4", "mov", "mkv")
	assert vid_lib in ("imageio", "pims", "opencv", "decord")

	if vid_lib == "pims":
		from .libs.pims import video_read as f
	elif vid_lib == "imageio":
		from .libs.imageio import video_read as f
	elif vid_lib == "opencv":
		from .libs.opencv import video_read as f
	elif vid_lib == "decord":
		from .libs.decord import video_read as f

	i = 0
	while True:
		try:
			data, fps, shape, n_frames = f(path, n_frames, **kwargs)
			is_portrait = is_rotated_90(path, data)
			assert len(shape) == 4
			video = MPLVideo(data, fps, is_portrait, shape, n_frames)
			logger.debug(f"Read video: {video}. \n Path: '{path}'. Video library: '{vid_lib}'")
			return video
		except Exception as e:
			logger.debug(f"Path: {path}. Exception: {e}")
			i += 1

			if i == count:
				raise Exception(e)
