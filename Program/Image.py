import cv2


class Image:

    #Protect before suddenly close
    @staticmethod
    def do_not_close():
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def __init__(self,filename):
        self.filename = filename
        self.img = cv2.imread(filename, cv2.IMREAD_COLOR)

    #show colorful input image
    def show_image_window(self):
        cv2.imshow("Image", self.img)
        Image.do_not_close()

    def convert_to_gray_scale(self):
        gray = cv2.cvtColor(self.img, cv2.COLOR_BGR2GRAY)
        self.img = gray

    def gaussian_blur(self,level = 5):
        if((level % 2) == 0):
            level = level + 1
        current_img = cv2.GaussianBlur(self.img, (level, level), 0)
        self.img = current_img













