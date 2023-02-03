import matplotlib.image as img
import numpy

from maze_maker import makeMaze
from texture import apply_texture
from blur import gaussian_blur
import numpy as np
import os


# get_color() returns a list of 3 integers, an R, G, and B value
def get_color():
    color_type = input("\tWould you like to enter an RGB value or a color?\n\t[Enter \"RGB\" or \"COLOR\"]:  ")
    while True:
        if color_type == "RGB":
            try:
                color = input("\tEnter the RGB value in the following format: \"R\" \"G\" \"B\"\n"
                              "\tFor example, white is 255 255 255\n")
                color = np.array(color.split(), dtype=int)
            except ValueError:
                print("RGB Values can only be integers from 0 to 255.")
                continue
            # CHECK FOR RGB VALS OUTSIDE 0 TO 255
            if len(color) != 3:
                print("Please only include 3 integer values between 0 and 255, inclusive")
                continue
            return color
        elif color_type == "COLOR":
            while True:
                color = input("Enter a color from the following list.\n"
                              "\t[RED, ORANGE, YELLOW, GREEN, BLUE, PURPLE, WHITE, BLACK]: ")
                if color == "RED":
                    return np.array([255, 0, 0])
                elif color == "ORANGE":
                    return np.array([255, 165, 0])
                elif color == "YELLOW":
                    return np.array([255, 255, 0])
                elif color == "GREEN":
                    return np.array([0, 255, 0])
                elif color == "BLUE":
                    return np.array([0, 0, 255])
                elif color == "PURPLE":
                    return np.array([255, 0, 255])
                elif color == "WHITE":
                    return np.array([255, 255, 255])
                elif color == "BLACK":
                    return np.array([0, 0, 0])
                else:
                    print("Entered color is not recognized.")
        else:
            color_type = input("Please type \"RGB\" or \"COLOR\": ")


def exportMaze(r, c, pc, wc, t, b, n):
    # STEP 1: Make maze
    # pixel_array is a 3D numpy array that is 4 times the cols by 4 times the rows
    # the 3rd axis is a list of 3 integers, which are RGB values
    pixel_array = makeMaze(r, c, pc, wc)

    # STEP 2: Apply image details
    # scale pixel array up
    scale_factor = 10
    # Scale Array up 10x
    print("Scaling maze up...")
    pixel_array2 = numpy.kron(pixel_array, np.ones((scale_factor, scale_factor, 1), dtype=np.uint8))

    # STEP 3: Pad the sides
    print("Padding maze borders...")
    pixel_array3 = np.pad(pixel_array2, ((30, 30), (30, 30), (0, 0)), mode='edge')

    # STEP 4: Apply Texture
    print("Applying Texture...")
    pixel_array4 = apply_texture(pixel_array3, t, pc, wc)

    # STEP 5: Apply Blur effect
    print("Applying Blur...")
    pixel_array5 = gaussian_blur(pixel_array4, b)

    # STEP 6: Export
    print("Exporting...")
    # u = os.path.expanduser("~")
    # p = u + "\\Documents\\Nick's Mazes"
    p = "output"
    if not os.path.isdir(p):
        os.makedirs(p)    
    fig_name = "image" + str(n) + ".png"
    img.imsave(os.path.join(p, fig_name), pixel_array5)


print("The mazes you generate in bulk with have the same parameters (color, size, blur, etc).")
num_mazes = 0
while num_mazes <= 0:
    try:
        num_mazes = int(input("How many mazes would you like to make? "))
    except ValueError:
        print("You can only enter a positive integer, please try again.")
if num_mazes > 50:
    yes = input("That's a lot of mazes! It might take a little while, is that okay? (Y/N)\n")
    while yes != "Y" and yes != "N":
        yes = input("Please enter Y or N\n")
    if yes == "N":
        print("Terminating Program...")
        exit(0)
print("Warning, exceedingly large mazes may take longer to generate.")
print("Specify the type of maze you want to generate.")
print("Enter the size of the maze.")
while True:
    try:
        # number of rows of the maze        (height)
        rows = int(input("\tEnter the number of rows: "))
        # number of columns of the maze     (width)
        cols = int(input("\tEnter the number of columns: "))
        break
    except ValueError:
        print("Please type in an Integer for rows and columns.")

# path color:
print("\nEnter a color for the maze path.")
path_color = get_color()

# maze texture:
texture = "unassigned"
texture = input("\nWhat texture should the maze have?"
                "\n\t[\"STRAIGHT\", \"WAVY\", \"JAGGED\"]: ")
while texture != "STRAIGHT" and texture != "WAVY" and texture != "JAGGED":
    texture = input("Please enter a texture from the list below."
                    "\n\t[\"STRAIGHT\", \"WAVY\", \"JAGGED\"]: ")

# wall color:
print("\nEnter a color for the maze walls.")
wall_color = get_color()
# background texture:   Lattice, Bubble, Oval
# background filling:   Yes/No

# blur effect:
global blur
blur = input("\nWhat blur level? [\"NONE\", \"MEDIUM\", \"STRONG\", \"CUSTOM\"]: ")
while True:
    if blur == "CUSTOM":
        print("Enter an integer. This integer will be the distance of the blur from each point.\n"
              "Greater integers will yield blurrier mazes.\nFor reference, \"MEDIUM\" uses a distance\n"
              "of 5 and \"STRONG\" uses a distance of 10.")
        while type(blur) != int:
            blur = int(input("Enter an integer: "))
        break
    elif not (blur == "NONE" or blur == "MEDIUM" or blur == "STRONG"):
        blur = input("Blur level is not recognized. Please enter \"NONE\", \"MEDIUM\", or \"STRONG\".")

    else:
        print("Blur level selected: ", blur)
        break
for i in range(num_mazes):
    print("Generating maze ", i+1, " of ", num_mazes)
    exportMaze(rows, cols, path_color, wall_color, texture, blur, i)

print("Your mazes were saved to:")
path = os.path.join(os.getcwd(), "output")
print("\t", path)
