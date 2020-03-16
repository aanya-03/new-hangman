import numpy as np
import pygame, sys
from pygame.locals import *
from pygame import gfxdraw
from functions2 import convert_to_homogeneous_coordinate, convert_to_graph_coordinate, shearing, translation, rotation, reflection, scaling

pygame.init()

size = (700,700)
screen_surface = pygame.display.set_mode(size, 0, 32)
pygame.display.set_caption("Transformation")

BLACK = (0,0,0)
WHITE = (255,255,255)
RED = (255,0,0)
GREEN = (0,128,0)
BLUE = (0,0,255)

screen_surface.fill(WHITE)


#------------------------------------------------------------------------#

print("""
1. TRANSLATION
2. SCALING
3. ROTATION
4. REFLECTION
5.SHEARING""")

transformation = int(input("Enter the transformation you want to perform: "))

# x_coord = [10,50,50,10]
# y_coord = [50,50,10,10]
# no_of_coord = 4
x_coord = [0,30,30,0]
y_coord = [30,30,0,0]
no_of_coord = 4

print("Original X Coordinate: {}".format(x_coord))
print("Original Y Coordinate: {}".format(y_coord))

graph_old = []
def draw_original_polygon(original_x_coordinate, original_y_coordinate):
    for i in range(no_of_coord):
        temp_x_old, temp_y_old = convert_to_graph_coordinate(original_x_coordinate, original_y_coordinate, no_of_coord)
        temp_graph_old = [temp_x_old[i], temp_y_old[i]]
        graph_old.append(temp_graph_old)
    pygame.gfxdraw.line(screen_surface, 350,0,350,700, BLACK)
    pygame.gfxdraw.line(screen_surface, 0,350,700,350, BLACK)
    pygame.gfxdraw.polygon(screen_surface, graph_old, RED)


graph_new = []
def draw_new_polygon(new_x_coordinate, new_y_coordinate):
    for i in range(no_of_coord):
        temp_x_new, temp_y_new = convert_to_graph_coordinate(new_x_coordinate, new_y_coordinate,no_of_coord)
        temp_graph_new = [temp_x_new[i], temp_y_new[i]]
        graph_new.append(temp_graph_new)
    pygame.gfxdraw.polygon(screen_surface, graph_new, BLUE)

def rotation_r(list_of_homogeneous_coordinate, theta):
    rotated_x_coordinate = []
    rotated_y_coordinate = []
    new_rotated_coordinate = []
    radian = ((2 * np.pi) / 360) * theta
    # if theta > 0:
    r = [np.cos(radian), -np.sin(radian), 0,
         np.sin(radian), np.cos(radian), 0,
         0, 0, 1]
    r = np.asarray(r).reshape(3, 3)
    for i in range(len(list_of_homogeneous_coordinate)):
        new_rotated_coordinate.append(np.dot(r, list_of_homogeneous_coordinate[i]))
        rotated_x_coordinate.append(new_rotated_coordinate[i][0][0])
        rotated_y_coordinate.append(new_rotated_coordinate[i][1][0])
    print("Rotated X Coordinate: {}".format(rotated_x_coordinate))
    print("Rotated Y Coordinate: {}".format(rotated_y_coordinate))
    return rotated_x_coordinate, rotated_y_coordinate


if transformation == 1:
    print("Performing Translation!")
    original_homogeneous_coordinate = convert_to_homogeneous_coordinate(x_coord, y_coord, no_of_coord)
    rotated_original_x_coordinates, rotated_original_y_coordinates = rotation(original_homogeneous_coordinate)
    translated_homogeneous_coordinates = translation(original_homogeneous_coordinate, no_of_coord)
    new_x_coordinates, new_y_coordinates = rotation(translated_homogeneous_coordinates)
elif transformation == 2:
    print("Performing Scaling")
    original_homogeneous_coordinate  = convert_to_homogeneous_coordinate(x_coord, y_coord, no_of_coord)
    rotated_original_x_coordinates, rotated_original_y_coordinates = rotation(original_homogeneous_coordinate)
    scaled_homogeneous_coordinates = scaling(original_homogeneous_coordinate, no_of_coord)
    new_x_coordinates, new_y_coordinates = rotation(scaled_homogeneous_coordinates)
elif transformation == 3:
    print("Performing Rotation!")
    original_homogeneous_coordinate = convert_to_homogeneous_coordinate(x_coord, y_coord, no_of_coord)
    rotated_x_coordinates, rotated_y_coordinates = rotation_r(original_homogeneous_coordinate, -90)
    rotated_original_x_coordinates, rotated_original_y_coordinates = x_coord, y_coord
    new_x_coordinates, new_y_coordinates = rotated_x_coordinates, rotated_y_coordinates

elif transformation == 4:
    print("Performing Reflection!")
    original_homogeneous_coordinate = convert_to_homogeneous_coordinate(x_coord, y_coord, no_of_coord)
    rotated_original_x_coordinates, rotated_original_y_coordinates = rotation(original_homogeneous_coordinate)
    reflected_homogeneous_coordinates = reflection(original_homogeneous_coordinate, 0, no_of_coord)
    new_x_coordinates, new_y_coordinates = rotation(reflected_homogeneous_coordinates)
elif transformation == 5:
    print("Performing Shearing!")
    original_homogeneous_coordinate = convert_to_homogeneous_coordinate(x_coord, y_coord, no_of_coord)
    rotated_original_x_coordinates, rotated_original_y_coordinates = rotation(original_homogeneous_coordinate)
    sheared_homogeneous_coordinates = shearing(original_homogeneous_coordinate, 1, no_of_coord)
    new_x_coordinates, new_y_coordinates = rotation(sheared_homogeneous_coordinates)

draw_original_polygon(rotated_original_x_coordinates, rotated_original_y_coordinates)

draw_new_polygon(new_x_coordinates, new_y_coordinates)



#------------------------------------------------------------------------#

pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()