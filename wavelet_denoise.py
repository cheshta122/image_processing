import pywt
import numpy as np

def wavelet_denoise(img, wavelet="db8", level=3):
    coeffs = pywt.wavedec2(img, wavelet, level=level)
    cA, cD = coeffs[0], coeffs[1:]

    # Estimate noise sigma using MAD
    sigma = np.median(np.abs(cD[-1][0])) / 0.6745
    uthresh = sigma * np.sqrt(2 * np.log(img.size))

    # Soft thresholding
    new_cD = []
    for (cH, cV, cD_layer) in cD:
        cH = pywt.threshold(cH, value=uthresh, mode="soft")
        cV = pywt.threshold(cV, value=uthresh, mode="soft")
        cD_layer = pywt.threshold(cD_layer, value=uthresh, mode="soft")
        new_cD.append((cH, cV, cD_layer))

    denoised = pywt.waverec2([cA] + new_cD, wavelet)
    denoised = np.clip(denoised, 0, 255)

    return denoised.astype("uint8")
