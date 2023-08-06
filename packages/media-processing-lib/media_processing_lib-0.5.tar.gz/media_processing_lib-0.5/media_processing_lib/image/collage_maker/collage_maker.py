import numpy as np
from pathlib import Path
from typing import List, Optional, Callable, Tuple
from tqdm import trange

from .utils import get_closest_square, auto_load_fn, collage_fn
from ..image_writer import image_write

class CollageMaker:
    def __init__(self, files: List[List[Path]], plotFns: List[Callable], outputDir: Path, \
            loadFns: Optional[List[Callable]]=None, names: Optional[List[str]]=None, \
            rowsCols: Optional[Tuple[int, int]]=None):
        assert isinstance(files, List)
        self.files = np.array([[Path(x) for x in y] for y in files])
        self.lens = [len(x) for x in self.files]
        self.outputDir = Path(outputDir)
        self.names = names
        self.rowsCols = get_closest_square(len(self.files)) if rowsCols is None else rowsCols
        nOutputs = len(self.files)

        # Bravely assuming all items can be plotted the same
        if isinstance(plotFns, Callable):
            plotFns = nOutputs * [plotFns]
        self.plotFns = plotFns
        # Bravely assuming we can infer the load fn based on suffixes
        if loadFns is None:
            loadFns = [auto_load_fn(x[0]) for x in self.files]
        # Bravely assuming all items can be loaded the same
        if isinstance(loadFns, Callable):
            loadFns = nOutputs * [loadFns]
        self.loadFns = loadFns

        assert np.std(self.lens) == 0, self.lens
        assert len(self.plotFns) == nOutputs, f"{len(self.plotFns)} vs. {nOutputs}"
        if self.names is not None:
            assert len(self.names) == nOutputs
        if self.rowsCols is not None:
            assert self.rowsCols[0] * self.rowsCols[1] >= nOutputs, \
                f"Rows ({self.rowsCols[0]}) * Cols ({self.rowsCols[1]}) < Outputs ({nOutputs})"

    def make_collage(self, startIx: Optional[int]=None, endIx: Optional[int]=None) -> np.ndarray:
        startIx = startIx if not startIx is None else 0
        endIx = endIx if not endIx is None else len(self.files[0])
        assert startIx < endIx
        assert endIx <= len(self.files[0]), f"{endIx} vs {len(self.files[0])}"
        self.outputDir.mkdir(parents=True, exist_ok=False)
        if self.names is not None:
            open(self.outputDir / "order.txt", "w").write(",".join(self.names))

        for i in trange(startIx, endIx):
            thisPaths = self.files[:, i]
            items = [loadFn(x) for loadFn, x in zip(self.loadFns, thisPaths)]
            images = [plotFn(x) for plotFn, x in zip(self.plotFns, items)]
            result = collage_fn(images, self.rowsCols, self.names)

            # Save to disk
            outFile = f"{self.outputDir}/{i}.png"
            image_write(result, outFile)

    def __call__(self, *args, **kwargs):
        return self.make_collage(*args, **kwargs)

    def __str__(self) -> str:
        Str = "[Collage Maker]"
        Str += f"\n - Num outputs: {len(self.files)}. Rows x Cols: {self.rowsCols}"
        Str += f"\n - Lens: {self.lens}"
        if self.names is not None:
            Str += f"\n - Names: {self.names}"
        Str += f"\n - Output dir: {self.outputDir}"
        return Str
