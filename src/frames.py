import numpy as np


def generate_black_frame(height, width):
    return np.zeros((height, width, 3), np.uint8)


def generate_color_frame(height, width):
    return np.random.randint(
        0,
        high=256,
        size=((height, width, 3)),
        dtype=np.uint8
    )
