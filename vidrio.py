from botella import Botella

class Botella_vidrio(Botella):
    def __init__(self, material, capacidad, forma):
        super().__init__(material, capacidad)
        self.forma = forma

    def set_datos(self, nueva_forma):
        self.forma = nueva_forma
        
    def ver_info(self):
        info = f"informacion de botella plastica \n material: {self.material} \n capacidad: {self.capacidad} \n forma: {self.forma}"
        return info 