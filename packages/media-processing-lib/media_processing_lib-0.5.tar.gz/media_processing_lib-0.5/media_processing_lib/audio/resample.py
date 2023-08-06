import numpy as np
from .mpl_audio import MPLAudio

def resample(audio: MPLAudio, sample_rate: int) -> MPLAudio:
    """Lazily use NumPy for this task"""
    newLen = int(len(audio.data) / audio.sample_rate * sample_rate)
    x = np.arange(0, newLen)
    xp = np.arange(0, len(audio.data))
    new_data = np.interp(x, xp, audio.data)
    new_audio = MPLAudio(new_data, sample_rate)
    return new_audio
