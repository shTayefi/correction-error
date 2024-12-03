import numpy as np
from PIL import Image  # Import Image from Pillow
import matplotlib.pyplot as plt
from scipy.ndimage import gaussian_filter
from cv2 import bilateralFilter

def add_awgn(image, snr):
    """
    Add Gaussian noise to an image based on a given SNR (Signal-to-Noise Ratio)
    """
    image = image / 255.0  # Normalize image to [0, 1]
    noise = np.random.normal(0, 10**(-snr / 20), image.shape)  # Generate Gaussian noise
    noisy_image = image + noise
    noisy_image = np.clip(noisy_image, 0, 1)  # Clip values to valid range
    return (noisy_image * 255).astype(np.uint8)  # Rescale back to [0, 255]

def bilateral_correction(image, d=9, sigma_color=75, sigma_space=75):
    """
    Apply Bilateral filter for noise correction while preserving edges
    """
    corrected_image = bilateralFilter(image, d=d, sigmaColor=sigma_color, sigmaSpace=sigma_space)
    return corrected_image

# Load the original image
image_path = r"C:\Users\test\image_1.jpg"
original_image = np.array(Image.open(image_path))

# Generate the noisy image
noisy_image = add_awgn(original_image, snr=20)

# Apply Bilateral correction
corrected_image = bilateral_correction(noisy_image)

# Plot the original, noisy, and corrected images
plt.figure(figsize=(15, 5))

# Original Image
plt.subplot(1, 3, 1)
plt.imshow(original_image)
plt.title("Original Image")
plt.axis('off')

# Noisy Image
plt.subplot(1, 3, 2)
plt.imshow(noisy_image)
plt.title("Noisy Image")
plt.axis('off')

# Corrected Image
plt.subplot(1, 3, 3)
plt.imshow(corrected_image)
plt.title("Corrected Image (Bilateral Filter)")
plt.axis('off')

# Show the comparison
plt.tight_layout()
plt.show()
