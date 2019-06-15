import numpy as np
from collections import OrderedDict


def IsShortCut(gray_mat1, cut_mat1, gray_mat2, cut_mat2, gray_mat3, cut_mat3, threshold=14):
    '''
    将前面得到的三段图片的结果汇总，判断整张图片是否存在短路的电池片
    Input:
    gray_mat1：第1段图片经由GetGrayLevel函数输出的灰度等级矩阵
    cut_mat1：第1段图片经由GetGrayLevel函数输出的切图坐标
    gray_mat2, cut_mat2, gray_mat3, cut_mat3同上
    threshold: 用来判断电池片是否短路，如果某块电池片的灰度等级超过这个阈值（太黑），则认为该电池片短路
    Output:
    qualified: 布尔变量，如果整张图片包含有短路的电池片，则为False，否则为True
    loc: 是一个长度为3的列表，分别包含了3段图片中对应的短路电池片的位置（行，列）
    coord: 是一个长度为3的列表，分别包含了3段图片中对应的短路电池片的切图坐标（xmin, ymin, xmax, ymax）
    '''
    gray_mat = np.concatenate((gray_mat1, gray_mat2, gray_mat3), axis=0)
    ## 判断，灰度等级大于threshold的电池片视作短路，记录其位置
    row_loc = np.where(gray_mat > threshold)[0]
    col_loc = np.where(gray_mat > threshold)[1]
    results = []
    for i in range(len(row_loc)):
        dic = OrderedDict()
        dic['loc'] = (row_loc[i], col_loc[i])
        if row_loc[i] < 2:            
            dic['coord'] = (cut_mat1[row_loc[i], col_loc[i]])
        elif row_loc[i] < 4:
            dic['coord'] = (cut_mat2[row_loc[i] - 2, col_loc[i]] + [0, 1000, 0, 1000])
        else:
            dic['coord'] = (cut_mat3[row_loc[i] - 4, col_loc[i]] + [0, 2000, 0, 2000])
        results.append(dic)   
    return results