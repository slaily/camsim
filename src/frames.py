import numpy as np


def generate_black_frame(height, width):
    return np.zeros((height, width, 3), np.uint8)
