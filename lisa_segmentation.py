import numpy as np

data = {}
# dictionary of labels: {"label value": [coordinates in rgb]}
dict_of_labels = {0: [0, 0, 0, 0], # nothing
                  10: [0, 255, 0, 127], # liver
                  20: [255, 0, 0, 127], # heart
                  30: [255, 200, 0, 127]} # spleen

# creating useble data for LISA
def create_data(length_x, length_y, length_z, data3d):
    data["segmentation"] = np.zeros((length_x, length_y, length_z))
    data["data3d"] = data3d

# editing segmentation data for LISA and pushing them to segmentation
def push_segmentation(pixel_array, index, plane):
    # data["segmentation"][index] = ((data["segmentation"][index] != pixel_array[..., 3]).astype('int8') * {k for k, v in dict_of_labels.items() if v[0] == pixel_array[0]})
    for i in range(0, len(pixel_array)):
        for j in range(0, len(pixel_array[i])):
            value = 0;
            for k, v in dict_of_labels.items():
                if v[0] == pixel_array[i][j][0] and v[1] == pixel_array[i][j][1] and v[2] == pixel_array[i][j][2]:
                    value = k
            data["segmentation"][index][i][j] = value
    # TODO zavolat segmentaci v lise
    
    # returning RGBA
    length_x = len(data["segmentation"])
    length_y = len(data["segmentation"][0])
    length_z = len(data["segmentation"][0][0])
    rgba_array = np.empty((length_x, length_y, length_z))
    # for i in range(0, length_x):
    #     for j in range(0, length_y):
    #         for k in range(0, length_z):
    #             for key, val in dict_of_labels.items():
    #                 if key == data["segmentation"][i][j][k]:
    #                     rgba_array[i][j][k] = key
    return rgba_array
