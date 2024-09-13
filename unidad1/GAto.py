class Gato:
    #
    def __init__(self) -> None:
        self.Color = ""
        self.Raza = ""
        self.Nombre = ""

    def pepe(self):
        print (self.color)
        print (self.dueño)
    pass

loki = Gato()
chester = Gato()

chester.color = "naranja"
chester.dueño = "Adrian"

loki.color = "pardo"
loki.dueño = "Diego"
print(loki)
print(chester)