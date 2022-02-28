import cv2
camera = cv2.VideoCapture(0)
while camera.isOpened():
    ret, frame = camera.read()
    ret, frame1 = camera.read()
    dif = cv2.absdiff(frame, frame1)
    gray = cv2.cvtColor(dif, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilation = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cv2.drawContours(frame, contours, -1, (0, 255, 0), 2)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('out cam', frame)
