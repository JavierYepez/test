from tictactoe import Partida


def main():
    partida = Partida()

    while not partida.isFinPartida():
        partida.refresco()
        try:
            jugada = int(input("Jugador "+str(partida.turno)+": "))
        except ValueError:
            continue
        else:
            partida.marcarCasilla(jugada)
    else:
        partida.refresco()
        if partida.isFinPartida():
            print("Gana el jugador {}".format(partida.isFinPartida()[1]))
        else:
            print("Empate")


if __name__ == '__main__':
    main()
