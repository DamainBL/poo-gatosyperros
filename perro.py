#Damian bermudez lara
#clases perro

print("programa perro \n")

#clase

class perro:
    #constructor
    def __init__(self, raza, color, nombre, colorojos):
        #atributos
        self.raza = raza
        self.color = color
        self.colorojos = colorojos
        self.nombre = nombre
    
    #metodos
    def ladrar(self):
        print(f"el perro se llama {self.nombre}, es un {self.raza} de color {self.color}, sus ojos son {self.colorojos} y dice GUAU!")
    
    def feliz(self):
        print(f"el perro {self.nombre} esta jugando con su pelota y esta feliz moviendo su cola")
    


#objetos

el_perro = perro(input("el perro es de raza: "), input("el perro es de color: "), input("el perro se llama: "), input("el perro tiene sus ojos de color: "))
el_perro.ladrar()
el_perro.feliz()




