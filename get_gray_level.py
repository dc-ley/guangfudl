from cut_pic import grid_cut
#from cut_pic import get_cut_line
import numpy as np
from match_gray_scale import MatchGrayScale

def GetGrayLevel(img, rows, cols):
    '''
    得到每一段图片对应的每块电池片的灰度等级
    Input:
    img: 待检测的图片段（已被转化成cv2格式）
    rows: 切割图片的行数
    cols: 切割图片的列数
    Output:
    gray_mat: 每块电池片对应的灰度等级构成的矩阵（维数：rows*cols）
    cut_mat: 每块电池片对应的切割坐标（xmin, ymin, xmax, ymax）
    '''
    
    #cut_points = get_cut_line(img, rows, cols, True)
    _, (rowline, coline) = grid_cut(img, rows, cols, True)
    
    ## 获得每块电池片的切图坐标
    #cut_mat = np.zeros((rows*cols, 4), dtype=int)
    #l = 0
    #for i in range(rows):
    #    for j in range(cols):
    #        tmp = [cut_points[0][j], cut_points[1][i], cut_points[0][j+1], cut_points[1][i+1]]
    #        cut_mat[l,:] = tmp
    #        l += 1
    #cut_mat = cut_mat.reshape([rows, cols, 4])
    
    cut_mat = np.zeros((rows*cols, 4), dtype=int)
    l = 0
    for i in range(rows):
        for j in range(cols):
            tmp = [coline[j], rowline[i], coline[j+1], rowline[i+1]]
            cut_mat[l,:] = tmp
            l += 1
    cut_mat = cut_mat.reshape([rows, cols, 4])
    
    ## 计算每块电池片的像素中位数
    med = np.zeros((rows,cols), dtype=int)
    #mod = np.zeros((rows,cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            tmp = img[cut_mat[i, j][1]:cut_mat[i, j][3], cut_mat[i, j][0]:cut_mat[i, j][2]]
            med[i, j] = np.median(tmp)
            #mod[i ,j] = stats.mode(tmp)[0][0]
            
    ## 得到每块电池片对应的灰度等级
    gray_mat = np.zeros((rows, cols), dtype=int)
    for i in range(rows):
        for j in range(cols):
            gray_mat[i, j] = MatchGrayScale(med[i, j])
            
    return gray_mat, cut_mat