import random
class Boec:
    def __init__(self,hp,attack):
        self.hp = hp
        self.attack = attack
    def be_attacked(self,attack):
        self.hp -= attack


def check_win():
        if piunguin.hp == 0 and sobaka.hp == 0:
            print("ничья")
            hfhhf = False
        if piunguin.hp <= 0:
            print("выиграла собака")
            hfhhf = False
        if sobaka.hp <= 0:
            print("выиграла пингвина")
            hfhhf = False

hits = 0
turn_toggler = random.randint(0,1)
hfhhf = True

sobaka = Boec(2,2)
piunguin = Boec(4,1)
while hfhhf == True:
    check_win()
    if turn_toggler == 1:
        sobaka.be_attacked(piunguin.attack)
        check_win()
        piunguin.be_attacked(sobaka.attack)
        check_win()
    if turn_toggler == 0:
        piunguin.be_attacked(sobaka.attack)
        check_win()
        sobaka.be_attacked(piunguin.attack)
        check_win()

 
# сделать чтобы первая аттака рандомно атаковали