import cv2
def GetRectangle(list_param, image, BGR=(0, 255, 0), size=2):
    x_min = list_param[0]
    y_min = list_param[1]
    x_max = list_param[2]
    y_max = list_param[3]
    cv2.rectangle(image, (x_min, y_min), (x_max, y_max), BGR, size)
    return image