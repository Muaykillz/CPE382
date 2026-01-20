import cv2
import numpy as np

img1 = cv2.imread('input/image1.jpg')
img2 = cv2.imread('input/image2.jpg')

if img1.shape != img2.shape:
    img2 = cv2.resize(img2, (img1.shape[1], img1.shape[0]))

# Image addition
blended = cv2.addWeighted(img1, 0.5, img2, 0.5, 0)
cv2.imwrite('output/part3_addition.jpg', blended)

# Image subtraction
subtraction = cv2.absdiff(img1, img2)
cv2.imwrite('output/part3_subtraction.jpg', subtraction)

# Create binary mask (circular mask in center)
mask = np.zeros(img1.shape[:2], dtype=np.uint8)
center = (img1.shape[1] // 2, img1.shape[0] // 2)
radius = min(center[0], center[1]) // 2
cv2.circle(mask, center, radius, 255, -1)

# Apply mask to image
masked = cv2.bitwise_and(img1, img1, mask=mask)
cv2.imwrite('output/part3_masking.jpg', masked)
cv2.imwrite('output/part3_mask.jpg', mask)