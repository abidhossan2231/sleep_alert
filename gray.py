import cv2
camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret, frame = camera.read()
    ret, frame1 = camera.read()
    dif = cv2.absdiff(frame, frame1)
    gray = cv2.cvtColor(dif, cv2.COLOR_RGB2GRAY)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('out cam', gray)
