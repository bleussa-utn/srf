from Singleton import Singleton
from tkinter import *
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