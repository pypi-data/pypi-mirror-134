import soundfile
from ...mpl_audio import MPLAudio
from ....logger import logger

def audio_write(audio: MPLAudio, path: str, **kwargs):
    """Uses soundfile to write audio"""
    logger.debug(f"Writing {audio} to '{path}'.")
    soundfile.write(path, audio.data, int(audio.sample_rate))
