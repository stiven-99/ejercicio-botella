class Base_datos:
    def __init__(self):
        self.lista_botella = []

    def agregar_botella(self, nuevo_obj):
        self.lista_botella.append(nuevo_obj)
        print("botella guardada exitosamente")
    
    def eliminar_botella(self, posicion):
        if 0 <= posicion<len(self.lista_botella):
            self.lista_botella.pop(posicion)
        else:
            print("posicion no encontrada")

    