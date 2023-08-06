from typing import Union, List
import numpy as np
from pathlib import Path
from .mpl_video import MPLVideo

# TODO: Add ffmpeg params here perhaps to call each specific writer with its caveats.

def video_write(video: Union[MPLVideo, np.ndarray, List], path: Union[str, Path], **kwargs):
	if isinstance(video, (np.ndarray, List)):
		assert "fps" in kwargs
		video:MPLVideo = MPLVideo(video, kwargs["fps"])
	video.write(path, **kwargs)
