# correction-error
### README: Image Noise Reduction Using Bilateral Filtering

---

####  Overview 
This script demonstrates:
1. Adding Gaussian noise to an image based on a specified  Signal-to-Noise Ratio (SNR) .
2. Removing the noise using  bilateral filtering , which preserves edges while smoothing noisy regions.
3. Visualizing the results with the original image, noisy image, and corrected image displayed side-by-side.

---

####  Features 
-  Add Gaussian Noise :
  - Simulate a noisy image by adding Gaussian noise with a configurable SNR.
-  Bilateral Filtering :
  - Smooth the noisy image while preserving edge details.
-  Visualization :
  - Display the original, noisy, and corrected images in a clear layout using Matplotlib.

---

####  Dependencies 
The script requires the following Python libraries:
1.  NumPy : For numerical operations.
   ```bash
   pip install numpy
   ```
2.  Pillow (PIL) : For image handling.
   ```bash
   pip install pillow
   ```
3.  Matplotlib : For plotting and visualization.
   ```bash
   pip install matplotlib
   ```
4.  SciPy : For Gaussian noise generation (optional but used in the example).
   ```bash
   pip install scipy
   ```
5.  OpenCV : For applying the bilateral filter.
   ```bash
   pip install opencv-python
   ```

---

####  How It Works 

1.  Add Gaussian Noise :
   - The function `add_awgn(image, snr)` introduces noise to an input image.
   - Noise intensity is controlled using the  Signal-to-Noise Ratio (SNR)  parameter:
     ```python
     noisy_image = add_awgn(original_image, snr=20)
     ```

2.  Bilateral Filtering :
   - The `bilateral_correction(image, d, sigma_color, sigma_space)` function smooths the noisy image.
   - It preserves the edges while reducing noise in homogeneous regions:
     ```python
     corrected_image = bilateral_correction(noisy_image, d=9, sigma_color=75, sigma_space=75)
     ```

3.  Visualization :
   - The script plots the original, noisy, and corrected images side-by-side for comparison.

---

####  Usage 

1.  Set the Image Path :
   - Replace the `image_path` variable with the path to your image file:
     ```python
     image_path = r"C:\Users\test\image_1.jpg"
     ```

2.  Run the Script :
   - Execute the script using Python:
     ```bash
     python script_name.py
     ```

3.  View Results :
   - The script will display a figure containing:
     - The  original image .
     - The  noisy image  (after adding Gaussian noise).
     - The  corrected image  (after bilateral filtering).

---

####  Code Structure 

1.  Import Libraries :
   - Required libraries are imported at the beginning of the script.

2.  Add Gaussian Noise :
   - The `add_awgn` function normalizes the input image, adds Gaussian noise, and rescales it to the original range.

3.  Apply Bilateral Filter :
   - The `bilateral_correction` function smooths the noisy image while preserving edges.

4.  Visualization :
   - Matplotlib is used to display the original, noisy, and corrected images side-by-side.

---

####  Customization 

1.  Adjust Noise Level :
   - Modify the `snr` parameter in the `add_awgn` function to change the noise intensity:
     ```python
     noisy_image = add_awgn(original_image, snr=15)
     ```

2.  Tune Bilateral Filter :
   - The `d`, `sigma_color`, and `sigma_space` parameters in the `bilateral_correction` function can be adjusted to fine-tune the filter:
     ```python
     corrected_image = bilateral_correction(noisy_image, d=15, sigma_color=100, sigma_space=100)
     ```

3.  Image Input :
   - Replace the `image_path` variable with a different image to test.

---

####  Output 
After running the script, you will see a comparison of three images:
1.  Original Image : The input image without noise.
2.  Noisy Image : The image after adding Gaussian noise.
3.  Corrected Image : The noisy image corrected using bilateral filtering.

---

####  Benefits of Bilateral Filtering 
-  Edge Preservation : Unlike Gaussian or median filtering, bilateral filtering maintains edge sharpness while reducing noise.
-  Adjustable Parameters : Fine-tune the filter to balance noise reduction and edge preservation.
