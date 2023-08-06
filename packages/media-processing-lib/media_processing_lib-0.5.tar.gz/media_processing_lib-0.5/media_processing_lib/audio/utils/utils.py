from typing import Tuple
import tempfile
import subprocess
from ...logger import logger

def get_wav_from_video(path: str) -> Tuple[int, str]:
    """Given a video path, use ffmpeg under the hood to extract the audio, and return the audio fd and path."""
    fd, tmp_path = tempfile.mkstemp(suffix=".wav")
    logger.debug2(f"Extracting audio from '{path}'. Will be stored at '{tmp_path}'.")
    command = f"ffmpeg -loglevel panic -y -i {path} -strict -2 {tmp_path}"
    subprocess.call(command, shell=True)
    return fd, tmp_path
