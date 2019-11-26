###
# Volume Calculator program
# By Shirley Wu
# Student number: 251082034

# Ensure that user input is not case sensitive with "formatInput" function
def formatInput(textLine) :
 textLine = textLine.lower()
 return textLine

# Import cube, pyramid, and ellipsoid volume functions from the "volume" file
from volume import cubeVolume
from volume import pyramidVolume
from volume import ellipsoidVolume

# Import the summarize function from the "summarize" file
from summarize import summarize

# Define initial test and shape variables with empty strings
test = ""
shape = ""

# Define initial shape dimension variables with values of 0
sideLength = 0
base = 0
height = 0
radius1 = 0
radius2 = 0
radius3 = 0

# Create empty lists to store cube, pyramid, and ellipsoid volumes
clist = []
plist = []
elist = []

# Prompt user for test number
test = input("Enter test number (1, 2, or 3): ")

# Loop user prompt for shape; loop will not proceed if termination code is entered
while shape != "q" or shape != "quit":
    shape = input("Enter shape (cube, pyramid, or ellipsoid; q or quit to terminate): ")
    shape = formatInput(shape)

    # "Sort" function used to sort the volumes calculated in order from smallest to greatest
    clist.sort()
    plist.sort()
    elist.sort()

# Prompt user for shape and corresponding dimensions
    if shape == "cube" or shape == "c":
        sideLength = input("Enter side length: ")
        # Use "int" to convert user input into an integer
        volume = cubeVolume(int(sideLength))
        # Use append function to add dimensions to corresponding list
        clist.append(volume)
    elif shape == "pyramid" or shape == "p":
        base = input("Enter base: ")
        height = input("Enter height: ")
        volume = pyramidVolume(int(base), int(height))
        plist.append(volume)
    elif shape == "ellipsoid" or shape == "e":
        radius1 = input("Enter radius 1: ")
        radius2 = input("Enter radius 2: ")
        radius3 = input("Enter radius 3: ")
        volume = ellipsoidVolume(int(radius1), int(radius2), int(radius3))
        elist.append(volume)

# If user inputs "quit" or "q", the program calculates the volumes of the shapes with dimensions entered by user
    elif shape == "quit" or shape == "q":
        # Use "summarize" function to output the volume results to test case files
        summarize(clist, plist, elist, test)
        print("You have reached the end of your session.")
        print("The volumes calculated for each shape are: ")
        print("Cube: " + str(clist))
        if not clist:
            print("No shapes entered")
        print("Pyramid: " + str(plist))
        if not plist:
            print("No shapes entered")
        print("Ellipsoid: " + str(elist))
        if not elist:
            print("No shapes entered")
        if clist == [] and plist == [] and elist == []:
            print("You did not perform any volume calculations.")
        break
# If user does not enter any shape or value, the program prints an error statement
    else:
        print("Error. Invalid shape.")
        shape = input("Enter shape (cube, pyramid, or ellipsoid; q or quit to terminate): ")

# End of program
