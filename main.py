# Import OpenCV library
# Used for image loading, denoising, and enhancement operations
import cv2

# Import NumPy library
# Used for numerical operations and array handling
import numpy as np

# Import Matplotlib
# Used for displaying images and visual comparison
import matplotlib.pyplot as plt

# Import Tkinter components
# Used to open a file browser dialog for image selection
from tkinter import Tk, filedialog


# Import custom wavelet denoising function
# This function applies wavelet-based noise reduction
from wavelet_denoise import wavelet_denoise

# Import image enhancement functions
# Includes histogram equalization, CLAHE, gamma correction, and sharpening
from enhancement import histogram_equalization, clahe_enhancement, gamma_correction, unsharp_mask

# Import image quality metric functions
# PSNR and SSIM are used to evaluate image quality
from metrics import compute_psnr, compute_ssim


# ==============================
#   SELECT IMAGE USING FILE BROWSER
# ==============================

# Initialize Tkinter window and hide the root window
Tk().withdraw()

# Open a file dialog to allow the user to select an image
image_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.png *.jpeg *.bmp")]
)

# Check if no image was selected
if not image_path:
    print("No image selected!")
    exit()


# ==============================
#   LOAD IMAGE
# ==============================

# Read the selected image in grayscale mode
image = cv2.imread(image_path, 0)

# Check if image loading failed
if image is None:
    print("Failed to load image!")
    exit()

# Create a copy of the image to represent the noisy input
noisy = image.copy()


# ==============================
#   WAVELET + NLM DENOISING
# ==============================

# Apply wavelet-based denoising to the noisy image
denoised_wavelet = wavelet_denoise(noisy)

# Apply Non-Local Means (NLM) denoising for further noise reduction
denoised_final = cv2.fastNlMeansDenoising(
    denoised_wavelet,
    None,
    h=20,                     # Strength of noise removal
    templateWindowSize=7,     # Size of the template window
    searchWindowSize=21       # Size of the search window
)

# Fix image shape in case of dimension mismatch
denoised_final = denoised_final[:image.shape[0], :image.shape[1]]


# ==============================
#   IMAGE ENHANCEMENT METHODS
# ==============================

# Apply Histogram Equalization
he = histogram_equalization(denoised_final)

# Apply CLAHE enhancement
clahe = clahe_enhancement(denoised_final)

# Apply Gamma Correction
gamma = gamma_correction(denoised_final, gamma=1.2)

# Apply Unsharp Masking for sharpening
sharp = unsharp_mask(denoised_final)

# Ensure all enhanced images have the same shape as the original
he     = he[:image.shape[0], :image.shape[1]]
clahe  = clahe[:image.shape[0], :image.shape[1]]
gamma  = gamma[:image.shape[0], :image.shape[1]]
sharp  = sharp[:image.shape[0], :image.shape[1]]


# ==============================
#        IMAGE QUALITY METRICS
# ==============================

# Print header for metrics output
print("\n======================================")
print("         IMAGE QUALITY METRICS")
print("======================================")

# Display PSNR and SSIM for the denoised image
print("\n--- MAIN DENOISING RESULT ---")
print("PSNR (Original → Denoised) :", compute_psnr(image, denoised_final))
print("SSIM (Original → Denoised) :", compute_ssim(image, denoised_final))

# Display PSNR and SSIM for each enhancement technique
print("\n--- ENHANCEMENT RESULTS ---")
print("HE     :", compute_psnr(denoised_final, he),    compute_ssim(denoised_final, he))
print("CLAHE  :", compute_psnr(denoised_final, clahe), compute_ssim(denoised_final, clahe))
print("Gamma  :", compute_psnr(denoised_final, gamma), compute_ssim(denoised_final, gamma))
print("Sharpen:", compute_psnr(denoised_final, sharp), compute_ssim(denoised_final, sharp))

print("======================================\n")


# ==============================
#    DISPLAY ALL IMAGES
# ==============================

# Titles for each displayed image
titles = [
    "Original",
    "Noisy",
    "Final Denoised",
    "Histogram Equalized",
    "CLAHE",
    "Gamma Corrected",
    "Sharpened"
]

# List of images to be displayed
images = [image, noisy, denoised_final, he, clahe, gamma, sharp]

# Create a figure window
plt.figure(figsize=(12, 10))

# Display each image in a grid layout
for i in range(len(images)):
    plt.subplot(3, 3, i + 1)
    plt.imshow(images[i], cmap="gray")
    plt.title(titles[i])
    plt.axis("off")

# Adjust layout to avoid overlap
plt.tight_layout()

# Show all images
plt.show()
