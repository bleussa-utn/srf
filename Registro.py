import cv2   
from tkinter import *
from MainView import MainView
from matplotlib import pyplot
from facenet_pytorch import MTCNN

def registro():
  global pantallaRegistro
  global password
  global passwordEntrada
  global userEntrada
  global usuario
  pantallaRegistro = Toplevel(MainView()) #Esta pantalla es de un nivel superior a la principal #ToDO: arreglar multiple instancia de Vista Principal
  pantallaRegistro.title("Registro")
  pantallaRegistro.geometry("400x300")  #Asignamos el tamaño de la ventana
     #--------- Empezaremos a crear las entradas ----------------------------------------
  
  usuario = StringVar()
  password = StringVar()
  # Instrucciones
  Label(pantallaRegistro, text = "Registro facial: debe de asignar un usuario:").pack()
  Label(pantallaRegistro, text = "Registro tradicional: debe asignar usuario y contraseña:").pack()
  # Labels y Entradas de Texto para Usuario y Password
  Label(pantallaRegistro, text = "Usuario * ").pack()  #Mostramos en la pantalla 1 el usuario
  userEntrada = Entry(pantallaRegistro, textvariable = usuario) #Creamos un text variable para que el usuario ingrese la info
  userEntrada.pack()
  Label(pantallaRegistro, text = "Contraseña * ").pack()  #Mostramos en la pantalla 1 la contraseña
  passwordEntrada = Entry(pantallaRegistro, textvariable = password) #Creamos un text variable para que el usuario ingrese la contra
  passwordEntrada.pack()
  Label(pantallaRegistro, text = "").pack()  #Dejamos un espacio para la creacion del boton
  Button(pantallaRegistro, text = "Registro Tradicional", width = 15, height = 1, command ="registrar_usuario").pack()  #Creamos el boton ToDO: agregar método funcion tradicional
    
    
  #------------ Vamos a crear el boton para hacer el registro facial --------------------
  Label(pantallaRegistro, text = "").pack()
  Button(pantallaRegistro, text = "Registro Facial", width = 15, height = 1, command = registro_facial).pack()

def registrar_usuario():
    usuario_info = usuario.get() #Obetnemos la informacion alamcenada en usuario
    contra_info = password.get() #Obtenemos la informacion almacenada en password

    archivo = open(usuario_info, "w") #Abriremos la informacion en modo escritura
    archivo.write(usuario_info + "\n")   #escribimos la info
    archivo.write(contra_info)
    archivo.close()

    #Limpiaremos los text variable
    userEntrada.delete(0, END)
    passwordEntrada.delete(0, END)

    #Ahora le diremos al usuario que su registro ha sido exitoso
    print("Registro exitoso")   

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
