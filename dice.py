from random import randint 


class Dice:

    @staticmethod
    def rollDie(die):
        return randint(1,die)
    
    @staticmethod
    def D6():
        return rollDie(6)

print(Dice.D6())