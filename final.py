import cv2
import winsound
cam = cv2.VideoCapture(0)
while cam.isOpened():
    ret, frame = cam.read()
    ret, frame1 = cam.read()
    dif = cv2.absdiff(frame, frame1)
    blk = cv2.cvtColor(dif, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(blk, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 20, 255, cv2.THRESH_BINARY)
    dilation = cv2.dilate(thresh, None, iterations=3)
    contours, _ = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for c in contours:
        if cv2.contourArea(c)<5000:
            continue
        x, y, w, h = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        winsound.PlaySound('alert.wav', winsound.SND_ASYNC)
    if cv2.waitKey(10) == ord('q'):
        break
    cv2.imshow('out cam', frame)
