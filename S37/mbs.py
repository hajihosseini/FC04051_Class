import matplotlib.pyplot as plt

W, H, I = 600, 400, 100  # width, height, iterations

xmin, xmax = -2.5, 1.0
ymin, ymax = -1.25, 1.25

img = [[0] * W for _ in range(H)]

for py in range(H):
    y = ymin + (ymax - ymin) * py / (H - 1)
    for px in range(W):
        x = xmin + (xmax - xmin) * px / (W - 1)
        c = complex(x, y)
        z = 0j
        n = 0
        while (z.real * z.real + z.imag * z.imag) <= 4.0 and n < I:
            z = z*z + c
            n += 1
        img[py][px] = n  # higher = longer to escape

plt.imshow(img, cmap="magma", extent=[xmin, xmax, ymin, ymax])
plt.axis("off")
plt.show()
