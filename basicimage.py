import cv2
import uuid
import time

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
detector = cv2.CascadeClassifier(
    'Cascades/haarcascade_frontalface_default.xml')


sampleNum = 0
result=True
while result:
    ret, img = cam.read()
    colorrgba = cv2.cvtColor(img, cv2.COLOR_BGR2RGBA)
    faces = detector.detectMultiScale(colorrgba, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        # incrementing sample number
        sampleNum = sampleNum+1
        # saving the captured face in the dataset folder
        
        if sampleNum==30:
            cv2.imwrite("dataSet/User_"+str(uuid.uuid1())
                    [:8:].replace("-", "") + ".jpg", colorrgba[y:y+h, x:x+w])
            cv2.waitKey(2)
            cv2.imshow('frame', img)
            cam.release()
            cv2.destroyAllWindows()
            result=False
            break
        
         
    # wait for 100 miliseconds

    # break if the sample number is morethan 20

     
        
        
    
