import cv2
import numpy as np

def sketch(image):
    
    scale_factor = 70
    height = int(image.shape[0] * scale_factor/100)
    width = int(image.shape[1] * scale_factor/100)
    
    dim = (height,width)

    rescale = cv2.resize(image,dim,interpolation=cv2.INTER_AREA)
    
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
   
    sharp = cv2.filter2D(rescale,-1,kernel)

    gray = cv2.cvtColor(sharp,cv2.COLOR_BGR2GRAY)
    inv=255-gray
    
    blur = cv2.GaussianBlur(src=inv,ksize=(15,15),sigmaX=0,sigmaY=0)
    
    s = cv2.divide(gray,255-blur,scale=256)
    return s


cap = cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    cv2.imshow('Sketch',sketch(frame))
        
    cv2.imshow('Live',frame)
    if cv2.waitKey(1)==ord('d'):
        break
cap.release()
cv2.destroyAllWindows()
    