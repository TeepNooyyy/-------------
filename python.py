import random
class Boec:
    def __init__(self,hp,attack):
        self.hp = hp
        self.attack = attack
    def be_attacked(self,attack):
        self.hp -= attack


hits = 0
turn_toggler = random.randint(0,1)
        

sobaka = Boec(2,2)
piunguin = Boec(4,1)
while True:
    if piunguin.hp <= 0:
        print("выиграла собака")
        break
    if sobaka.hp <= 0:
        print("выиграла пингвина")
        break
    sobaka.be_attacked(piunguin.attack)
    piunguin.be_attacked(sobaka.attack)

 
# сделать чтобы первая аттака рандомно атаковали