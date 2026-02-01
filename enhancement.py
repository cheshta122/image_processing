# Import the OpenCV library
# Used for image processing operations like contrast enhancement, denoising, blurring, and sharpening
import cv2

# Import the NumPy library
# Used for numerical computations and creating lookup tables
import numpy as np


# Function to perform Histogram Equalization
# Improves the overall contrast of a grayscale image
def histogram_equalization(image):

    # Apply OpenCV's built-in histogram equalization function
    # Redistributes pixel intensity values to enhance contrast
    return cv2.equalizeHist(image)


# Function to apply CLAHE (Contrast Limited Adaptive Histogram Equalization)
# Enhances local contrast while preventing over-amplification of noise
def clahe_enhancement(image):

    # Create a CLAHE object
    # clipLimit controls the maximum contrast
    # tileGridSize defines the number of regions the image is divided into
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))

    # Apply the CLAHE algorithm to the image
    return clahe.apply(image)


# Function to perform Gamma Correction
# Adjusts the brightness of the image
def gamma_correction(image, gamma=1.2):

    # Calculate the inverse of gamma
    # Used in the gamma correction formula
    invGamma = 1.0 / gamma

    # Create a Lookup Table (LUT)
    # Computes corrected pixel values for all intensity levels (0–255)
    table = np.array(
        [
            (i / 255.0) ** invGamma * 255  # Gamma correction formula
            for i in range(256)            # Iterate over all possible pixel values
        ]
    ).astype("uint8")                      # Convert values to unsigned 8-bit integers

    # Apply the lookup table to the image
    return cv2.LUT(image, table)


# Function to perform Unsharp Masking
# Sharpens the image by enhancing edges
def unsharp_mask(image):

    # Apply Gaussian Blur to create a smoothed version of the image
    # (9,9) is the kernel size and 10 is the standard deviation
    gaussian = cv2.GaussianBlur(image, (9, 9), 10)

    # Combine the original image and the blurred image
    # Increases edge contrast by subtracting the blurred version
    sharp = cv2.addWeighted(image, 1.5, gaussian, -0.5, 0)

    # Return the sharpened image
    return sharp


# Function to remove noise from the image
# Uses the Non-Local Means Denoising algorithm
def denoise(image):

    # Apply Fast Non-Local Means Denoising
    # h controls the strength of noise removal
    # templateWindowSize defines the size of the comparison window
    # searchWindowSize defines the size of the search area
    denoised = cv2.fastNlMeansDenoising(
        image,
        None,
        h=7,
        templateWindowSize=7,
        searchWindowSize=21
    )

    # Return the denoised image
    return denoised


# Complete image enhancement pipeline
# Applies all enhancement steps sequentially
def enhance_image(image):

    # Step 1: Remove noise from the image
    image = denoise(image)

    # Step 2: Enhance local contrast using CLAHE
    image = clahe_enhancement(image)

    # Step 3: Adjust brightness using gamma correction
    image = gamma_correction(image, 1.1)

    # Step 4: Sharpen the image using unsharp masking
    image = unsharp_mask(image)

    # Return the final enhanced image
    return image
