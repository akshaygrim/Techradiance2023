import cv2 #importing opencv 
cap = cv2.VideoCapture(0)
#infinite loop to keep the program running 
while True:
    # frames from the cam 
    ret, frame = cap.read()
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == ord('p'):
        cv2.imwrite("cap.jpg", frame)
        break #ends the conditon 
cap.release()
cv2.destroyAllWindows() # terminates 
