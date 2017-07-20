import cv2
import Adafruit_BBIO.GPIO as GPIO
cascPath = "haarcascade_eye_tree_eyeglasses.xml"
GPIO.setup("P8_11", GPIO.OUT)
GPIO.output("P8_11",GPIO.LOW)
faceCascade = cv2.CascadeClassifier(cascPath)
cap=cv2.VideoCapture(-1)
cap.set(3,320)
cap.set(4,240)
key_var=0
i=0
counter=0
#cap.set(cv2.cv.CV_CAP_PROP_FPS, 10)
while (True):
        key_var=0
        i=0
        ret,frame=cap.read()
        if(ret):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(30, 30),flags=cv2.cv.CV_HAAR_SCALE_IMAGE)
                for (x, y, w, h) in faces:
                        i+=1
                        print('Looking forward')
                        GPIO.output("P8_11",GPIO.LOW)
                        #cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                        key_var=1
        if(key_var==0 and counter<=4 ):
                counter+=1

        elif(key_var==0 and counter>4 ):
                print("You've not been looking forward beyond the permissible time ")
                GPIO.output("P8_11",GPIO.HIGH)
        elif(key_var==1 and counter<=4):
                counter=0
        elif(key_var==1 and counter>4):
                counter=0
        if(i<2):
                GPIO.output("P8_11",GPIO.LOW)
                print("Not looking forward")
        #cv2.imshow('Video', frame)
        k=cv2.waitKey(20)
        if k>=27:
                break
#cv2.destroyAllWindows()
