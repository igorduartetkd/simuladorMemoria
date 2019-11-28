#lacuna.py

class Lacuna:

    def __init__(self, tamanho, inicio, fim):
        self.__tamanho = tamanho
        self.__inicio = inicio
        self.__fim = fim

    #GETTERS AND SETTERS
    def get_tamanho(self):
        return self.__tamanho

    def get_inicio(self):
        return self.__inicio

    def get_fim(self):
        return self.__fim

    def set_inicio(self, inicio):
        self.__inicio = inicio
        self.__update_tamanho()

    def set_fim(self, fim):
        self.__fim = fim
        self.__update_tamanho()

    def __update_tamanho(self):
        self.__tamanho = self.__fim - self.__inicio + 1
