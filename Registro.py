import cv2   
from tkinter import *
from Singleton import Singleton
from matplotlib import pyplot
from facenet_pytorch import MTCNN

def registro():
  global pantallaRegistro
  global password
  global passwordEntrada
  global userEntrada
  global usuario
  pantallaRegistro = Toplevel(Singleton.get_main_screen()) #Esta pantalla es de un nivel superior a la principal
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
  Button(pantallaRegistro, text = "Registro Tradicional", width = 15, height = 1, command =registrar_usuario).pack()
    
    
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
    registroExitoso()   

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

    def reg_rostro(img, lista_resultados):
        data = pyplot.imread(img)
        for i in range(len(lista_resultados)):
            cajas = lista_resultados[0][0]  # Obtener el primer array de la tupla
            x1, y1, ancho, alto = cajas
            y2 = y1 + alto
            x2 = x1 + ancho

            x1, y1, ancho, alto = int(x1), int(y1), int(ancho), int(alto)
            x2, y2 = int(x2), int(y2)
            cara_reg = data[y1:y2, x1:x2]

            x2,y2 = x1 + ancho, y1 + alto
            pyplot.subplot(1, len(lista_resultados), i+1)
            pyplot.axis('off')
            cara_reg = data[y1:y2, x1:x2]
            cara_reg = cv2.resize(cara_reg,(150,200), interpolation = cv2.INTER_CUBIC) #Guardamos la imagen con un tamaño de 150x200
            cv2.imwrite(usuario_img+".jpg",cara_reg)
            pyplot.imshow(data[y1:y2, x1:x2])
        pyplot.show()

    img = usuario_img+".jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect(pixeles)
    reg_rostro(img, caras)
    registroExitoso()   

def registroExitoso():
    # Limpia la ventana
    for widget in pantallaRegistro.winfo_children():
        widget.destroy()
    # Crea el nuevo Label de éxito
    Label(pantallaRegistro, text="Registro Exitoso", fg="green", font=("Calibri",14)).pack()
    pantallaRegistro.update()  # Actualiza la ventana
    pantallaRegistro.after(1200, pantallaRegistro.destroy())
