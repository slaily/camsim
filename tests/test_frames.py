import numpy as np

from src.frames import *


def test_black_frame():
    frame = generate_black_frame(32, 32)

    assert not np.any(frame)


def test_generate_color_frame():
    frame = generate_color_frame(32, 32)
    _, _, channels = frame.shape

    assert channels == 3
