import pywt
import numpy as np
import copy
import matplotlib.pyplot as plt
import pandas as pd
def sgn(x):
    if x>0:
        return 1
    elif x<0:
        return -1
    else:
        return 0

def wt(index_list, wavefunc = 'db4', lv = 4, m=1,n=4, plot = True):

    #Denoising
    #soft Threshold Processing Method
    coeff = pywt.wavedec(index_list, wavefunc, mode='sym',level=lv)  # Decomposing by levels，cD is the details coefficient

    # Denoising
    # Soft Threshold Processing Method
    for i in range(m,n + 1):  # Select m~n Levels of the wavelet coefficients，and no need to dispose the cA coefficients(approximation coefficients)
        Tr = np.sqrt(2 * np.log2(len(coeff[i])))  # Compute Threshold using Stein's Unbiased Risk Estimate (SURE)
        for j in range(len(coeff[i])): #denoise using soft-thresholding
            if (coeff[i][j] > Tr) :
                coeff[i][j] -= Tr
                #coeff[i][j] = sgn(coeff[i][j]) * (abs(coeff[i][j]) - Tr)  # Shrink to zero
            elif (coeff[i][j] < -Tr) :
                coeff[i][j] += Tr
            else:
                coeff[i][j] = 0  # Set to zero if smaller than threshold

    # Reconstructing
    c = pywt.waverec(coeff, wavefunc)
    if len(c) > len(index_list):
        c = c[:-1]

    if plot:
        data = pd.DataFrame({'CLOSE': index_list, 'denoised': c})
        data.plot(figsize=(10, 10), subplots=(2, 1))
        data.plot(figsize=(10, 5))
        plt.show()
    return c