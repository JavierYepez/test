class Tablero():

    _marcasIniciales = (0, 0, 0, 0, 0, 0, 0, 0, 0)

    def __init__(self):
        self._marcas = list(self._marcasIniciales)

    def marcarCasilla(self, jugador, posicion):
        if jugador == 1:
            marca = 1
        elif jugador == 2:
            marca = 2
        else:
            raise ValueError("Este jugador no existe", jugador)
        if self._marcas[posicion] != 0:
            return True
        else:
            self._marcas[posicion] = marca
            return False

    def imprimir(self):
        print("-----------")
        for i in range(0, 9, 3):
            self._casillasMarcadas(self._marcas[i:i+3])
        else:
            print("-----------")

    def _casillasMarcadas(self, marcas):
        print("|", end="")
        for i in range(3):
            print(" "+str(marcas[i]), end=" ")
        else:
            print("|")

    def limpiarTablero(self):
        self._marcas = list(self._marcasIniciales)

    @property
    def marcas(self):
        return tuple(self._marcas)


class Partida():
    __tablero = Tablero()

    def __init__(self):
        self._turno = 1

    def isFinPartida(self):
        if self.__tablero.marcas.count(1) < 3 \
                and self.__tablero.marcas.count(2) < 3:
            return False
        else:
            for jugador in (1, 2):
                for i in range(0, 9, 3):
                    if self._isTresEnRaya(jugador,
                                          self.__tablero.marcas[i:i+3]):
                        return True, jugador
                for i in range(0, 3):
                    if self._isTresEnRaya(jugador,
                                          self.__tablero.marcas[i::3]):
                        return True, jugador
                if self._isTresEnRaya(jugador,
                                      self.__tablero.marcas[0::4]):
                    return True, jugador
                if self._isTresEnRaya(jugador,
                                      self.__tablero.marcas[2:7:2]):
                    return True, jugador
            else:
                return False

    def _isTresEnRaya(self, jugador, linea):
        if linea.count(jugador) == 3:
            return True
        else:
            return False

    def marcarCasilla(self, casilla):
        if not self.__tablero.marcarCasilla(self._turno, casilla):
            if self._turno == 1:
                self._turno = 2
            else:
                self._turno = 1
        else:
            # TODO: añadir error
            pass

    def refresco(self):
        self.__tablero.imprimir()

    @property
    def turno(self):
        return self._turno
