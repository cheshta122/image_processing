import cv2
import numpy as np
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

from wavelet_denoise import wavelet_denoise
from enhancement import histogram_equalization, clahe_enhancement, gamma_correction, unsharp_mask
from metrics import compute_psnr, compute_ssim


# ==============================
#   SELECT IMAGE USING BROWSE
# ==============================
Tk().withdraw()
image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")]
)

if not image_path:
    print("No image selected!")
    exit()

# ==============================
#   LOAD IMAGE
# ==============================
image = cv2.imread(image_path, 0)
if image is None:
    print("Failed to load image!")
    exit()

# Use the noisy uploaded image
noisy = image.copy()


# ==============================
#   WAVELET + NLM DENOISING
# ==============================
denoised_wavelet = wavelet_denoise(noisy)

denoised_final = cv2.fastNlMeansDenoising(
    denoised_wavelet,
    None,
    h=20,
    templateWindowSize=7,
    searchWindowSize=21
)

# SHAPE FIX
denoised_final = denoised_final[:image.shape[0], :image.shape[1]]


# ==============================
#   ENHANCEMENT METHODS
# ==============================
he = histogram_equalization(denoised_final)
clahe = clahe_enhancement(denoised_final)
gamma = gamma_correction(denoised_final, gamma=1.2)
sharp = unsharp_mask(denoised_final)

# SHAPE FIX FOR ALL
he     = he[:image.shape[0], :image.shape[1]]
clahe  = clahe[:image.shape[0], :image.shape[1]]
gamma  = gamma[:image.shape[0], :image.shape[1]]
sharp  = sharp[:image.shape[0], :image.shape[1]]


# ==============================
#        METRICS SECTION
# ==============================
print("\n======================================")
print("         IMAGE QUALITY METRICS")
print("======================================")

# MAIN DENOISING METRICS
print("\n--- MAIN DENOISING RESULT ---")
print("PSNR (Original → Denoised) :", compute_psnr(image, denoised_final))
print("SSIM (Original → Denoised) :", compute_ssim(image, denoised_final))

# ENHANCEMENT METRICS
print("\n--- ENHANCEMENT RESULTS ---")
print("HE     :", compute_psnr(denoised_final, he),    compute_ssim(denoised_final, he))
print("CLAHE  :", compute_psnr(denoised_final, clahe), compute_ssim(denoised_final, clahe))
print("Gamma  :", compute_psnr(denoised_final, gamma), compute_ssim(denoised_final, gamma))
print("Sharpen:", compute_psnr(denoised_final, sharp), compute_ssim(denoised_final, sharp))

print("======================================\n")


# ==============================
#    DISPLAY ALL IMAGES
# ==============================
titles = [
    "Original",
    "Noisy",
    "Final Denoised",
    "Histogram Equalized",
    "CLAHE",
    "Gamma Corrected",
    "Sharpened"
]

images = [image, noisy, denoised_final, he, clahe, gamma, sharp]

plt.figure(figsize=(12, 10))

for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

plt.tight_layout()
plt.show()
