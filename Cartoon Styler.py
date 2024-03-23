import cv2 as cv
import numpy as np
import os

video_file = 'traffic.mp4'
video_name = os.path.splitext(video_file)[0]
video = cv.VideoCapture(video_file)

fourcc = cv.VideoWriter_fourcc(*'XVID')
frame_rate = video.get(cv.CAP_PROP_FPS)
video_writer = cv.VideoWriter(f'cartoon_{video_name}.avi', fourcc, frame_rate, (480, 270))

while video.isOpened():
    valid, frame = video.read()
    if not valid:
        print('Unable to read video')
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    blur = cv.bilateralFilter(frame, 15, 40, 40)

    edge = 255 - cv.Canny(gray, 80, 160)
    edge = cv.cvtColor(edge, cv.COLOR_GRAY2BGR)

    cartoon = cv.bitwise_and(blur, edge)

    frame = cv.resize(frame, (480, 270))
    cartoon = cv.resize(cartoon, (480, 270))

    merge = np.vstack((frame, cartoon))
    cv.imshow('Cartoon Styler: Original | Result', merge)
    video_writer.write(cartoon)

    key = cv.waitKey(1) & 0xFF
    if key == 27:
        break

cv.destroyAllWindows()