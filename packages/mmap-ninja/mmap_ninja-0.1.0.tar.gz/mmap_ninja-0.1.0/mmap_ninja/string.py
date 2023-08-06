import mmap
from pathlib import Path
from typing import Sequence, Union

import numpy as np

from mmap_ninja import numpy
from mmap_ninja.base import bytes_to_str, str_to_bytes, sequence_of_strings_to_bytes


class StringsMmmap:

    def __init__(self, data_file: Union[str, Path], starts, ends, mode='r+b'):
        self.data_file = Path(data_file)
        self.mode = mode
        self.starts = starts
        self.ends = ends
        self.range = np.arange(len(starts), dtype=np.int32)
        self.file = open(data_file, mode=mode)
        self.buffer = mmap.mmap(self.file.fileno(), 0)

    def get_multiple(self, item):
        indices = self.range[item]
        return [self.__getitem__(idx) for idx in indices]

    def get_single(self, item):
        start = self.starts[item]
        end = self.ends[item]
        return bytes_to_str(self.buffer[start:end])

    def __getitem__(self, item):
        if np.isscalar(item):
            return self.get_single(item)
        return self.get_multiple(item)

    def __setitem__(self, key, value):
        if np.isscalar(key):
            return self.set_single(key, value)
        return self.set_multiple(key, value)

    def __len__(self):
        return len(self.starts)

    def set_multiple(self, key, value):
        for i, idx in enumerate(self.range[key]):
            new_value: str = value[i]
            self.set_single(idx, new_value)

    def set_single(self, idx, new_value):
        start = self.starts[idx]
        end = self.ends[idx]
        self.buffer[start:end] = str_to_bytes(new_value)

    def close(self):
        self.buffer.close()
        self.file.close()

    def extend(self, list_of_strings: Sequence[str], verbose=False):
        buffer, start_offsets, end_offsets = sequence_of_strings_to_bytes(list_of_strings, verbose=verbose)
        end = self.ends[-1]
        start_offsets = end + start_offsets
        end_offsets = end + end_offsets
        numpy.extend(self.starts, start_offsets)
        numpy.extend(self.ends, end_offsets)
        self.close()
        out_dir = self.data_file.parent
        with open(out_dir / 'data.ninja', 'ab') as data_file:
            data_file.write(buffer)
            data_file.flush()
        self.starts = numpy.open_existing(out_dir / 'starts', mode='r')
        self.ends = numpy.open_existing(out_dir / 'ends', mode='r')
        self.file = open(self.data_file, mode=self.mode)
        self.buffer = mmap.mmap(self.file.fileno(), 0)
        self.range = np.arange(len(self.starts), dtype=np.int32)

    def append(self, string: str):
        self.extend([string])

    @classmethod
    def from_strings(cls, strings: Sequence[str], out_dir: Union[str, Path], verbose=False):
        out_dir = Path(out_dir)
        out_dir.mkdir(exist_ok=True)
        buffer, starts, ends = sequence_of_strings_to_bytes(strings, verbose=verbose)
        with open(out_dir / 'data.ninja', "wb") as f:
            f.write(buffer)
        numpy.from_ndarray(np.array(starts, dtype=np.int32), out_dir / 'starts')
        numpy.from_ndarray(np.array(ends, dtype=np.int32), out_dir / 'ends')
        return cls.open_existing(out_dir)

    @classmethod
    def from_generator(cls, sample_generator,
                       out_dir: Union[str, Path],
                       batch_size: int,
                       verbose=False):
        out_dir = Path(out_dir)
        out_dir.mkdir(exist_ok=True)
        samples = []
        memmap = None
        if verbose:
            from tqdm import tqdm
            sample_generator = tqdm(sample_generator)
        for sample in sample_generator:
            samples.append(sample)
            if len(samples) % batch_size != 0:
                continue
            if memmap is None:
                memmap = cls.from_strings(samples, out_dir)
            else:
                memmap.extend(samples)
            samples = []
        if len(samples) > 0:
            if memmap is None:
                memmap = cls.from_strings(samples, out_dir)
            else:
                memmap.extend(samples)
        return memmap

    @classmethod
    def open_existing(cls, out_dir: Union[str, Path], mode='r+b'):
        out_dir = Path(out_dir)
        out_dir.mkdir(exist_ok=True)
        starts_np = numpy.open_existing(out_dir / 'starts', mode='r')
        ends_np = numpy.open_existing(out_dir / 'ends', mode='r')
        return cls(out_dir / 'data.ninja', starts_np, ends_np, mode=mode)
