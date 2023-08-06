import numpy as np
from decord import VideoReader, cpu, gpu
from typing import Optional, List, Tuple
from pathlib import Path
from ....logger import logger

ReadReturnType = Tuple[np.ndarray, int, List[int], int]

def video_read(path:Path, n_frames:Optional[int], context="cpu") -> ReadReturnType:
    context = {
        "cpu":cpu(0),
        "gpu":gpu(0)
    }[context]

    vr = VideoReader(str(path), ctx=context)
    n_frames = len(vr) if n_frames is None else n_frames
    logger.debug(f"Reading raw data. Path: {path}. Num frames: {n_frames}")
    shape = [n_frames, *vr[0].shape]
    fps = vr.get_avg_fps()
    return vr, fps, shape, n_frames
