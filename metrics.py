import numpy as np
from skimage.metrics import peak_signal_noise_ratio, structural_similarity

def compute_psnr(original, denoised):
    original = original[:denoised.shape[0], :denoised.shape[1]]
    return peak_signal_noise_ratio(original, denoised)

    
def compute_ssim(original, denoised):
    original = original[:denoised.shape[0], :denoised.shape[1]]
    return structural_similarity(
        original, 
        denoised,
        data_range=denoised.max() - denoised.min()
    )
