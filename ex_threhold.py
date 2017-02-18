# -*- coding: utf-8 -*-
"""
ex_threshold.py
"""
import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('template.jpg', 0)
ri, ci = img.shape

rL = np.arange(ri)
cL = np.arange(ci)

#%% Method 1
res = np.zeros_like(img)
for r in rL:
    for c in cL:
        if img[r, c] > 127:
            res[r, c] = 255

plt.imshow(res)
plt.show()
#%% Method 2
res = img.copy()
for r in rL:
    for c in cL:
        if img[r, c] > 127:
            res[r, c] = 255
        else:
            res[r, c] = 0
plt.imshow(res)
plt.show()
            
#%% Method 3
img2 = img.ravel()
res = img2.copy()
for n, i in enumerate(img2):
    res[n] = 255 if i > 127 else 0

res = res.reshape(img.shape[0], -1)

plt.imshow(res)
plt.show()

#%% boolen
res = img.copy()
res[img > 127] = 0
res[img <= 127] = 255

plt.imshow(res)
plt.show()

#%% cv2
# github_test
# new branch test
# protect test

plt.imshow(res)
plt.show()