import os
import mimetypes
import warnings

from .utils import get_wav_from_video
from .mpl_audio import MPLAudio
from ..logger import logger, logging


# FUN FACT: Reading mp4 (videos in general?) will yield different results every time, so we can convert data to wav
#  first if mp4
def audio_read(path:str, audio_lib: str="librosa", force_wav: bool=True, count: int=5, **kwargs):
	assert audio_lib in ("librosa", )
	if audio_lib == "librosa":
		from .libs.librosa import audio_read as f

	if logger.getEffectiveLevel() < logging.DEBUG:
		warnings.filterwarnings("ignore")

	is_video = mimetypes.guess_type(path)[0].startswith("video")
	if force_wav and is_video:
		fd, tmpPath = get_wav_from_video(path)
		logger.debug(f"Converting {path} video to wav. Got path: {tmpPath}")
		path = tmpPath

	i = 0
	while True:
		try:
			audio_data, sample_rate = f(path, **kwargs)
			audio = MPLAudio(audio_data, sample_rate)
			logger.debug(f"Read audio {path}. Shape: {audio.shape}. Sample rate: {audio.sample_rate:.2f}")
			if force_wav and is_video:
				os.remove(path)
				os.close(fd)
			return audio
		except Exception as e:
			logger.debug(f"Path: {path}. Exception: {e}")
			i += 1

			if i == count:
				raise Exception(e)
