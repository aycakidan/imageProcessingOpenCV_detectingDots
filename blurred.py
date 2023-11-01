import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('testImg.jpg', cv2.IMREAD_COLOR)

# Görüntüyü gri tona dönüştür
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Görüntü üzerinde Gaussian bulanıklık uygula
blurred = cv2.GaussianBlur(gray, (15, 15), 0)

# Canny kenar dedektörü uygula
edges = cv2.Canny(blurred, 30, 150)

# Kenar görüntüsü üzerinde kontur tespiti yap
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Daireden farklı olan konturları filtrele
circles = []

for contour in contours:
    perimeter = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * perimeter, True)

    if len(approx) >= 8:
        circles.append(contour)

# Daireleri çizme
for circle in circles:
    (x, y), radius = cv2.minEnclosingCircle(circle)
    center = (int(x), int(y))
    radius = int(radius)
    cv2.circle(image, center, radius, (0, 255, 0), 2)

# Sonucu göster
cv2.imshow('Daireleri Tespit Et', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
