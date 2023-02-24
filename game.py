import carta1
import carta2
import cartacasa
import JoinToGame

Game = JoinToGame.NewGame
Cantidad_de_jugadores = JoinToGame.CantidadJugadores

if Game == 'si':

    if Cantidad_de_jugadores == 1:
        cartacasa.turno_casa()
        print("Las cartas de", JoinToGame.NombreJugador1, "son:")
        carta1.carta1_Jugador1()
        carta2.carta2_Jugador1()
        carta1 = carta1.Deck()
        carta2 = carta2.Deck()
        puntosjugador1 = carta1 + carta2
        cantidad_puntos = sum(puntosjugador1)
        print("El valor de las cartas del jugador", JoinToGame.NombreJugador1, "es", sum(puntosjugador1)) 

    if cantidad_puntos > 21:
        print("Su resultado es mayor a 21, ha perdido la partida \n")

    if cantidad_puntos == 21:
        print("Su resultado es igual a 21, ha ganado la partida \n")

import carta1
while cantidad_puntos < 21:
    pregunta = input("Desea pedir otra carta: 'si' o 'no' \n")
    if pregunta == 'si':
        #carta1.carta1_Jugador1()
        carta3 = carta1.Deck()
        puntosjugador1_1 = puntosjugador1 + carta3
        cantidad_puntos1 = sum(puntosjugador1_1)
        print("El valor de las cartas del jugador", JoinToGame.NombreJugador1, "es", sum(puntosjugador1_1))

    break   

        

        
