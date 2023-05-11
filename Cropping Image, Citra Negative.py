import matplotlib.pyplot as plt
import cv2 as cv
import numpy as np

img = cv.imread("image/riram.jpg")
img2 = cv.imread("image/uin.png")

riramCropped = img[100:100+200, 100:100+200]
uinCropped = img2[100:100+200, 100:100+200]

print('Riram Ori Shape : ' ,img.shape)
print('Riram Crop Shape : ' ,img.shape)

print('Uin Ori Shape : ' ,img2.shape)
print('Uin Crop Shape : ' ,img2.shape)

fig, axes = plt.subplots(2, 2, figsize=(5, 5))
ax = axes.ravel()

ax[0].imshow(img)
ax[0].set_title("Citra Input 1")
ax[1].imshow(img2, cmap='gray')
ax[1].set_title('Citra Input 2')
ax[2].imshow(riramCropped)
ax[2].set_title("Citra Output 1")
ax[3].imshow(uinCropped, cmap='gray')
ax[3].set_title('Citra Output 2')
fig.tight_layout()
plt.show()

inv = 255 - uinCropped
print('Shape Input : ', riramCropped.shape)
print('Shape Output : ',inv.shape)

fig, axes = plt.subplots(2, 2, figsize=(5, 5))
ax = axes.ravel()

ax[0].imshow(riramCropped)
ax[0].set_title("Citra Input")
ax[1].hist(riramCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')
ax[2].imshow(inv)
ax[2].set_title('Citra Output (Inverted Image)')
ax[3].hist(inv.ravel(), bins=256)
ax[3].set_title('Histogram Output')
fig.tight_layout()#untuk menyesuaikan parameter subplot secara otomatis sehingga subplot sesuai dengan area gambar
plt.show()#menampilkan semua plot

copyuin = uinCropped.copy().astype(float)

shape = copyuin.shape
output1 = np.empty(shape)

for baris in range(0, shape[0] - 1):
    for kolom in range(0, shape[1] - 1):
        a1 = baris
        b1 = kolom
        output1[a1, b1] = copyuin[baris, kolom] / 192

fig, axes = plt.subplots(2, 2, figsize=(12, 12))
ax = axes.ravel()

ax[0].imshow(uinCropped, cmap='gray')
ax[0].set_title("Citra Input")
ax[1].hist(uinCropped.ravel(), bins=256)
ax[1].set_title('Histogram Input')
ax[2].imshow(output1, cmap='gray')
ax[2].set_title('Citra Output (Brightnes)')
ax[3].hist(output1.ravel(), bins=192)
ax[3].set_title('Histogram Input')
print(output1.shape)
plt.show()