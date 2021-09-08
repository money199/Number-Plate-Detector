import cv2
import numpy as np
#####################3
minArea =500
color =(0,255,0)
count=0
###########################
address='http://192.168.29.41:8080/video'
cap=cv2.VideoCapture(address)

nplateCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_russian_plate_number.xml')
while True:
    sucess,img=cap.read()
    img=cv2.resize(img,(640,480))
    imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    numberPlates = nplateCascade.detectMultiScale(imgGray, 1.1, 4)
    for (x, y, w, h) in numberPlates:
        area =w*h
        print(x,y,w,h)
        if area > minArea :
            cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
            cv2.putText(img,"Number Plate",(x,y-5),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)
            imgRoi =img[y:y+h,x:x+w] #region of plate
            cv2.imshow("plate",imgRoi)

    cv2.imshow("img",img)

    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite("assets/NoPlate_" + str(count) + ".jpg", imgRoi)
        cv2.rectangle(img, (0, 200), (640, 300), (0, 255, 0), cv2.FILLED)
        cv2.putText(img,"Scan Saved", (150, 265), cv2.FONT_HERSHEY_DUPLEX,
                    2, (0, 0, 255), 2)
        cv2.imshow("Result", img)
        cv2.waitKey(500)
        count += 1


cv2.destroyAllWindows()