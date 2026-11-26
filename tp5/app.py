import cv2

image = cv2.imread("renard.jpg")
if image is not None:
    gris = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    contours = cv2.Canny(gris, 100, 200)
    cv2.imshow("Contours", contours)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Image introuvable : verifiez le nom et l'emplacement de l'image")