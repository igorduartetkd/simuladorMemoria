#lacuna.py

class Lacuna:

    def __init__(self, tamanho, inicio, fim):
        if tamanho >= fim - inicio:
            print("Erro ao tentar alocar lacuna com tamanho {} no espaco de inicio {} e fim {}".format(tamanho, inicio, fim))
            raise NameError('Tamanho da lacuna maior que espaco para alocar')

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

