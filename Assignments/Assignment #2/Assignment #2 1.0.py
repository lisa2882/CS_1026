

import math
#  Determine Shape via user input


# @param nothing
#  @return is the shape to be evaluated
def ask_for_shape():
    shapetype = ""
    shapetype += str(input("Please input the shape that you are interested in: ")).lower()
    return shapetype

# Sanitizing shape input
numTimesAsked = 0
if numTimesAsked < 1:
    userInp = ask_for_shape()
while (not userInp == "cube" and not userInp == "pyramid"
    and not userInp == "ellipsoid" and not userInp == "quit"):
    print("Input is not a vaild shape")
    numTimesAsked += 1
    userInp = ask_for_shape()
    if numTimesAsked > 1:
        print('Valid inputs are: "cube", "pyramid", "ellipsoid" and "quit" ')


# Asking for appropriate lengths

cubeVolumeList = []
pyramidVolumeList = []
ellipsoidVolumeList =[]


def volume_cube():
    sideLength = int(input("Please input the side lengths of the cube: "))
    volCube = sideLength ** 3
    return volCube


def volume_pyramid():
    baseLength = int(input("Please input the base length of the pyramid: "))
    heightLength = int(input("Please input the height of the pyramid: "))
    volPyramid = (1/2)*(baseLength**2)*heightLength
    return volPyramid


def volume_ellipsoid():
    radius1 = int(input("Please input radius 1 of the ellipsoid: "))
    radius2 = int(input("Please input radius 2 of the ellipsoid: "))
    radius3 = int(input("Please input radius 3 of the ellipsoid: "))
    volEllipsoid = (4/3) * math.pi * radius1 * radius2 * radius3
    return volEllipsoid

while userInp == "cube" or userInp == "pyramid" or userInp == "ellipsoid":
    while userInp == "cube":  # cube
        cubeVolumeList.append(volume_cube())
        userInp = ask_for_shape()
    while userInp == "pyramid":  # pyramid
        pyramidVolumeList.append(volume_pyramid())
        userInp = ask_for_shape()
    while userInp == "ellipsoid":  # ellipsoid
        ellipsoidVolumeList.append(volume_ellipsoid())
        userInp = ask_for_shape()

if userInp == "quit":
        print("Volumes of inputted cubes are: ", cubeVolumeList)
        print("Volumes of inputted pyramids are: ", pyramidVolumeList)
        print("Volumes of inputted ellipsoids are: ", ellipsoidVolumeList)

