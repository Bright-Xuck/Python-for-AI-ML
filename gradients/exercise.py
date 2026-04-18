import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
from scipy.ndimage import gaussian_filter 
# --------------------------- 
# 1. Load image (grayscale) 
# --------------------------- 
image = cv2.imread('SAVE_20260414_114714.jpg', cv2.IMREAD_GRAYSCALE) 
# Normalize to [0,1] 
image = image / 255.0 
# --------------------------- 
# 2. Add Poisson Noise 
# --------------------------- 
noisy = np.random.poisson(image * 255) / 255.0 
# --------------------------- 
# 3. Anscombe Transform 
# --------------------------- 
def anscombe_transform(img): 
 return 2 * np.sqrt(img + 3/8) 
transformed = anscombe_transform(noisy) 
# --------------------------- 
# 4. Gaussian Denoising 
# --------------------------- 
denoised = gaussian_filter(transformed, sigma=1) 
# --------------------------- 
# 5. Inverse Anscombe Transform (approx) 
# --------------------------- 
def inverse_anscombe(img): 
 return (img / 2)**2 - 3/8 
final = inverse_anscombe(denoised) 
# Clip values 
final = np.clip(final, 0, 1) 
# --------------------------- 
# 6. Display Results 
# --------------------------- 
plt.figure(figsize=(10,5)) 
plt.subplot(1,3,1) 
plt.title("Original") 
plt.imshow(image, cmap='gray') 
plt.axis('off') 
plt.subplot(1,3,2) 
plt.title("Poisson Noise") 
plt.imshow(noisy, cmap='gray') 
plt.axis('off') 
plt.subplot(1,3,3) 
plt.title("Denoised") 
plt.imshow(final, cmap='gray') 
plt.axis('off') 
plt.show()