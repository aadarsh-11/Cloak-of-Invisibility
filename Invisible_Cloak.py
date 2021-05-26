import cv2
import numpy as np
import cv2 as cv
import os

window = cv.VideoCapture(0)
# hsv ranges for cloak color (blue here)
low_h = 100
low_s = 100
low_v = 50
high_h = 120
high_s = 255
high_v = 255

window_name = 'Lights, Cloak and ACTION!'
background_image = "background.jpg"
flag = 1

while window.isOpened():
    ret, frame = window.read()
    if ret:
        # save background image on camera start
        if flag:
            cv.imwrite(background_image, frame)
            background = cv.imread(background_image)
            flag = 0

        # get hcv form of image to detect colored object
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

        # define range of cloak color in HSV
        l_range = np.array([low_h, low_s, low_v])
        u_range = np.array([high_h, high_s, high_v])

        # Threshold the HSV image to get only cloak colors
        mask = cv.inRange(hsv, l_range, u_range)
        cloak = cv.bitwise_and(background, background, mask=mask)

        # Threshold the HSV image to get everything but cloak
        mask2 = cv.bitwise_not(mask)
        cloak_back = cv.bitwise_and(frame,frame, mask=mask2)

        # merge both the masks
        final_frame = cloak+cloak_back

        cv.imshow(window_name, final_frame)

        if cv.waitKey(3) == ord('q'):
            break

if os.path.exists(background_image):
    os.remove(background_image)

window.release()
cv.destroyAllWindows()
