from PIL import Image
import math
W, H = 1024, 768
ITER = 100
LIMIT = 2.0
img = Image.new('RGB', (W, H))

palette = [
    (
        int(255 * math.sin(i / 50.0 + 1.0) ** 2),
        int(255 * math.sin(i / 50.0 + 0.5) ** 2),
        int(255 * math.sin(i / 50.0 + 1.7) ** 2)
    ) for i in range(ITER - 1)
]
palette.append((0, 0, 0))
for px in range(W):
    for py in range(H):
        x = px / W * 3 - 2  # x = -2..1
        y = py / H * 2 - 1  # y = -1..1
        c = x + 1j * y
        z = 0j
        for n in range(ITER):
            z = z ** 2 + c
            if abs(z) > LIMIT:
                break
        img.putpixel((px, py), palette[n])
img.save('mand1.png')
img.show()
