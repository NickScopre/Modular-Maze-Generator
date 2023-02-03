# Modular Maze Generator

## Description
This is a tool for generating mazes with the same parameters in bulk. 
These parameters include:
- Path Color
- Wall Color 
- Number of Rows
- Number of Columns
- Maze Texture
- Blur Effect
The maze texture can either be straight, wavy, or jagged.
The blur effect uses a box based gaussian blur.
The default distance of medium being 5, and strong being 10. A custom value may be entered.


## Installation
### If you are already familiar with Python:
Just download the source and set up a virtual environment using `requirements.txt`.

### If you are not:
1. [Download Python](https://www.python.org/downloads/). Make sure to select the "Add to PATH" option during installation.

2. Download the Repository from the [Releases](https://github.com/NickScopre/Modular-Maze-Generator) page.

3. Unzip the file into whatever folder you like

4. Open the Command Prompt (or if on Mac/Linux, the equivalent terminal) and [Navigate](https://www.digitalcitizen.life/command-prompt-how-use-basic-commands/#ftoc-heading-3) to the same folder you extracted the repository into.
This should be the same folder that contains `editor_site.py` as well as the rest of the scripts.

5. Create a Virtual Environment
Use `python -m venv ./venv` to create a Virtual Environment for the program to run in. You can technically skip this if you really wanted to,  but a virtual environment is best practice.

6. Enter the Virtual Environment
Use `venv\Scripts\activate` to activate and enter the Virtual Environment. This is the only step you will have to repeat after initial setup.

7. Install Dependencies
Use `pip install -r requirements.txt` to download the required packages for MMG. 

If you've closed the terminal window and need to return to GalaxyGen, you simply need to navigate back to the same directory and run `venv\Scripts\activate`. (Equivalent to steps 4 and 6) This will put you back into GalaxyGen's environment and allow you to run its scripts.

## How it works
###1. Maze Structure Generation
After taking in user input, makeMaze is called. The maze is made up of cell objects with 4x4 numpy array of 0s representing path, and 1s representing walls. 
All of these cells are then put in a 2D numpy array with a length and width specified by user inputted rows and columns. Every cell that is
visited is placed into a list, starting with the top left cell. The visited list is shuffled and iterated through, and for each cell in 
the visited list (which at the beginning is only the top left cell) has all of its neighbors checked one whether they are in bounds and not 
visited. If both of these conditions are met, the next cell is determined to be the first cell determined to be valid by those conditions. 
The order in which neighbors are checked is Top, Right, Left, Bottom, meaning there may be some bias in generation, although it seems to 
be negligible. From there a path is made between the first valid neighbor and by calling the recursive function makeAPath. This function 
makes a path between two cells by calling the Cell member function, makePath, which determines the orientation of two cells, ensures the 
cells are neighbors, and sets individual indexes within the internal 4x4 array of each cell to 0, aka path. Whenever a cell has a path made 
with it, it is added to the visited list. The makeAPath recursive function calls itself with the cell that just had a path made to it as the
starting cell. The makeAPath recursive function will call itself until the next cell has no neighbors, in which case it returns and the 
makeMaze function will continue to iterate through the again shuffled list of visted cells, checking for neighbors that are unvisited, and
making paths through them in this same manner until the length of the visited list is the same as the product of rows and columns, meaning 
every cell has been visited. The main 2D numpy array then has each index of each cells' 4x4 array copied into its own index of a new array
4 times the width and height of the wall/path array, with each index taking a 1x3 numpy array storing the RGB values entered by the user.
This array is then returned to the main function.
###2. Scaling the Maze
Since the maze isn't just supposed to be an abstract object but an actual image, the array is scaled up since each index now represents a 
pixel on the image. I found a scale factor of 10 seemed to be sufficient in not blowing an image up too big but also giving the wavy and 
jagged textures enough room to show their shape. This uses a numpy function, kron, to scale the image and to ensure the data type of each
index is UINT8, since thats what MatPlotLib needs to save the image as a PNG. 
###3. Pad the sides
This just expands the maze borders by 30 pixels each using another numpy function, pad. 
###4. Apply Texture
If the user selected straight, the maze continues as is. If they selected Wavy or Jagged, a process follows. 2D arrays within the current 3D 
pixel array are "rolled" increasing or decreasing the indicies of all elements by a value that is the product of a given amplitude, sin value
of a given frequency times the current index or the row/column being rolled, and a given offset used to line up the curves with the maze a bit
better. This happens once for horizontal rolling and once for vertical rolling, but both results are stored in a separate 3D array. A 3rd 3D
array is made by taking some elements from one rolled pixel array and some elements from another on numerous conditions. This seemingly 
redundant portion is actually extremely important to avoid wave distortion. 
###5. Blur
The blur effect is a relatively standard Gaussian Blur implementation. It goes cell by cell and takes a square with a side length double the 
given value. The average of all colors within the square is taken, and then applied to the individual cell. This is without a doubt the 
slowest part of the entire program and surely must have some room for improvement. 
###6. Export 
The numpy array is saved into an image using MatPlotLib's image package and uses Python's os package to determine where to save the mazes.