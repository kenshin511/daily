# -*- coding: utf-8 -*-
import cv2
import numpy as np
import matplotlib.pyplot as plt


# def triWave(L(길이), thick, 배율(a) )
thick = 5
img = np.zeros((50, 100), np.uint8)

# +x,y 좌표 계산 함수 

x1, y1 = 10, 5
x2, y2 = 20, 30
x3, y3 = 70, 20
x4, y4 = 50, 10

pts = np.array([[x1, y1], [x2, y2], [x3, y3], [x4, y4]], np.int32)
pts = pts.reshape((-1,1,2))
img = cv2.polylines(img, [pts], False, 255, thick)

plt.imshow(img)
plt.show()