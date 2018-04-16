from tictactoe import Partida


def main():
    partida = Partida()

    while not partida.isFinPartida():
        partida.refresco()
        jugada = int(input("Jugador "+str(partida.turno)+": "))
        partida.marcarCasilla(jugada)
    else:
        partida.refresco()
        if partida.isFinPartida():
            print("Gana el jugador {}".format(partida.isFinPartida()[1]))
        else:
            print("Empate")


main()
