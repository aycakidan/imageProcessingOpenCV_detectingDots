import cv2
import numpy as np

# Görüntüyü yükle
image = cv2.imread('testImg.jpg', cv2.IMREAD_GRAYSCALE)

# Bölme boyutunu ayarla
block_size = 30

# İçi dolu siyah daireleri tespit et
detected_circles = []

for y in range(0, image.shape[0], block_size):
    for x in range(0, image.shape[1], block_size):
        block = image[y:y+block_size, x:x+block_size]
        num_black_pixels = np.sum(block < 128)
        
        # Belirli bir eşik değeri ile kontrol et
        if num_black_pixels > 0.7 * block.size:
            detected_circles.append((x + block_size // 2, y + block_size // 2, block_size // 2))

# Daireleri çizme (sadece pembe sınırlayıcı çizgi)
output_image = cv2.cvtColor(image, cv2.COLOR_GRAY2BGR)  # Renkli görüntüye dönüştür

for circle in detected_circles:
    center = (circle[0], circle[1])
    radius = circle[2]
    
    # Pembe sınırlayıcı çizgiyi çiz
    cv2.circle(output_image, center, radius, (255, 0, 255), 2)

# Sonucu göster
cv2.imshow('Daireleri Tespit Et', output_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
