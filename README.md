Image Denoising and Enhancement System
Overview

This project implements an image denoising and enhancement pipeline using classical image processing techniques. The system focuses on reducing noise, improving contrast, adjusting brightness, sharpening edges, and evaluating image quality using standard metrics.

The application allows users to select an image through a graphical file browser, processes the image using multiple enhancement techniques, computes PSNR and SSIM metrics, and displays visual comparisons of all results.

This project is designed for academic use (IDP / mini project) and demonstrates practical implementation of image processing concepts.

Features

Interactive image selection using a file dialog

Wavelet-based denoising using Discrete Wavelet Transform

Non-Local Means (NLM) denoising for refined noise removal

Multiple enhancement techniques:

Histogram Equalization

CLAHE (Contrast Limited Adaptive Histogram Equalization)

Gamma Correction

Unsharp Masking (Sharpening)

Image quality evaluation using:

PSNR (Peak Signal-to-Noise Ratio)

SSIM (Structural Similarity Index)

Side-by-side visual comparison of original, noisy, denoised, and enhanced images
<img width="744" height="233" alt="{4ACBEE1C-3608-4846-944C-BA04086AFCB3}" src="https://github.com/user-attachments/assets/6fb22422-df3c-42ac-b4ff-8890836a719b" />



Technologies Used

Python

OpenCV

NumPy

PyWavelets

scikit-image

Matplotlib

Tkinter

Methodology
1. Image Input

The user selects an image using a graphical file browser. The image is loaded in grayscale format for consistent processing.

2. Denoising

Wavelet Denoising:

The image is decomposed into frequency components using Discrete Wavelet Transform.

Noise is estimated using Median Absolute Deviation (MAD).

Soft thresholding is applied to suppress noise while preserving edges.

Non-Local Means (NLM) Denoising:

Further refines the image by comparing pixel neighborhoods to remove residual noise.

3. Image Enhancement

After denoising, multiple enhancement techniques are applied:

Histogram Equalization: Improves global contrast.

CLAHE: Enhances local contrast while avoiding over-amplification.

Gamma Correction: Adjusts brightness and intensity distribution.

Unsharp Masking: Sharpens edges and fine details.

4. Quality Evaluation

PSNR evaluates the noise reduction performance quantitatively.

SSIM measures perceptual similarity by comparing structural information.

5. Visualization

All intermediate and final images are displayed using Matplotlib for visual comparison.

Image Quality Metrics
PSNR (Peak Signal-to-Noise Ratio)

Measures the ratio between the maximum possible pixel value and the noise.

Higher PSNR indicates better image quality.

SSIM (Structural Similarity Index)

Measures similarity based on luminance, contrast, and structure.

Values range from -1 to 1, where higher values indicate greater similarity.

How to Run the Project
1. Install Dependencies

Create a virtual environment (recommended) and install required libraries:

pip install opencv-python numpy pywavelets scikit-image matplotlib
2. Run the Application
python main.py
3. Select an Image

A file dialog will appear.

Choose any grayscale or color image (JPG, PNG, BMP).

The system will automatically process and display results.

Input and Output

Input:

Grayscale or color image (automatically converted)

Output:

Denoised image

Enhanced images using different techniques

PSNR and SSIM values

Visual comparison of all results

Applications

Medical image preprocessing

Satellite and remote sensing images

Low-light image enhancement

Academic demonstrations of image processing techniques

Limitations

Designed primarily for grayscale images

Performance may slow down for very high-resolution images

Classical methods used (no deep learning)

Future Enhancements

Support for color image processing

GPU acceleration

Integration of deep learning-based denoising

Real-time image enhancement

Conclusion

This project demonstrates a complete image processing pipeline that combines denoising, enhancement, evaluation, and visualization. It effectively balances noise reduction and detail preservation, making it suitable for academic and experimental applications.

# Image Processing using Wavelet Denoising


## Overview


This repository implements an image processing pipeline focused on
reducing noise and improving image quality using wavelet-based
denoising techniques.


The project is designed to read input images, apply noise reduction,
enhance visual quality, and evaluate the results using standard
image quality metrics.


This repository is also structured to be easily understood by
automated systems such as Retrieval-Augmented Generation (RAG)
based chatbots.


---


## Purpose of the Project


The main objective of this project is to:


- Remove noise from images while preserving important visual details
- Improve the overall clarity and appearance of images
- Evaluate image quality before and after processing


Wavelet-based denoising is used because it allows multi-resolution
analysis, making it effective at separating noise from useful image
information.


---


## How the Project Works


The image processing workflow follows these steps:


1. Input images are loaded from the `images` directory.
2. Noise is reduced using wavelet-based denoising techniques.
3. Image enhancement methods are applied to improve visual quality.
4. Image quality is evaluated using PSNR and SSIM metrics.


Each step of the pipeline is implemented in a separate module for
clarity and modularity.


---


## Repository Structure



image_processing/
│
├── images/ # Input images for processing
├── main.py # Entry point for executing the pipeline
├── wavelet_denoise.py # Wavelet-based noise reduction logic
├── enhancement.py # Image enhancement techniques
├── metrics.py # Image quality evaluation metrics
└── README.md # Project documentation



---


## Description of Key Files


### main.py
Acts as the entry point of the project.  
It connects all modules and executes the complete image processing
pipeline from loading images to evaluating results.


### wavelet_denoise.py
Implements wavelet-based denoising to remove noise from images while
preserving edges and important details.


### enhancement.py
Enhances the visual quality of images after denoising by improving
contrast, brightness, or clarity.


### metrics.py
Evaluates the quality of processed images using objective metrics
such as PSNR (Peak Signal-to-Noise Ratio) and SSIM (Structural
Similarity Index).


---


## Image Quality Evaluation


The project uses the following metrics:


- **PSNR**: Measures the difference between the original and
  processed images. Higher values indicate better quality.
- **SSIM**: Measures structural similarity between images, focusing
  on perceived visual quality.


These metrics help quantify the effectiveness of the denoising and
enhancement steps.


---


## Use Cases


This project can be used for:


- Learning wavelet-based image denoising
- Studying image enhancement techniques
- Comparing image quality before and after processing
- Demonstrating an image processing pipeline for academic or
  practical purposes


---


## Example Questions for RAG-based Chatbots


When this repository is used with a RAG-based chatbot, the following
questions can be answered accurately:


- What does this repository do?
- Explain the image processing pipeline.
- How does wavelet denoising work in this project?
- Why is wavelet denoising used?
- What happens after denoising?
- How is image quality evaluated?
- What metrics are used and why?
- What is the role of main.py?
- Explain the purpose of enhancement.py.


---


## Notes


- The code is fully functional and modular.
- The repository is structured to support automated understanding
  by tools that read and reason over source code and documentation.
