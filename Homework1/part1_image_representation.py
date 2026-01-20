import cv2
import numpy as np

img = cv2.imread('input/image1.jpg')

# RGB image
cv2.imwrite('output/part1_rgb.jpg', img)

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imwrite('output/part1_grayscale.jpg', gray)

# Extract and display 5x5 pixel region from top-left corner
region_rgb = img[0:5, 0:5]
region_gray = gray[0:5, 0:5]

print("5x5 Pixel Region (RGB):")
print("Shape:", region_rgb.shape)
for i in range(5):
    for j in range(5):
        b, g, r = region_rgb[i, j]
        print(f"Pixel({i},{j}): R={r:3d}, G={g:3d}, B={b:3d}")
    print()

print("\n5x5 Pixel Region (Grayscale):")
print("Shape:", region_gray.shape)
print(region_gray)
