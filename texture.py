import numpy as np


def apply_texture(pix_array, texture, color1, color2):
    if texture == "STRAIGHT":
        # nothing to be done
        return pix_array
    elif texture == "WAVY":
        amplitude = 5
        frequency = np.pi / 40
        frequency_offset1 = 40 / len(pix_array)
        frequency_offset2 = 40 / len(pix_array[0])

        wavy1 = np.copy(pix_array)
        for i in range((len(pix_array))):
            offset = int(amplitude * np.sin(frequency * i) + frequency_offset1)
            wavy1[i] = np.roll(pix_array[i], (offset, offset, offset))

        pix_array = np.rot90(pix_array, k=1, axes=(0, 1))
        wavy2 = np.copy(pix_array)
        for i in range((len(pix_array))):
            offset = int(amplitude * np.sin(frequency * i) + frequency_offset2)
            wavy2[i] = np.roll(pix_array[i], (offset, offset, offset))
        pix_array = np.rot90(pix_array, k=1, axes=(1, 0))
        wavy2 = np.rot90(wavy2, k=1, axes=(1, 0))
        hits = [False, False, False, False]
        for i in range(len(pix_array)):
            progress = int(100*(i/len(pix_array)))
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
            for j in range(len(pix_array[0])):
                if np.all(pix_array[i][j] == wavy1[i][j]) and np.all(pix_array[i][j] == wavy2[i][j]):
                    continue
                elif np.all(pix_array[i][j] != wavy1[i][j]) and np.all(pix_array[i][j] != wavy2[i][j]):
                    if np.any(pix_array[i][j] == color1):
                        pix_array[i][j] = color2
                    else:
                        pix_array[i][j] = color1
                # elif np.all(pix_array[i][j] != wavy1[i][j]) and np.all(pix_array[i][j] == wavy2[i][j]):
                #     pix_array[i][j] = np.array([0, 0, 255])
                else:
                    if np.any(pix_array[i][j] == color1):
                        pix_array[i][j] = color2  # np.array([255, 255, 0])  color2
                    else:
                        pix_array[i][j] = color1  # np.array([0, 0, 255])    color1
        print("\t100%")
        return pix_array
    else:
        amplitude = 5
        #
        frequency = np.pi / 10
        frequency_offset1 = 40 / len(pix_array)
        frequency_offset2 = 40 / len(pix_array[0])

        wavy1 = np.copy(pix_array)
        for i in range((len(pix_array))):
            offset = int(amplitude * np.sin(frequency * i) + frequency_offset1)
            wavy1[i] = np.roll(pix_array[i], (offset, offset, offset))

        pix_array = np.rot90(pix_array, k=1, axes=(0, 1))
        wavy2 = np.copy(pix_array)
        for i in range((len(pix_array))):
            offset = int(amplitude * np.sin(frequency * i) + frequency_offset2)
            wavy2[i] = np.roll(pix_array[i], (offset, offset, offset))
        pix_array = np.rot90(pix_array, k=1, axes=(1, 0))
        wavy2 = np.rot90(wavy2, k=1, axes=(1, 0))
        hits = [False, False, False, False]
        for i in range(len(pix_array)):
            progress = int(100 * (i / len(pix_array)))
            if not hits[0] and progress >= 20:
                print("\t" + str(progress) + "%")
                hits[0] = True
            elif not hits[1] and progress >= 40:
                print("\t" + str(progress) + "%")
                hits[1] = True
            elif not hits[2] and progress >= 60:
                print("\t" + str(progress) + "%")
                hits[2] = True
            elif not hits[3] and progress >= 80:
                print("\t" + str(progress) + "%")
                hits[3] = True
            for j in range(len(pix_array[0])):
                if np.all(pix_array[i][j] == wavy1[i][j]) and np.all(pix_array[i][j] == wavy2[i][j]):
                    continue
                elif np.all(pix_array[i][j] != wavy1[i][j]) and np.all(pix_array[i][j] != wavy2[i][j]):
                    if np.any(pix_array[i][j] == color1):
                        pix_array[i][j] = color2
                    else:
                        pix_array[i][j] = color1
                # elif np.all(pix_array[i][j] != wavy1[i][j]) and np.all(pix_array[i][j] == wavy2[i][j]):
                #     pix_array[i][j] = np.array([0, 0, 255])
                else:
                    if np.any(pix_array[i][j] == color1):
                        pix_array[i][j] = color2  # np.array([255, 255, 0])  color2
                    else:
                        pix_array[i][j] = color1  # np.array([0, 0, 255])    color1
        print("\t100%")
        return pix_array
