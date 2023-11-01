import cv2
import numpy as np
import argparse

# Argümanları tanımla
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="Görüntü dosyasının yolu")
args = vars(ap.parse_args())

# Görüntüyü yükle
image = cv2.imread(args["image"])
output = image.copy()
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# İçi dolu siyah daireleri tespit et (ilk kod)
block_size = 30
detected_circles = []

for y in range(0, gray.shape[0], block_size):
    for x in range(0, gray.shape[1], block_size):
        block = gray[y:y+block_size, x:x+block_size]
        num_black_pixels = np.sum(block < 128)

        if num_black_pixels > 0.7 * block.size:
            detected_circles.append((x + block_size // 2, y + block_size // 2, block_size // 2))

# İçi dolu daireleri temizleme
for circle in detected_circles:
    center = (circle[0], circle[1])
    radius = circle[2]
    cv2.circle(output, center, radius-2, (255, 255, 255), -1)

# Hough dönüşümünü kullanarak daireleri tespit et (ikinci kod)
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1.2, 100)

if circles is not None:
    circles = np.round(circles[0, :]).astype("int")
    for (x, y, r) in circles:
        if r < 5:
            continue
        cv2.circle(output, (x, y), r, (0, 255, 0), 4)

# Görüntüyü göster
cv2.imshow("Çıktı", output)
cv2.waitKey(0)
cv2.destroyAllWindows()
