from random import randint 


class Dice:

    @staticmethod
    def rollDie(die):
        return randint(1,die)
    
    @staticmethod
    def D6():
        return Dice.rollDie(6)
    
    @staticmethod
    def D10():
        return Dice.rollDie(10)
    
    @staticmethod
    def D20():
        return Dice.rollDie(20)

print(Dice.D6())