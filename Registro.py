import cv2   
from tkinter import *
from MainView import MainView
def registro():
  global pantallaRegistro
  global password
  global passwordEntrada
  global userEntrada
  global usuario
  pantallaRegistro = Toplevel(MainView()) #Esta pantalla es de un nivel superior a la principal #ToDO: arreglar multiple instancia de Vista Principal
  pantallaRegistro.title("Registro")
  pantallaRegistro.geometry("400x300")  #Asignamos el tamaño de la ventana

    
  #------------ Vamos a crear el boton para hacer el registro facial --------------------
  Label(pantallaRegistro, text = "").pack()
  Button(pantallaRegistro, text = "Registro Facial", width = 15, height = 1, command = registro_facial).pack()

def registro_facial():
    #Vamos a capturar el rostro
    cap = cv2.VideoCapture(0)               #Elegimos la camara con la que vamos a hacer la deteccion
    while(True):
        ret,frame = cap.read()              #Leemos el video
        cv2.imshow('Registro Facial',frame)         #Mostramos el video en pantalla
        if cv2.waitKey(1) == 27:            #Cuando oprimamos "Escape" rompe el video
            break
    print(usuario.get())
    usuario_img = usuario.get()
    cv2.imwrite(usuario_img+".jpg",frame)       #Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()                               #Cerramos
    cv2.destroyAllWindows()

    userEntrada.delete(0, END)   #Limpiamos los text variables
    passwordEntrada.delete(0, END)
