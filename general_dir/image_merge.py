import cv2
from itertools import groupby
import glob


def combine_images(images_path):
    '''
    Combine set of images preserving resolution

    parameter:
    images_path: string
    '''

    image_list = [filename for filename in glob.iglob(images_path + "**/*.png")]
    four_level_list = [list(i) for j, i in groupby(image_list, lambda a: a[:a.rindex("-")])]
    final_image = cv2.hconcat(
        [cv2.vconcat(list(map(lambda image: cv2.imread(image), image_list))) for image_list in four_level_list])

    cv2.imwrite("combined_image.png", final_image)

#Usage
if __name__ == "main":
    images_path = r"C:\Users\Praneeth\Downloads\output\output\16_images" #paste the path here
    combine_images(images_path)




