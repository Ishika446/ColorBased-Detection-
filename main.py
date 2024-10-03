import cv2
import numpy as np

image = cv2.imread("C:\\Users\Ishika\OneDrive\Pictures\Screenshots\Screenshot 2024-10-03 135031.png")

hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

lower_red1=np.array([0,120,70])
upper_red1=np.array([10,255,255])

lower_red2=np.array([170,120,70])
upper_red2=np.array([180,255,255])

lower_green=np.array([35,100,100])
upper_green=np.array([85,255,255])

mask1=cv2.inRange(hsv_image,lower_red1,upper_red1)
mask2=cv2.inRange(hsv_image,lower_red2,upper_red2)
mask3=cv2.inRange(hsv_image,lower_green,upper_green)

red_mask=mask1+mask2
red_object=cv2.bitwise_and(image,image, mask=red_mask)
green_object=cv2.bitwise_and(image,image, mask=mask3)

mask = cv2.inRange(hsv_image, lower_blue, upper_blue)
blue_objects = cv2.bitwise_and(image, image, mask=mask)

cv2.imshow("Original Image", image)
cv2.imshow("Blue Objects", blue_objects)
cv2.imshow("Red object",red_object)
cv2.imshow("Green object",green_object)
cv2.waitKey(0)
cv2.destroyAllWindows()

