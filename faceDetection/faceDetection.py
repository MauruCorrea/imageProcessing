import cv2

captura = cv2.VideoCapture(0)

# Classificador
classificadorFace = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


while(1):
    ret, frame = captura.read()
    ##converter para cinza
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    ##detecta a face utilizando um classificador 
    faceDetection = classificadorFace.detectMultiScale(frameGray,minSize=(20,20))
    ##Desenha o retangulo na face
    for(x,y,l,a) in faceDetection:
        cv2.rectangle(frame, (x,y), (x+l, y+a), (0,0,255), 2) 



    cv2.imshow("Video", frame)
   
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

captura.release()
cv2.destroyAllWindows() 