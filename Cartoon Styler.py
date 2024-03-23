import cv2 as cv
import numpy as np

video_file = 'korea.mp4'
video = cv.VideoCapture(video_file)

while video.isOpened():
    vaild, frame = video.read()
    if not vaild:
        print('Unable to read video')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    blur = cv.bilateralFilter(frame, 15, 40, 40)

    edge = 255 - cv.Canny(gray, 80, 160)
    edge = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)

    cartoon = cv.bitwise_and(blur, edge)

    frame = cv.resize(frame, (480, 270))
    cartoon = cv.resize(cartoon, (480, 270))

    merge = np.hstack((frame, cartoon))
    cv.imshow('Cartoon Styler: Original | Result', merge)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cv.destroyAllWindows()