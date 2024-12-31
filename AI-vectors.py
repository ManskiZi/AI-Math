# Standard library imports
import math

# Third-party library imports
import numpy as np
# from scipy.spatial import distance  # Uncomment if needed


def vector_addition(vec1, vec2):
    return np.array(vec1) + np.array(vec2)

def vector_magnitude(vec):
    return math.sqrt(sum(x**2 for x in vec))
