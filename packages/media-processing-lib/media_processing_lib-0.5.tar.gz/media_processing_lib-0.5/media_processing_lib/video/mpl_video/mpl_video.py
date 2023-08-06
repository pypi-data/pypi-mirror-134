from __future__ import annotations
import numpy as np
from abc import ABC
from typing import Any, Tuple, Optional, Callable
from copy import copy
from decord.ndarray import NDArray
from ...logger import logger, drange

class MPLVideo(ABC):
	def __init__(self, data:Any, fps:int, isPortrait:Optional[bool]=False, \
		shape:Optional[Tuple[int]]=None, nFrames:Optional[int]=None):
		self.data = data
		self.nFrames = len(self.data) if nFrames is None else nFrames
		self.baseShape = self.data.shape if shape is None else shape
		self.fps = fps
		# for the awesome technology that films in 'portrait' mode, but phones store the data as 'landscape',
		# however for all intents and purposes, we must read it as 'portrait'.
		self.isPortrait = isPortrait
		self.shape = (self.baseShape[0], self.baseShape[2], self.baseShape[1], self.baseShape[3]) \
			if self.isPortrait else self.baseShape

	# @brief Creates a copy of this MPLVideo object
	# @return A copy of this video
	def copy(self) -> MPLVideo:
		dataCopy = copy(self.data)
		if isinstance (dataCopy, np.ndarray):
			isPortrait = False
		else:
			isPortrait = self.isPortrait
		return MPLVideo(dataCopy, self.fps, isPortrait, self.baseShape, self.nFrames)

	def __getitem__(self, key):
		if isinstance(key, slice):
			# Slicing is troubling. If the underlying reader converts it to numpy (thus accessing element by element)
			#  then it's no longer a portrait mode (but a regular one). However, if it's slicing (i.e. not accessing)
			#  then we need to make sure the data remains in portrait mode!
			assert key.step is None
			sliceData = self.data[key]
			sliceNFrames = len(sliceData)
			sliceShape = (sliceNFrames, *self.baseShape[1 :])
			if isinstance(sliceData, np.ndarray):
				sliceIsPortrait = False
			else:
				sliceIsPortrait = self.isPortrait
			return MPLVideo(sliceData, self.fps, sliceIsPortrait, sliceShape, sliceNFrames)
		
		item = self.data[key]
		if isinstance(item, NDArray):
			item = item.asnumpy()
		if self.isPortrait:
			# Landscape to portrait and via trapose & mirror
			item = item.transpose(1, 0, 2)
			item = np.flip(item, axis=1)
		return item

	def __setitem__(self, key, value):
		assert False, "Cannot set values to a video object. Use video.data or video[i] to get the frame."

	# def __getattr__(self, key):
	# 	print(key)
	# 	# if key == "shape":
	# 	# 	if self.isPortrait:
	# 	# 		N, H, W, D = self.baseShape
	# 	# 		return (N, W, H, D)
	# 	# 	else:
	# 	# 		return self.baseShape
	# 	# Convert to numpy array.
	# 	# elif key == "__array_struct__":
	# 	# 	npData = np.array(self.data)
	# 	# 	return npData.__array_struct__
	# 	# elif key == "__array_interface__":
	# 	# 	npData = np.array(self.data)
	# 	# 	return npData.__array_interface__
	# 	# else:
	# 	# if key == "nFrames":
	# 	# 	breakpoint()
	# 	return getattr(self, key)

	def __len__(self):
		return len(self.data)

	def __eq__(self, other:MPLVideo):
		try:
			check1 = self.nFrames == other.nFrames
		except Exception as e:
			logger.debug(e)
			breakpoint()

		check = check1 and (self.shape == other.shape) and \
			(self.fps == other.fps) and (self.isPortrait == other.isPortrait)
		if not check:
			return False

		for i in range(len(self)):
			# if not np.abs(self[i] - other[i]).sum() < 1e-5:
			if not np.allclose(self[i], other[i]):
				return False
		return True

	def __deepcopy__(self, x):
		return self.copy()

	# @brief Applies a function to each frame of the self video and creates a new video with the applied function.
	#  The callable prototype is (video, timestep) and must return a modified frame of video[timestep]
	# @return A new video where each frame is updates according to the provided callback
	def apply(self, applyFn:Callable[[MPLVideo, int], np.ndarray]) -> MPLVideo:
		N = len(self)
		firstFrame = applyFn(self, 0)
		newData = np.zeros((self.nFrames, *firstFrame.shape), dtype=np.uint8)
		newData[0] = firstFrame
		for i in drange(1, N, desc="[MPLVideo::apply]"):
			newFrame = applyFn(self, i)
			newData[i] = newFrame
		# Here we call MPLVideo as we basically rotate the video (in case of rotate 90) when accessing it.
		newShape = (N, *firstFrame.shape)
		return MPLVideo(newData, self.fps, isPortrait=False, shape=newShape, nFrames=self.nFrames)

	# @brief Saves the current video to the desired path. Calls tryWriteVideo with it's desired params, such as vidLib
	# @param[in] A path where to save this current file
	def write(self, path: str, apply_fn:Optional[Callable[[MPLVideo, int], np.ndarray]]=None, **kwargs):
		if apply_fn is None:
			logger.debug2("Apply function not set. Defaulting to video[t].")
			apply_fn = lambda video, t: video[t]
		from .writer import video_write
		video_write(self, path, apply_fn, **kwargs)

	def save(self, path: str, apply_fn:Optional[Callable[[MPLVideo, int], np.ndarray]]=None, **kwargs):
		self.write(path, apply_fn, **kwargs)

	def __str__(self) -> str:
		Str = "[MPL Video]"
		Str += f"\n-  Shape: {self.shape}."
		Str += f"\n-  Duration: {len(self)}."
		Str += f"\n-  FPS: {self.fps:.2f}."
		Str += f"\n-  Portrait: {self.isPortrait}."
		return Str
