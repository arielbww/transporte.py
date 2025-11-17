class Transporte:
    def __init__(self, velocidade, marca):
        self.velocidade = velocidade
        self.marca = marca

    def Mover(self):
        print("O transporte está se movendo")
    
class Carro(Transporte):
    def __init__(self, velocidade, marca):
        super().__init__(velocidade, marca)
    def Mover(self):
        print("O carro está rodando pela estrada")
    
class Moto(Transporte):
    def __init__(self, velocidade, marca):
        super().__init__(velocidade, marca)
    def Mover(self):    
        print("A moto está acelerando")
    
class Bicicleta(Transporte):
    def __init__(self, velocidade, marca):
        super().__init__(velocidade, marca)
    def Mover(self):
        print("A bicicleta está pedalando")

print("----RESULTADO FINAL----")    
moto = Moto("120KM/h", "YAMAHA")
moto.Mover()

carro = Carro("140KM/h", "FERRARI")
carro.Mover()

bicicleta = Bicicleta("50KM", "KSW")
bicicleta.Mover()