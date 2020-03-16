import numpy as np
import pygame, sys
from pygame.locals import *
from pygame import gfxdraw
from functions3 import convert_to_homogeneous_coordinate, translation,  scaling, rotation

from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt



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



x_coord = [0,30,30,0]
y_coord = [30,30,0,0]
z_coord = [10,20,0,0]
# x_coord = [1]
# y_coord = [2]
# z_coord = [3]
no_of_coord = 4

print("""
1. TRANSLATION
2. SCALING
3. ROTATION""")

transformation = int(input("Enter the transformation you want to perform: "))


print("Original x-coordinate: {}".format(x_coord))
print("Original y-coordinate: {}".format(y_coord))
print("Original z-coordinate: {}".format(z_coord))


original_homogeneous_coordinate  = convert_to_homogeneous_coordinate(x_coord, y_coord,z_coord, no_of_coord)


if transformation == 1:
    print("Performing Translation!")
    translation_homogeneous_coordinates = translation(original_homogeneous_coordinate,no_of_coord)
elif transformation == 2:
    print("Performing Scaling")
    scaled_homogeneous_coordinates = scaling(original_homogeneous_coordinate,no_of_coord)
elif transformation == 3:
    print("Performing Rotation!")
    rotated_homogeneous_coordinates = rotation(original_homogeneous_coordinate, no_of_coord)






pygame.display.flip()

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()