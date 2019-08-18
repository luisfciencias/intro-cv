# skeleton for an image processing pipeline
import cv2
import matplotlib.pyplot as plt
import sys

path_to_image = sys.argv[1]

img_array = cv2.imread(path_to_image, 0)


def function_to_do_something(img):
    print('Doing something with image ...')
    print(img.shape)
    plt.imshow(img, 'gray')
    plt.show()


function_to_do_something(img_array)
