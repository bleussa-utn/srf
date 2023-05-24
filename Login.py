from Singleton import Singleton
from tkinter import *
import cv2   
import os
from matplotlib import pyplot 
from facenet_pytorch import MTCNN
# Pantalla de Login
def login():
  # Variables para el resto de métodos
  global userEntrada
  global pantallaLogin
  global userVerificacion
  global passwordVerificacion
  global passwordEntrada
  #Obtenemos referencia a la Pantalla Principal
  pantallaLogin = Toplevel(Singleton.get_main_screen())
  pantallaLogin.title("Login")
  pantallaLogin.geometry("400x300")   #Creamos la ventana
  Label(pantallaLogin, text = "Login facial: debe de asignar un usuario:").pack()
  Label(pantallaLogin, text = "Login tradicional: debe asignar usuario y contraseña:").pack()
  Label(pantallaLogin, text = "").pack()  #Dejamos un poco de espacio
  
  userVerificacion = StringVar()
  passwordVerificacion = StringVar()
  
  #---------------------------------- Ingresamos los datos --------------------------
  Label(pantallaLogin, text = "Usuario * ").pack()
  userEntrada = Entry(pantallaLogin, textvariable = userVerificacion)
  userEntrada.pack()
  Label(pantallaLogin, text = "Contraseña * ").pack()
  passwordEntrada = Entry(pantallaLogin, textvariable = passwordVerificacion)
  passwordEntrada.pack()
  Label(pantallaLogin, text = "").pack()
  Button(pantallaLogin, text = "Inicio de Sesion Tradicional", width = 20, height = 1, command = verificacion_login).pack()

  #------------ Boton para hacer el login facial --------------------
  Label(pantallaLogin, text = "").pack()
  Button(pantallaLogin, text = "Inicio de Sesion Facial", width = 20, height = 1, command = login_facial).pack()

 #----------------- Funcion para autenticacion de usuario y contraseña --------------------------
def verificacion_login():
    log_usuario = userVerificacion.get()
    log_contra = passwordVerificacion.get()

    userEntrada.delete(0, END)
    passwordEntrada.delete(0, END)

    lista_archivos = os.listdir()   # Importamos la lista de archivos con la libreria os
    if log_usuario in lista_archivos:   #Comparamos los archivos con el que nos interesa
        archivo2 = open(log_usuario, "r")  #Abrimos el archivo en modo lectura
        verificacion = archivo2.read().splitlines()  #leera las lineas dentro del archivo ignorando el resto
        if log_contra in verificacion:
            print("Inicio de sesion exitoso")
            loginExitoso()
        else:
            print("Contraseña incorrecta, ingrese de nuevo")
            Label(pantallaLogin, text = "Contraseña Incorrecta", fg = "red", font = ("Calibri",11)).pack()
    else:
        print("Usuario no encontrado")
        Label(pantallaLogin, text = "Usuario no encontrado", fg = "red", font = ("Calibri",11)).pack()

def login_facial():
    #------------------Captura del rostro-----------------------------
    cap = cv2.VideoCapture(0)           	#Elegimos la camara con la que vamos a hacer la deteccion
    while(True):
        ret,frame = cap.read()          	#Leemos el video
        cv2.imshow('Login Facial',frame)     	#Mostrar el video en pantalla
        if cv2.waitKey(1) == 27:        	#Oprimir "Escape" para romper el video
            break
    usuario_login = userVerificacion.get()	#Con esta variable vamos a guardar la foto pero con otro nombre para no sobreescribir
    cv2.imwrite(usuario_login+"LOG.jpg",frame)   	#Guardamos la ultima caputra del video como imagen y asignamos el nombre del usuario
    cap.release()                           	#Cerramos
    cv2.destroyAllWindows()

    userEntrada.delete(0, END)   #Limpiamos los text variables
    passwordEntrada.delete(0, END)

 #----------------- Funcion para guardar el rostro --------------------------
    
    def log_rostro(img, lista_resultados):
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
            cara_reg = cv2.resize(cara_reg,(150,200), interpolation = cv2.INTER_CUBIC) #Guardamos la imagen 150x200
            cv2.imwrite(usuario_login+"LOG.jpg",cara_reg)

            return pyplot.imshow(data[y1:y2, x1:x2])
        
        pyplot.show()

    #-------------------------- Detectamos el rostro-------------------------------------------------------
    
    img = usuario_login+"LOG.jpg"
    pixeles = pyplot.imread(img)
    detector = MTCNN()
    caras = detector.detect(pixeles)
    log_rostro(img, caras)

#-------------------------- Funcion para comparar los rostros --------------------------------------------
    def orb_sim(img1,img2):
        orb = cv2.ORB_create()  #Creamos el objeto de comparacion
  
        kpa, descr_a = orb.detectAndCompute(img1, None)  #Creamos descriptor 1 y extraemos puntos claves
        kpb, descr_b = orb.detectAndCompute(img2, None)  #Creamos descriptor 2 y extraemos puntos claves

        comp = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True) #Creamos comparador de fuerza

        matches = comp.match(descr_a, descr_b)  #Aplicamos el comparador a los descriptores

        regiones_similares = [i for i in matches if i.distance < 70] #Extraemos las regiones similares en base a los puntos claves
        if len(matches) == 0:
            return 0
        return len(regiones_similares)/len(matches)  #Exportamos el porcentaje de similitud

    #---------------------------- Importamos las imagenes y llamamos la funcion de comparacion ---------------------------------
    print("Comparando")
    im_archivos = os.listdir()   # Importamos la lista de archivos con la libreria os
    if usuario_login+".jpg" in im_archivos:   # Comparamos los archivos con el que nos interesa
        rostro_reg = cv2.imread(usuario_login+".jpg",0)     #Importamos el rostro del registro
        rostro_log = cv2.imread(usuario_login+"LOG.jpg",0)  #Importamos el rostro del inicio de sesion
        similitud = orb_sim(rostro_reg, rostro_log)
        if similitud >= 0.90:
            Label(pantallaLogin, text = "Inicio de Sesion Exitoso", fg = "green", font = ("Calibri",11)).pack()
            print("Bienvenido al sistema: ",usuario_login)
            print("Compatibilidad con la foto del registro: ",similitud)
            loginExitoso()
        else:
              print("Rostro incorrecto, Cerifique su usuario")
              print("Compatibilidad con la foto del registro: ",similitud)
              Label(pantallaLogin, text = "Incompatibilidad de rostros", fg = "red", font = ("Calibri",11)).pack()
    else:
      print("Usuario no encontrado")
      Label(pantallaLogin, text = "Usuario no encontrado", fg = "red", font = ("Calibri",11)).pack()

def loginExitoso():
    # Limpia la ventana
    for widget in pantallaLogin.winfo_children():
        widget.destroy()
    # Crea el nuevo Label de éxito
    Label(pantallaLogin, text="Inicio de Sesión Exitoso", fg="green", font=("Calibri",14)).pack()
    pantallaLogin.update()  # Actualiza la ventana
    pantallaLogin.after(1200, pantallaLogin.destroy())
