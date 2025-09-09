#damian bermudez lara
#clases

print("programa gatos y perros \n")

#clase

class gato:
    #construcctor
    def __init__(self, raza, color, nombre):
        #atributos
        self.raza = raza
        self.color = color
        self.nombre = nombre
    
    #metodos
    def maullar(self):
        print(f"el gato se llama {self.nombre} es un {self.raza} de color {self.color} y dice MIAU!")
    
    def feliz(self):
        print(f"el gato {self.nombre} esta jugando con rollo de lana y esta feliz")
    




el_gato = gato(input("el gato es de raza: "), input("el gato es de color: "), input("el gato se llama: "))
el_gato.maullar()
el_gato.feliz()




