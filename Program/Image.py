import cv2
import


class Image:

    def __init__(self,filename):
        self.filename = filename
        self.orginal_img = cv2.imread(filename,cv2.IMREAD_COLOR)

    #show colorful input image
    def show_original_image_window(self):
        cv2.imshow("Orginal colorful input image", self.orginal_img)




