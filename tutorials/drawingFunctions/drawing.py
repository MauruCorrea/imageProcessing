
import numpy as np
import cv2 as cv
# Create a black image
img = np.zeros((512,512,3), np.uint8)
# Draw a diagonal blue line with thickness of 5 px
#cv.line(img,(0,0),(511,511),(255,0,0),5)

# Draw Retangle
#cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Draw Circle
# cv.circle(img,(190,190), 63, (0,0,255), -1)
# Draw OpenCV logo

cv.circle(img,(190,300), 64, (0,255,0), -1) #green
cv.circle(img,(322,300), 64, (255,0,0), -1) #blue
cv.circle(img,(252,180), 64, (0,0,255), -1) #red

cv.circle(img,(190,300), 32, (0,0,0), -1) # green hole
cv.circle(img,(322,300), 32, (0,0,0), -1) # blue hole
cv.circle(img,(252,180), 32, (0,0,0), -1) # red hole

#green
pts = np.array([[190,300],[255,290],[250,200],[190,300]], np.int32)
pts = pts.reshape((-1,1,2))
cv.fillPoly(img,[pts],(0,0,0))

#blue
pts = np.array([[322,300],[290,232],[370,232],[322,300]], np.int32)
pts = pts.reshape((-1,1,2))
cv.fillPoly(img,[pts],(0,0,0))

#red 
pts = np.array([[252,180],[190,290],[290,234],[252,180]], np.int32)
pts = pts.reshape((-1,1,2))
cv.fillPoly(img,[pts],(0,0,0))

#Draw openCV logo ellipses
#img = cv.ellipse(img, (256, 80), (60,60), 120,0,300,(0,0,255),-1)
#img = cv.ellipse(img, (256, 80), (20,20), 120,0,300,(0,0,0),-1)
#img = cv.ellipse(img, (176, 200), (60,60), 0,0,300,(0,255,0),-1)
#img = cv.ellipse(img, (176, 200), (20,20), 0,0,300,(0,0,0),-1)
#img = cv.ellipse(img, (336, 200), (60,60), 300,0,300,(255,0,0),-1)
#img = cv.ellipse(img, (336, 200), (20,20), 300,0,300,(0,0,0),-1)

# Draw Elipse
#cv.ellipse(img,(256,256),(100,50),0,0,180,255,-1)

# Draw Polygon
#pts = np.array([[10,5],[20,30],[70,20],[50,10]], np.int32)
#pts = pts.reshape((-1,1,2))
#cv.polylines(img,[pts],True,(0,255,255))
#cv.fillPoly(img,[pts],(0,0,0))

# Add Text
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'Mauru S2',(10,500), font, 2,(255,255,255),2,cv.LINE_4)





cv.imshow("Canvas", img)

cv.waitKey(0)
cv.destroyAllWindows()