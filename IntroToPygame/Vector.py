import math

# Used to represent quantities like position/movement
class Vector:
    # Constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Converts a vector to a string
    def __str__(self):
        return ("Vector(" + str(self.x) + "," + str(self.y) + ")")

    # Adds two vectors together
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    # Subtracts two vectors from each other
    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    # Multiplies a vector by an int
    def __mult__(self, other):
        return Vector(self.x * other.x, self.y * other.y)
    
    # Returns dot product of two vectors
    def dot(self, other):
        return ((self.x * other.x) + (self.y * other.y))

    # Scales the vector by a float value
    def scale(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
    
    # Returns the magnitude of a vector
    def length(self):
        return (math.sqrt((self.x * self.x) + (self.y * self.y)))
    
    # Normalizes the vector by changing its length to 1 while pointing in the same direction
    def normalize(self):
        # Store self.length because sqrt is expensive
        leng = self.length()

        # Check if length is 0 to prevent divide-by-zero errors
        if leng == 0:
            return Vector(0,0)
        else:
            return Vector(self.x / leng, self.y / leng)

    # Returns a zero Vector
    def zero():
        return (Vector(0,0))