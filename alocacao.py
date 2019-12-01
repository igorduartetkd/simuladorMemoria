#alocacao.py
from espacoMemoria import EspacoMemoria
from tipoEspaco import TipoEspaco

class Alocacao(EspacoMemoria):

    def __init__(self, processo):
        super(Alocacao, self).__init__(TipoEspaco.ALOCACAO, 0, 0, processo.get_tamanho())
        self.__processo = processo

    #GETTERS AND SETTERS
    def get_processo(self):
        return self.__processo

    def set_inicio(self, inicio):
        self._inicio = inicio
        self.__update_fim()

    def __update_fim(self):
        self._fim = self._inicio + self.__processo.get_tamanho() - 1

