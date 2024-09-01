import cv2
import numpy as np

cap = cv2.VideoCapture('videot.mp4')

algo = cv2.bgsegm.createBackgroundSubtractorMOG()

def center_handle(x, y, w, h):
    cx = x + int(w / 2)
    cy = y + int(h / 2)
    return cx, cy

detect = []
offset = 6 
counter = 0

while True:
    ret, frame1 = cap.read()

    if not ret:
        break
    

    grey = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(grey, (3, 3), 5)

    imgsub = algo.apply(blur)

    dilat = cv2.dilate(imgsub, np.ones((5, 5), np.uint8))

    kernal = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    dilatada = cv2.morphologyEx(dilat, cv2.MORPH_CLOSE, kernal)
    dilatada = cv2.morphologyEx(dilatada, cv2.MORPH_CLOSE, kernal)

    contours, _ = cv2.findContours(dilatada, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.line(frame1, (25, 550), (1200, 550), (255, 127, 0), 2)

    for (i, c) in enumerate(contours):
        (x, y, w, h) = cv2.boundingRect(c)
        validate_counter = (w >= 80) and (h >= 80)
        if not validate_counter:
            continue

        cv2.rectangle(frame1, (x, y), (x + w, y + h), (0, 255, 0), 2)

        center = center_handle(x, y, w, h)
        detect.append(center)
        cv2.circle(frame1, center, 4, (0, 0, 255), -1)

        for (x, y) in detect:
            if 550 - offset < y < 550 + offset:
                counter += 1
                cv2.line(frame1, (25, 550), (1200, 550), (0, 127, 255), 3)
                detect.remove((x, y))
                print("Vehicle Counter: " + str(counter))

    cv2.putText(frame1, "VEHICLE COUNTER: " + str(counter), (450, 70), cv2.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 5)

    cv2.imshow('Original Video', frame1)

    if cv2.waitKey(1) == 13:
        break

cap.release()
cv2.destroyAllWindows()