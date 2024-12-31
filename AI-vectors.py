# Standard library imports
import math

# Third-party library imports
import numpy as np
# from scipy.spatial import distance  # Uncomment if needed

class VectorData:
    def __init__(self, vector):
        if not isinstance(vector, (list, np.ndarray)):
            raise ValueError("Input vector must be a list or a NumPy array.")
        self.vector = np.array(vector)
        
    def vector_addition(self, vec2):
        vec2 = np.array(vec2)
        if self.vector.shape != vec2.shape:
            raise ValueError("Vectors must have the same dimensions for addition.")
        return self.vector + vec2
    
    def vector_subtraction(self, vec2):
        vec2 = np.array(vec2)
        if self.vector.shape != vec2.shape:
            raise ValueError("Vectors must have the same dimensions for subtraction.")
        return self.vector - vec2
    
    def vector_magnitude(self, vec=None):
        vec = self.vector if vec is None else np.array(vec)
        if not isinstance(vec, np.ndarray):
            raise ValueError("Input must be a NumPy array or list.")
        return math.sqrt(sum(x**2 for x in vec))
    
    def dot_product(self, vec2):
        vec2 = np.array(vec2)
        if self.vector.shape != vec2.shape:
            raise ValueError("Vectors must have the same dimensions for the dot product.")
        return np.dot(self.vector, vec2)
    
    def vector_proportions(self, vec2):
        vec2 = np.array(vec2)
        m1 = self.vector_magnitude(self.vector)
        m2 = self.vector_magnitude(vec2)
        if m2 == 0:
            raise ZeroDivisionError("Cannot compute proportions with a zero-magnitude vector.")
        return m1 / m2
