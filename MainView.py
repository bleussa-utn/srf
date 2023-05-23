from tkinter import *
from Registro import registro
from Singleton import Singleton
class MainView:
    def __init__(self):
        
        pantalla = Tk()
        pantalla.geometry("300x400")  # Asignamos el tamaño de la ventana 
        pantalla.title("Reconocimiento Facial")       # Asignamos el titulo de la pantalla
        pantalla.configure(bg = '#F1F1F1')
        pantalla.resizable(False, False)
        Label(text = "SRF Beta", bg = "#0066ff", width = "50", height = "4", font = ("Verdana", 18), fg = "#ffffff").pack() # Asignamos caracteristicas de la ventana
        
        #--------------- Vamos a Crear los Botones -------------------------
        
        # TODO: agregar metodo login y agregar metodo registro
        Label(text = "", bg = "#f1f1f1").pack()  # Creamos el espacio entre el titulo y el primer boton
        Button(text = "Iniciar Sesion", height = "3", width = "20", bg = "#ffffff", fg = "#0060ff", borderwidth = "0",  command = "", font = ("Verdana", 14)).pack()
        Button(text = "Registro", height = "3", width = "20", bg = "#ffffff", fg = "#0060ff", borderwidth = "0", command = registro, font = ("Verdana", 14)).pack()
        Label(text = "", bg = "#f1f1f1").pack() # Creamos el espacio entre el primer boton y el segundo boton
        # Se carga la referencia del MainView en el Singleton        
        singleton_instance = Singleton.get_instance()  # Crea una instancia de Singleton
        singleton_instance.set_main_screen(pantalla)  # Llama al método set_main_screen()
        pantalla.mainloop()
        
MainView()
        
