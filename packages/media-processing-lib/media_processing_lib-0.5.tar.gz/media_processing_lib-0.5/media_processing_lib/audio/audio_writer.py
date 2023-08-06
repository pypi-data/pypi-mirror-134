import numpy as np
from typing import List, Union
from pathlib import Path
from .mpl_audio import MPLAudio

def audio_write(audio: Union[MPLAudio, np.ndarray, List], path: Union[str, Path], audio_lib: str="soundfile", \
		count: int=5, **kwargs):
	path = str(path) if not isinstance(path, str) else path

	assert audio_lib in ("soundfile", )
	if audio_lib == "soundfile":
		from .libs.soundfile import audio_write as f

	if isinstance(audio, (np.ndarray, List)):
		assert "sample_rate" in kwargs
		audio = MPLAudio(audio, kwargs["sample_rate"])

	i = 0
	while True:
		try:
			f(audio, path, **kwargs)
			return
		except Exception as e:
			print(f"Path: {path}. Exception: {e}")
			i += 1

			if i == count:
				raise Exception
