import cv2
import numpy as np

img = np.zeros((64,64,3))
cv2.imshow("test", img)
res = cv2.waitKey(0)
print('You pressed %d (0x%x), LSB: %d (%s)' % (res, res, res % 256,
    repr(chr(res%256)) if res%256 < 128 else '?'))