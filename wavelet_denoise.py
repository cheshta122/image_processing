# Import PyWavelets library
# Used for performing wavelet decomposition and reconstruction
import pywt

# Import NumPy library
# Used for numerical operations and array handling
import numpy as np


# Function to perform wavelet-based image denoising
# Uses Discrete Wavelet Transform (DWT) and soft thresholding
def wavelet_denoise(img, wavelet="db8", level=3):

    # Perform 2D wavelet decomposition of the image
    # coeffs contains approximation and detail coefficients
    coeffs = pywt.wavedec2(img, wavelet, level=level)

    # Extract approximation coefficients (low-frequency components)
    # cA represents the coarse structure of the image
    cA = coeffs[0]

    # Extract detail coefficients (high-frequency components)
    # These contain noise and edge information
    cD = coeffs[1:]


    # ==============================
    #   NOISE ESTIMATION
    # ==============================

    # Estimate noise standard deviation (sigma)
    # Median Absolute Deviation (MAD) is used for robust estimation
    # cD[-1][0] corresponds to horizontal detail coefficients of the last level
    sigma = np.median(np.abs(cD[-1][0])) / 0.6745

    # Calculate universal threshold value
    # Used to suppress noise in wavelet coefficients
    uthresh = sigma * np.sqrt(2 * np.log(img.size))


    # ==============================
    #   SOFT THRESHOLDING
    # ==============================

    # List to store thresholded detail coefficients
    new_cD = []

    # Iterate through detail coefficients at each decomposition level
    for (cH, cV, cD_layer) in cD:

        # Apply soft thresholding to horizontal detail coefficients
        cH = pywt.threshold(cH, value=uthresh, mode="soft")

        # Apply soft thresholding to vertical detail coefficients
        cV = pywt.threshold(cV, value=uthresh, mode="soft")

        # Apply soft thresholding to diagonal detail coefficients
        cD_layer = pywt.threshold(cD_layer, value=uthresh, mode="soft")

        # Append the thresholded coefficients
        new_cD.append((cH, cV, cD_layer))


    # ==============================
    #   IMAGE RECONSTRUCTION
    # ==============================

    # Reconstruct the image using inverse wavelet transform
    # Combines approximation and thresholded detail coefficients
    denoised = pywt.waverec2([cA] + new_cD, wavelet)

    # Clip pixel values to valid image range (0–255)
    denoised = np.clip(denoised, 0, 255)

    # Convert image to unsigned 8-bit integer format
    return denoised.astype("uint8")
