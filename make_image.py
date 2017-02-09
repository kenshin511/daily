# -*- coding: utf-8 -*-
"""
make_image.py
"""
#%%
import cv2
import numpy as np
import matplotlib.pyplot as plt

#%%
x = np.arange(360).astype(np.uint16)
ang = np.deg2rad(x)
y = ((np.sin(ang)+1)*30).astype(np.uint16)+50
x = x+50

rows, cols =y.max()+50,  x.max()+50
base = np.zeros((rows,cols), np.uint8)

base[y, x] = 255

# ===========================================================
# Dilation
kernel = np.ones((10, 1))
dst = cv2.dilate(base, kernel)    

#%%
plt.imshow(base, 'gray')
plt.show()

plt.imshow(dst, 'gray')
plt.show()

plt.plot(x, y)
plt.show()

#%%
"""
x = np.linspace(0, 2*np.pi, 10)
y = np.sin(x)

plt.plot(x, y)
plt.show()
"""

#%%
# TRUNC
A = np.zeros((100,100))
for c in range(10,100, 10):
    A[:,:-c] = c
B = A.copy() # 

B[B>70] = 0

plt.figure(1)
plt.subplot(121)
plt.imshow(A)

plt.subplot(122)
plt.imshow(B)
plt.axis('off') #
plt.show()

plt.figure(1) #
plt.plot(A[0,:])
plt.ylim([-5,100])

plt.figure(2) #
plt.plot(B[0,:])
plt.ylim([-5,100]) #




