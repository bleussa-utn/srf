from Singleton import Singleton
from tkinter import *
import cv2   
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
  Button(pantallaLogin, text = "Inicio de Sesion Tradicional", width = 20, height = 1, command = "verificacion_login").pack() #TODO: agregar funciones para la login tradicional

  #------------ Boton para hacer el login facial --------------------
  Label(pantallaLogin, text = "").pack()
  Button(pantallaLogin, text = "Inicio de Sesion Facial", width = 20, height = 1, command = "login_facial").pack()  #TODO: agregar funciones para el login facial

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
    