
#  Determine Shape via user input


# @param nothing
#  @return is the shape to be evaluated
def ask_for_shape():
    shapetype = ""
    shapetype += str(input("Please input the shape that you are interested in: ")).lower()
    return shapetype

# Sanitizing input
numTimesAsked = 0
if numTimesAsked < 1:
    userInp = ask_for_shape()
while (not userInp == "cube" and not userInp == "pyramid"
    and not userInp == "ellipsoid" and not userInp == "quit"):
    print("Input is not a vaild shape")
    userInp = ask_for_shape()
    numTimesAsked += 1