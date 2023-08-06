from typing import Any
import ffmpeg

def is_rotated_90(path: str, data: Any) -> bool:
	ix = []
	f = ffmpeg.probe(path)
	for i, stream in enumerate(f["streams"]):
		if ("codec_type" in stream) and (stream["codec_type"] == "video"):
			ix.append(i)
	assert len(ix) == 1
	stream = f["streams"][ix[0]]

	# Other weird cases ? We'll see...
	if (not "tags" in stream) or (not "rotate" in stream["tags"]):
		return False

	if stream["tags"]["rotate"] != "90":
		return False

	# Some good shit happening here.
	strType = str(type(data)).split(".")[-1][0:-2]
	# Basically, ImageIOReader decided to transpose it by default for us.
	if strType == "ImageIOReader":
		return False
	# PyAVTimedReader decided to not transpose it at all.
	elif strType == "PyAVReaderTimed":
		return True
	# We'll see for other cases... we assume to it is not transposed.
	return True
