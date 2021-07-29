
import cv2 as cv
import sys
## read image
img = cv.imread(cv.samples.findFile("thumbsUp.jpg"))

#check if image was loaded correctly
if img is None:
    sys.exit("Could not read the image.")

#show image
cv.imshow("Display window", img)

#wait for a key to write the image as a png file
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("thumbsUp.png", img)

    

