import cv2
import numpy as np

def histogram_equalization(image):
    return cv2.equalizeHist(image)

def clahe_enhancement(image):
    clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
    return clahe.apply(image)

def gamma_correction(image, gamma=1.2):
    invGamma = 1.0 / gamma
    table = np.array([(i/255.0)**invGamma * 255 for i in range(256)]).astype("uint8")
    return cv2.LUT(image, table)

def unsharp_mask(image):
    gaussian = cv2.GaussianBlur(image, (9, 9), 10)
    sharp = cv2.addWeighted(image, 1.5, gaussian, -0.5, 0)
    return sharp

def denoise(image):
    raise NotImplementedError

def enhance_image(image):
    image = denoise(image)
    image = clahe_enhancement(image)
    image = gamma_correction(image, 1.1)
    image = unsharp_mask(image)
    return image
