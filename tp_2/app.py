import cv2
 image=cv2.imread("renard.png")

if image is None:
 print("image intouvable")

else:
 gris=cv2.cvtcolor(image,cv2.COLOR_BGR2GRAY)
 cv2.imshow("originale",image)
 cv2.imshow("niveau de gris",gris)
 cv2.waitkey(0)

 cv2.destroyAlWindows()