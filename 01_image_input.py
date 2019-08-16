# skeleton for an image processing pipeline
import cv2
import sys

path_to_image = sys.argv[1]

img_array = cv2.imread(path_to_image)


def function_to_do_something(img):
    print('Doing something with image ...')


function_to_do_something(img_array)
