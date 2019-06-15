import cv2
def GetTexts(image, cut_mat, gray_mat, rows, cols, size=5, BGR=(0, 68, 255)):
    '''
    put the gray level numbers onto each of the slides
    image: the object from the cv2.imread(path, cv2.IMREAD_COLOR)
    cut_mat: the coordinates matrix of each cutting slide
    gray_mat: the gray-level matrix of each cutting slide
    rows; the rows of the cutting
    cols: the colums of the cutting
    size: the size of the text
    BGR: the blue-green-red number of the text
    '''
    for i in range(rows):
        for j in range(cols):
            list_param = cut_mat[i, j]
            xmin = list_param[0]
            ymin = list_param[1]
            xmax = list_param[2]
            ymax = list_param[3]
            x_average = int((xmin+xmax)/2)
            y_average = int((ymin+ymax)/2)
            #x = int(list_param[2])
            #y = int(list_param[1])
            font = cv2.FONT_HERSHEY_SIMPLEX
            cv2.putText(image, str(gray_mat[i, j]), (x_average, y_average), font, size, BGR, 2)
    return image