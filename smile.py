
#importing open cv module
import cv2
#declaring vairlabes for cascade file
f_cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
smile_cas = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
#declaring vairable for video capture
cap = cv2.VideoCapture(0)
#starting the infite loop for the program to run
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = f_cas.detectMultiScale(gray, 1.3, 5)
#drawing the outlines for smile and face (mentioning dimnesions)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]
        smiles = smile_cas.detectMultiScale(roi_gray, 1.8, 20)
        for (sx, sy, sw, sh) in smiles:
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)     #box around simle 
#
    cv2.imshow('Face and Smile Detection', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):          # hotkey for exiting the program 
        break#ends the loop

cap.release()
cv2.destroyAllWindows()#calling out all fucntions