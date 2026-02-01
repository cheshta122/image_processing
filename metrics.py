# Import NumPy library
# Used for numerical operations and array manipulation
import numpy as np

# Import image quality metric functions from scikit-image
# PSNR measures noise reduction quality
# SSIM measures structural similarity between images
from skimage.metrics import peak_signal_noise_ratio, structural_similarity


# Function to compute Peak Signal-to-Noise Ratio (PSNR)
# Higher PSNR value indicates better image quality
def compute_psnr(original, denoised):

    # Resize/crop the original image to match denoised image dimensions
    # This avoids dimension mismatch errors during comparison
    original = original[:denoised.shape[0], :denoised.shape[1]]

    # Calculate and return the PSNR value
    return peak_signal_noise_ratio(original, denoised)


# Function to compute Structural Similarity Index (SSIM)
# SSIM measures perceptual similarity (structure, contrast, luminance)
def compute_ssim(original, denoised):

    # Resize/crop the original image to match denoised image dimensions
    # Ensures both images have identical dimensions
    original = original[:denoised.shape[0], :denoised.shape[1]]

    # Calculate and return the SSIM value
    # data_range specifies the range of pixel values in the image
    return structural_similarity(
        original,
        denoised,
        data_range=denoised.max() - denoised.min()
    )
