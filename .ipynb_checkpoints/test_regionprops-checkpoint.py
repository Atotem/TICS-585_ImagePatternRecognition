"""
 Universidad Adolfo Ibañez
 Facultad de Ingeniería y Ciencias
 TICS 585 - Reconocimiento de Patrones en imágenes

 Ejemplo de funcion RegionProps
 Autor:. Miguel Carrasco (26-08-2021)
 rev.1.0
"""
import cv2
import matplotlib.pyplot as plt
from skimage.measure import regionprops, label

#lectura de una imagen
im = cv2.imread('sopa_letras.png')
gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

#binarizamos la imagen
ret, bw = cv2.threshold(gray, 125,255,cv2.THRESH_BINARY_INV)


#etiquetamos cada imagen
label_bw = label(bw)

plt.figure()
plt.imshow(bw, cmap='gray')

# para cada region, extraemos la información de coordenadas
for region in regionprops(label_image= label_bw):
    #para cada region extraemos información especifica
    cxy = region.centroid
    plt.scatter(cxy[1], cxy[0], marker='x', color='blue')

plt.show()
