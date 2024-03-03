import cv2

img = cv2.imread("C:/Users/vrish_fl8o8kc/Downloads/Python Projects/104 Add Images And Text Project/PRO-104-Project-Image-main/PRO-104-Project-Image-main/solar-system.jpg")
img = cv2.cvtColor(img,cv2.COLOR_BAYER_RGGB2RGB)
cv2.putText(img,"The Sun",(20,300),cv2.FONT_HERSHEY_COMPLEX,0.5,(255,255,255))

cv2.imshow("The Planets",img)

cv2.waitKey(0)
