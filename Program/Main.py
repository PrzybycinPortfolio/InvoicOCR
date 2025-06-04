import Image

test = Image.Image('./original_images/test_colorful.png')
test_level = 3
test.gaussian_blur(test_level)
test.convert_to_gray_scale()
test.show_image_window()





