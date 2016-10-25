
# David Daugela
# CS 1026


import math


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
    if numTimesAsked > 1 and not userInp == "cube" and not userInp == "pyramid" \
            and not userInp == "ellipsoid" and not userInp == "quit":
        print('Valid inputs are: "cube", "pyramid", "ellipsoid" and "quit" ')

#  Storing volumes of entered shapes without formatting
cubeVolumeList = []
pyramidVolumeList = []
ellipsoidVolumeList = []

# 3 Functions below to compute volume of entered shapes
#  @param: nothing
#  @return: volume of shape

def volume_cube():
    sideLength = float(input("Please input the side lengths of the cube: "))
    volCube = sideLength ** 3
    print("The volume of a cube with sidelengths of %.2f" % sideLength, "is %.2f" % volCube)
    return volCube


def volume_pyramid():
    baseLength = float(input("Please input the base length of the pyramid: "))
    heightLength = float(input("Please input the height of the pyramid: "))
    volPyramid = 0.50*(baseLength**2)*heightLength
    print("The volume of a pyramid with a base of %.2f" % baseLength, "and height %.2f"
          % heightLength, "is %.2f" % volPyramid)
    return volPyramid


def volume_ellipsoid():
    radius1 = float(input("Please input radius 1 of the ellipsoid: "))
    radius2 = float(input("Please input radius 2 of the ellipsoid: "))
    radius3 = float(input("Please input radius 3 of the ellipsoid: "))
    volEllipsoid = (4/3) * math.pi * radius1 * radius2 * radius3
    print("The volume of a pyramid with a radius one of %.2f" % radius1, "and radius 2 of %.2f" % radius2,
          "and radius 3 of %.2f" % radius3, "is %.2f" % volEllipsoid)
    return volEllipsoid

#  For first input, if string entered is "quit"
quit1 = ""
if userInp == "quit":
        print("You have come to the end of the session")
        print("You did not perform any volume calculations")
        quit1 = True


#  Asks user for inputs and appends results to unformatted list
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

# Current Variable

# Decimal formatting earlier volume calculations
decimalCubeVolumeList = []  # Cube volumes decimal decimal
cubeListTwo = map(float, sorted(cubeVolumeList, key=int))
for item in cubeListTwo:
    decimalCubeVolumeList.append("{0:.2f}".format(item))
decimalPyramidVolumeList = []  # Pyramid volumes decimal formatted
pyramidListTwo = map(float, sorted(pyramidVolumeList, key=int))
for item in pyramidListTwo:
    decimalPyramidVolumeList.append("{0:.2f}".format(item))
decimalEllipsoidVolumeList = []  # Ellipsoid volumes decimal formatted
ellipsoidListTwo = map(float, sorted(ellipsoidVolumeList, key=int))
for item in ellipsoidListTwo:
    decimalEllipsoidVolumeList.append("{0:.2f}".format(item))


# String formatting function to eliminate unwanted brackets and apostrophes
# @param: char1 and char2 and char 3 are undesired characters, which will be replaced
# @param: listInp is the original list that you want to be cloned and returned without the desired characters
# @return: a clone of listInp without the desired characters that were in listInp

def replace_3_char_blank(char1, char2, char3, listInp):
    temp1 = listInp.replace(char1, "")
    temp2 = temp1.replace(char2, "")
    temp3 = temp2.replace(char3, "")
    return temp3


if userInp == "quit" and not quit1:
        print("-" * 70)
        print("Volumes of inputted cubes are: ", replace_3_char_blank('[', ']', "'", str(decimalCubeVolumeList)))
        print("Volumes of inputted pyramids are: ", replace_3_char_blank('[', ']', "'", str(decimalPyramidVolumeList)))
        print("Volumes of inputted ellipsoids are: ", replace_3_char_blank('[', ']', "'", str(decimalEllipsoidVolumeList)))
