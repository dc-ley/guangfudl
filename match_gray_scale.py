import numpy as np
gray_scale = np.linspace(255, 0, 20, endpoint=True).round()
gray_scale = np.asarray(gray_scale, dtype=int)
def MatchGrayScale(pixel):
    tmp = np.abs(pixel - gray_scale)
    results = np.where(tmp == np.min(tmp))[0][0]
    return results