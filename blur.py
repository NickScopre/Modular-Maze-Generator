import numpy as np


def gaussian_blur(pix_array, blur):
    if blur == "NONE":
        # nothing to be done
        return pix_array
    elif blur == "MEDIUM":
        radius = 5
    elif blur == "STRONG":
        radius = 10
    else:
        radius = blur
    blur_array = np.copy(pix_array)
    # each row
    hits = [False, False, False, False]
    for i in range(len(pix_array)):
        progress = int(100 * (i / len(pix_array)))
        if not hits[0] and progress >= 20:
            print("\t"+str(progress) + "%")
            hits[0] = True
        elif not hits[1] and progress >= 40:
            print("\t"+str(progress) + "%")
            hits[1] = True
        elif not hits[2] and progress >= 60:
            print("\t"+str(progress) + "%")
            hits[2] = True
        elif not hits[3] and progress >= 80:
            print("\t"+str(progress) + "%")
            hits[3] = True
        # each column
        for j in range(len(pix_array[0])):
            # each rgb value
            for a in range(3):
                blur_array[i, j, a] = area_average(radius, pix_array, i, j, a)
    print("\t100%")
    return blur_array


def area_average(radius, pix_arr, row, col, color_idx):
    rgb_sum = 0
    observations = 0
    # while row - radius is out of bounds, increase starting row
    while row - radius < 0:
        row += 1
    # while col - radius is out of bounds, increase starting col
    while col - radius < 0:
        col += 1
    # while row + radius is out of bounds, decrease starting row
    while row + radius >= len(pix_arr):
        row -= 1
    # while col + radius is out of bounds, decrease starting col
    while col + radius >= len(pix_arr[0]):
        col -= 1
    for i in range(-radius, radius + 1, 1):
        for j in range(-radius, radius + 1, 1):
            rgb_sum += pix_arr[i + row, j + col, color_idx]
            observations += 1
    return rgb_sum//observations
