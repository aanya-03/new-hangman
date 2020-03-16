import numpy as np



def convert_to_homogeneous_coordinate(x_coordinate, y_coordinate,z_coordinate, no_of_coord):
    '''takes a list of x_coordinates, y_coordinates, z_coordinates and no of coordinates
    and runs a for loop for the coordinates and returns a
    list of homogeneous coordinate that has a bunch of homogeneous coordinates '''
    list_of_homogeneous_coordinate = []
    for i in range(no_of_coord):
        temp_x_coord = x_coordinate[i]
        temp_y_coord = y_coordinate[i]
        temp_z_coord = z_coordinate[i]
        homogeneous_coordinate = [temp_x_coord, temp_y_coord, temp_z_coord,1]
        homogeneous_coordinate = np.asarray(homogeneous_coordinate).reshape(4, 1)
        list_of_homogeneous_coordinate.append(homogeneous_coordinate)

    list_of_homogeneous_coordinate = np.asarray(list_of_homogeneous_coordinate)
    return list_of_homogeneous_coordinate


def translation(list_of_homogeneous_coordinate, no_of_coord):
    translated_x_coordinate = []
    translated_y_coordinate = []
    translated_z_coordinate = []
    tx = 100
    ty = 50
    tz = 25
    new_translated_coordinate = []
    translation_matrix = [1,0,0,tx,0,1,0,ty,0,0,1,tz,0,0,0,1,]
    translation_matrix = np.asarray(translation_matrix).reshape(4,4)
    for i in range(len(list_of_homogeneous_coordinate)):
        new_translated_coordinate.append(np.dot(translation_matrix, list_of_homogeneous_coordinate[i]))
        translated_x_coordinate.append(new_translated_coordinate[i][0][0])
        translated_y_coordinate.append(new_translated_coordinate[i][1][0])
        translated_z_coordinate.append(new_translated_coordinate[i][2][0])
    print("Translated X Coordinate: {}".format(translated_x_coordinate))
    print("Translated Y Coordinate: {}".format(translated_y_coordinate))
    print("Translated Z Coordinate: {}".format(translated_z_coordinate))
    # translated_homogeneous_coordinate = convert_to_homogeneous_coordinate(translated_x_coordinate, translated_y_coordinate, translated_z_coordinate,no_of_coord)
    # return translated_homogeneous_coordinate


def scaling(list_of_homogeneous_coordinate, no_of_coord):
    '''takes a list of homogenous coordinate and using matrix multiplication
    sacles the x_coordinate and y_coordinate according to their scale factors.'''
    scaled_x_coordinate = []
    scaled_y_coordinate = []
    scaled_z_coordinate = []
    sx =2
    sy =3
    sz = 3
    new_scaled_coordinate = []
    scaling_matrix = [sx,0,0,0,0,sy,0,0,0,0,sz,0,0,0,0,1]
    scaling_matrix = np.asarray(scaling_matrix).reshape(4,4)
    for i in range(len(list_of_homogeneous_coordinate)):
        new_scaled_coordinate.append(np.dot(scaling_matrix, list_of_homogeneous_coordinate[i]))
        scaled_x_coordinate.append(new_scaled_coordinate[i][0][0])
        scaled_y_coordinate.append(new_scaled_coordinate[i][1][0])
        scaled_z_coordinate.append(new_scaled_coordinate[i][2][0])
    print("Scaled X Coordinate: {}".format(scaled_x_coordinate))
    print("Scaled Y Coordinate: {}".format(scaled_y_coordinate))
    print("Scaled Z Coordinate: {}".format(scaled_z_coordinate))
    # scaled_homogeneous_coordinate = convert_to_homogeneous_coordinate(scaled_x_coordinate, scaled_y_coordinate, scaled_z_coordinate, no_of_coord)
    # return scaled_homogeneous_coordinate




def rotation(list_of_homogeneous_coordinate, theta = -90):
    '''' take a list of homogenous coordinates and rotates it by an angle of 270 degree'''
    rotated_x_coordinate = []
    rotated_y_coordinate = []
    rotated_z_coordinate = []
    new_rotated_coordinate = []
    radian = ((2 * np.pi) / 360) * theta
    r = [1,0,0,0,
         0,np.cos(radian), -np.sin(radian), 0,
         0,np.sin(radian), np.cos(radian), 0,
         0,0, 0, 1]
    # print(list_of_homogeneous_coordinate)
    r = np.asarray(r).reshape(4, 4)
    for i in range(len(list_of_homogeneous_coordinate)):
        new_rotated_coordinate.append(np.dot(r, list_of_homogeneous_coordinate[i]))
        rotated_x_coordinate.append(new_rotated_coordinate[i][0][0])
        rotated_y_coordinate.append(new_rotated_coordinate[i][1][0])
        rotated_z_coordinate.append(new_rotated_coordinate[i][2][0])
    print("Rotated X Coordinate: {}".format(rotated_x_coordinate))
    print("Rotated Y Coordinate: {}".format(rotated_y_coordinate))
    print("Rotated Z Coordinate: {}".format(rotated_z_coordinate))
    return rotated_x_coordinate, rotated_y_coordinate, rotated_z_coordinate

