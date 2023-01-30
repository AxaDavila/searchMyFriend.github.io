#Puedes utilizar la biblioteca de OpenCV en Python para implementar el reconocimiento facial. Aquí hay un ejemplo de código simple que detecta caras en una imagen y las marca con un rectángulo:

import cv2

# Cargar la imagen
img = cv2.imread("image.jpg")

# Cargar el clasificador de caras
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

# Convertir la imagen a gris
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Detectar caras en la imagen
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

# Dibujar un rectángulo alrededor de las caras detectadas
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# Mostrar la imagen con las caras marcadas
cv2.imshow("Faces", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
