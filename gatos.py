#damian bermudez lara
#clases gato

print("programa gato \n")

#clase

class gato:
    #constructor
    def __init__(self, raza, color, nombre, colorojos):
        #atributos
        self.raza = raza
        self.color = color
        self.colorojos = colorojos
        self.nombre = nombre
    
    #metodos
    def maullar(self):
        print(f"el gato se llama {self.nombre}, es un {self.raza} de color {self.color}, sus ojos son {self.colorojos} y dice MIAU!")
    
    def feliz(self):
        print(f"el gato {self.nombre} esta jugando con rollo de lana y esta feliz")
    


#objetos

el_gato = gato(input("el gato es de raza: "), input("el gato es de color: "), input("el gato se llama: "), input("el gato tiene sus ojos de color: "))
el_gato.maullar()
el_gato.feliz()




