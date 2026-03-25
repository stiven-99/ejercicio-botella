class Base_datos:
    def __init__(self):
        self.lista_botella = []

    def agregar_botella(self, nuevo_obj):
        self.lista_botella.append(nuevo_obj)
        print("botella guardada exitosamente")
        print(nuevo_obj.get_material())
    