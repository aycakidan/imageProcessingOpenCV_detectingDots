import cv2
import numpy as np
import math

# Görüntüyü yükleyin
img = cv2.imread('testImg.jpg')

# Görüntüyü siyah-beyaz yapın
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Hough dönüşümü ile daireleri tespit edin
circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, dp=1, minDist=105, param1=50, param2=30, minRadius=5, maxRadius=50)

# Daireler bulundu mu?
if circles is not None:
    # Dairelerin koordinatları ve yarıçapları corner adlı bir diziye atanır.
    corner = np.uint16(np.around(circles[0, :]))

    # İlk üç çemberin merkezlerini ve birbirlerine olan mesafelerini hesaplamak için döngü
    for i in range(3):
        x1, y1 = corner[i][0], corner[i][1]
        cv2.circle(img, (x1, y1), 2, (0, 0, 255), 3)  # Merkezleri kırmızı işaretle
        for j in range(i + 1, 3):
            x2, y2 = corner[j][0], corner[j][1]
            cv2.circle(img, (x2, y2), 2, (0, 0, 255), 3)  # Merkezleri kırmızı işaretle
            # İki merkez arasındaki mesafeyi hesaplayın
            distance = np.linalg.norm(np.array([x1, y1]) - np.array([x2, y2]))
            # Merkezler arasındaki mesafeyi yazdırın
            print(f"Çember {i + 1} - Çember {j + 1} Uzaklık: {distance:.2f}")
            cv2.putText(img, f'{distance:.2f}', (int((x1 + x2) / 2), int((y1 + y2) / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 255), 2)
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imshow('corner', img)
    cv2.waitKey(0)
else:
    print("There is no circle is found.")
