'''
Clase Card: representa una carta de naipe
'''


class Card:
    # atributos de instancia de la clase card
    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    # metodo de la clas
    def print_card(self):
        print(
            f"{self.number}{self.suit}")