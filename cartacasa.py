import Clases
import utils
import random

# crea una lista de 4 cartas que representa la mano de un jugador
user_hand = []
cartas = ["A",2,3,4,5,6,7,8,9,10,"J","Q","K"]
corazon = '\u2764'
palo_de_picas = '\u2660'
diamante = '\u2666'
trebol = '\u2618'
simbolos = (corazon, palo_de_picas, diamante, trebol)
numero = random.choice(cartas)   
simbolo = random.choice(simbolos)

def Deck():
    deck = []
    if numero == "A" : 
        NewValue = 1
        deck.append(NewValue)
        
    elif numero == 'J':
        NewValue = 10
        deck.append(NewValue)
        
    elif numero == "Q":
        NewValue = 10
        deck.append(NewValue)
        
    elif numero == "K":
        NewValue = 10
        deck.append(NewValue)
        
    else:
        deck.append(numero)
   # print(deck)

    return deck

def turno_casa():
    print("Las cartas de la casa son:")
    new_card = Clases.Card(simbolo, numero)
    user_hand.append(new_card)
    utils.show_hand(user_hand)
    resultado_casa2 = print("?")
    print("El valor de la carta de la casa es", Deck())

    return

