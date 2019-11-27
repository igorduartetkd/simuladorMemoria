#alocacao.py
from processo import Processo

class Alocacao:

    def __init__(self, processo):
        self.__processo = processo
        self.__inicio = 0
        self.__fim = 0

    #GETTERS AND SETTERS
    def get_processo(self):
        return self.__processo

    def get_inicio(self):
        return self.__inicio

    def get_fim(self):
        return self.__fim

    def set_inicio(self, inicio):
        self.__inicio = inicio

    def set_fim(self, fim):
        self.__fim = fim

