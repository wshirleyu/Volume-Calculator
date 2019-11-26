#

# Volume file stores volume functions for cube, pyramid, and ellipsoid

# import pi from math module for use in ellipsoid function
from math import pi

# Define cube volume function with cube formula, rounding to three decimals
def cubeVolume(sideLength):
    volume = sideLength ** 3
    return round(volume, 3)

# Define pyramid volume function with pyramid formula, rounding to three decimals
def pyramidVolume(base, height):
    volume = ((base ** 2) * height) / 3
    return round(volume, 3)

# Define ellipsoid volume function with ellipsoid formula, rounding to three decimals
def ellipsoidVolume(radius1, radius2, radius3):
    volume = (pi * radius1 * radius2 * radius3) * (4/3)
    return round(volume, 3)






