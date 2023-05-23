class Singleton:
    instance = None
    main_screen = None

    @staticmethod
    def get_instance():
        if Singleton.instance is None:
            Singleton.instance = Singleton()
        return Singleton.instance

    @staticmethod
    def set_main_screen(screen):
        Singleton.main_screen = screen

    @staticmethod
    def get_main_screen():
        return Singleton.main_screen

    def __init__(self):
        if Singleton.instance is not None:
            raise Exception("¡Clase Singleton!")
