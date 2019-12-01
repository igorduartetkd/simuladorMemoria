#lacuna.py

from espacoMemoria import EspacoMemoria
from tipoEspaco import TipoEspaco


class Lacuna(EspacoMemoria):

    def __init__(self, tamanho, inicio, fim):
        super().__init__(TipoEspaco.LACUNA, inicio, fim, tamanho)

    #GETTERS AND SETTERS
    def set_inicio(self, inicio):
        self._inicio = inicio
        self.__update_tamanho()

    def set_fim(self, fim):
        self._fim = fim
        self.__update_tamanho()

    def __update_tamanho(self):
        self._tamanho = self._fim - self._inicio + 1
