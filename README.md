Image Processing Project (Python)
 Overview

This project is a Python-based Image Processing system that focuses on image enhancement, denoising, and quality evaluation.
It applies wavelet-based denoising techniques, enhancement methods, and calculates image quality metrics to analyze performance.

The project is modular, cleanly structured, and suitable for academic submissions, internships, and portfolio showcase.

Objectives

Improve image quality using enhancement techniques

Remove noise from images using Wavelet Transform

Evaluate results using standard image quality metrics

Maintain a clean and modular Python codebase

 Project Structure
image_processing/
│
├── images/                 # Input and output images
│
├── enhancement.py          # Image enhancement techniques
├── wavelet_denoise.py      # Wavelet-based image denoising
├── metrics.py              # Image quality evaluation metrics
├── main.py                 # Main execution file
│
├── __pycache__/            # Python cache files (auto-generated)
└── README.md               # Project documentation
 Module-wise Explanation
🔹 main.py

Entry point of the project

Loads input image

Calls denoising and enhancement functions

Computes evaluation metrics

Displays or saves output images

Acts as the controller that connects all modules.

🔹 enhancement.py

Image Enhancement Module

Implements techniques such as:

Contrast enhancement

Brightness adjustment

Histogram-based improvements

 Used to improve visual clarity and sharpness of images.

🔹 wavelet_denoise.py

Wavelet-based Image Denoising

Uses Discrete Wavelet Transform (DWT)

Removes noise while preserving edges

Reconstructs clean image after thresholding

 Highly effective for reducing Gaussian and high-frequency noise.

🔹 metrics.py

Image Quality Evaluation

Calculates standard metrics like:

PSNR (Peak Signal-to-Noise Ratio)

MSE (Mean Squared Error)

SSIM (if implemented)

 Helps in quantitative comparison of original vs processed images.

🔹 images/

Stores input images

Saves processed output images

Helps in testing different samples

Technologies Used

Python 3

OpenCV

NumPy

PyWavelets

Matplotlib

 How to Run the Project
1️⃣ Clone the Repository
git clone https://github.com/cheshta122/image_processing.git
cd image_processing
2️⃣ Install Dependencies
pip install numpy opencv-python pywavelets matplotlib
3️⃣ Run the Project
python main.py
Output

Denoised image

Enhanced image

Quality metrics (PSNR, MSE, etc.)

Visual comparison between original and processed images

Applications

Medical image preprocessing

Satellite and aerial image analysis

Low-light image improvement

Academic research and learning

Key Highlights

✔ Modular and readable code
✔ Wavelet-based denoising
✔ Real-world image processing techniques
✔ Beginner + intermediate friendly


Future Improvements

Add GUI using Tkinter or Streamlit

Support for real-time image processing

Extend metrics (SSIM, RMSE)

Add batch image processing
