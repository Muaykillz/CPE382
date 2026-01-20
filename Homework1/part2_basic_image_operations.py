import cv2
import numpy as np

img = cv2.imread('input/image1.jpg')

# Brightness adjustment
brightness = cv2.add(img, np.full(img.shape, 50, dtype=np.uint8))
cv2.imwrite('output/part2_brightness.jpg', brightness)

# Contrast adjustment
contrast = cv2.convertScaleAbs(img, alpha=1.5, beta=0)
cv2.imwrite('output/part2_contrast.jpg', contrast)

# Negative transformation
negative = cv2.bitwise_not(img)
cv2.imwrite('part2_negative.jpg', negative)
