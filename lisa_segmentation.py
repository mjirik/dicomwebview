import numpy as np

data = {}
rgba_array = []
# dictionary of labels: {"label value": [coordinates in rgb]}
dict_of_labels = {0: [0, 0, 0, 0], # nothing
                  1: [150, 150, 0, 127], # 1st half of liver
                  3: [0, 150, 150, 127], # 2nd half of liver
                  2: [150, 0, 0, 127], # portal vein
                  4: [], # 2nd half of pv
                  5: [150, 0, 150, 127], # seeds
                  10: [0, 255, 0, 127], # liver
                  20: [255, 0, 0, 127], # heart
                  30: [255, 200, 0, 127]} # spleen

# creating useble data for LISA
def create_data(length_x, length_y, length_z, data3d):
    rgba_array = np.empty((length_x, length_y, length_z))
    data["segmentation"] = np.zeros((length_x, length_y, length_z))
    data["data3d"] = data3d

# from LISA data to RGBA
def data_to_rgba():
    length_x = len(rgba_array)
    length_y = len(rgba_array[0])
    length_z = len(rgba_array[0][0])
    for i in range(0, length_x):
        for j in range(0, length_y):
            for k in range(0, length_z):
                for key, val in dict_of_labels.items():
                    if key == data["segmentation"][i][j][k]:
                        rgba_array[i][j][k] = key
    return rgba_array

# editing segmentation data for LISA and pushing them to segmentation
def push_segmentation(pixel_array, index, plane):
    # data["segmentation"][index] = ((data["segmentation"][index] != pixel_array[..., 3]).astype('int8') * {k for k, v in dict_of_labels.items() if v[0] == pixel_array[0]})
    for i in range(0, len(pixel_array)):
        for j in range(0, len(pixel_array[i])):
            value = 0;
            for k, v in dict_of_labels.items():
                if v[0] == pixel_array[i][j][0] and v[1] == pixel_array[i][j][1] and v[2] == pixel_array[i][j][2]:
                    value = k
                if plane == 0:
                    data["segmentation"][index][i][j] = value
                elif plane ==  1:
                    data["segmentation"][i][index][j] = value
                else:
                    data["segmentation"][i][j][index] = value

    # TODO zavolat segmentaci v lise
    ''' problém: když uživatel označuje vícero obrázků pro segmentaci -> tato funkce se volá vícekrát (resp. tolikrát, na kolika obrázcích jsou označeny labely)
        ... nelze zjistit, kolik obrázků bylo označováno ... nejlepší řešení: metoda push by se volala okamžitě, jakmile by uživatel nakreslil něco do obrázku,
        segmentace by se volala, jakmile by stisknul checkbox '''
    
    # returning RGBA
    # data_to_rgba()
    return rgba_array

#def push_resection_portal_vein(seeds):
#    data = resection_portal_vein_new(data, interactivity=False, seeds=seeds, organ_label=10, vein_label=3)
#    # nutno upravit předchozí funkci / napsat novou - smazání vizualizace