import cv2
import numpy as np
from matplotlib import pyplot as plt

input = cv2.imread("images/love.jpg")
# cv2.imshow("Love",input)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# print input.shape
# print "Height of Image: ",int(input.shape[0]),' pixels'
# print "Width of Image: ",int(input.shape[1]), 'pixels'

#save image
# cv2.imwrite("images/copy_love.jpg",input)
# cv2.imwrite("images/copy_love.png",input)

#We use cvtColor, to convert to grayscale
#gray images are easier to process, color information is not always necessary
# gray_image=cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
# cv2.imshow("Grayscale",gray_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

#first pixel's color
#open cv stores color as B,G,R
# gray_image=cv2.cvtColor(input,cv2.COLOR_BGR2GRAY)
# print gray_image[0,0]

#split colors
B,G,R = cv2.split(input)
# cv2.imshow("Red",R)
# cv2.imshow("Green",G)
# cv2.imshow("Blue",B)

# cv2.waitKey(0)
# cv2.destroyAllWindows()
#
# merged = cv2.merge([B,G,R+100])
# cv2.imshow("Merged",merged)
#
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# zeros=np.zeros(input.shape[:2],dtype="uint8")
# cv2.imshow("Red",cv2.merge([zeros,zeros,R]))
# cv2.imshow("Green",cv2.merge([zeros,G,zeros]))
# cv2.imshow("Blue",cv2.merge([B,zeros,zeros]))
#
# cv2.waitKey()
# cv2.destroyAllWindows()


#Histograms are a great way to visualize
