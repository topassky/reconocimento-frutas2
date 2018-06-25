#se importan las libreriras de opencv
import numpy as np
import cv2

fondo=cv2.imread("fondo.jpg")
mayor=0
kmayor=343
print('Presione dos veces "q" para salir')
# Crea una ventana
valido = True
#codigo para detectar la camara y recibe un solo parametro "cero" camara principal
captura = cv2.VideoCapture(0)
#Se valida que exista una cámara a la que se pueda acceder
if not captura.isOpened()  :
    print("No es posible acceder al dispositivo")

while(True):
    #Se captura cada fotograma
    try :
        ret , fotograma = captura.read()
        alto, ancho, canales = fotograma.shape
        salida = np.zeros( (alto,ancho,canales), np.uint8 )
        

    except:
        print("No se reconoce el dispositivo")
        valido = False


    if valido == True:

        fotor=cv2.add(fondo,fotograma)
        cv2.imshow('Entrada',fotor)
    

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Liberar la cámara
captura.release()
#cv2.destroyAllWindows()


cv2.imwrite("Entrada.jpg",fotor)
imagen=cv2.imread("Entrada.jpg")
imagen1=imagen[142:360,176:481]

cv2.imwrite("Template.jpg",imagen1)
k=0
img=( cv2.imread('banano.jpg'),cv2.imread('banano-1.jpg'),cv2.imread('banano-2.jpg'),cv2.imread('banano-3.jpg'),
      cv2.imread('manzana.jpg'),cv2.imread('manzana-1.jpg'),cv2.imread('manzana-2.jpg'),cv2.imread('manzana-3.jpg'),cv2.imread('manzana-4.jpg'),
      cv2.imread('manzana-5.jpg'),cv2.imread('gulupa.jpg'),cv2.imread('gulupa-2.jpg'),cv2.imread('gulupa-3.jpg'),cv2.imread('gulupa-4.jpg')
      ,cv2.imread('aguacate.jpg'),cv2.imread('aguacate-1.jpg'),cv2.imread('aguacate-2.jpg'),cv2.imread('aguacate-3.jpg'),cv2.imread('aguacate-4.jpg')
      ,cv2.imread('aguacate-5.jpg'),cv2.imread('aguacate-6.jpg'),cv2.imread('aguacate-7.jpg'),cv2.imread('gulupa-5.jpg'),cv2.imread('naranja.jpg')
      ,cv2.imread('naranja-1.jpg'),cv2.imread('naranja-2.jpg'),cv2.imread('naranja-3.jpg'))

template = cv2.imread('Template.jpg')


methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]

while(True):
    for k in range (0,26):
        res = cv2.matchTemplate(img[k] ,template, methods[1])
        alto, ancho = res.shape
        ac=0
        contador=0
        for w in range (0,alto):
            for z in range (0,ancho):
                ac=ac+res[w,z]
                contador=contador+1

        max_val=ac/contador
                    
        cv2.imshow("Muestra",template)
        

        if max_val>mayor:
            mayor=max_val
            kmayor=k
           
    ch=0xFF& cv2.waitKey()
    if ch==ord('q'):
        
        break


if (max_val>0.9):


    if (kmayor==0)or(kmayor==1)or(kmayor==2)or(kmayor==3):
        print("Es un banano")
    if (kmayor==4)or(kmayor==5)or(kmayor==6)or(kmayor==7)or(kmayor==8)or(kmayor==9):
        print("Es una manzana")
    if (kmayor==10)or(kmayor==11)or(kmayor==12)or(kmayor==13)or(kmayor==14)or(kmayor==23):
        print("Es una gulupa")
    if (kmayor==15)or(kmayor==16)or(kmayor==17)or(kmayor==18)or(kmayor==19)or(kmayor==20)or(kmayor==21)or(kmayor==22):
        print("Es una aguacate")
    if (kmayor==24)or(kmayor==25)or(kmayor==26)or(kmayor==27):
        print("Es una naranja")
else:
    print("El objeto no esta en la base de datos")



    

cv2.destroyAllWindows()        
    
    
    
    

        
        
        




   
    


    

