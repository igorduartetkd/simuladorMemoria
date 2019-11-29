#processo.py


class Processo:
    id = 0

    def __init__(self, tamanho):
        self.__pid = Processo.id
        Processo.id += 1
        self.__tamanho = tamanho
        print("Processo {} criado. Tamanho: {}".format(self.__pid, self.__tamanho))

    # GETTERS AND SETTERS
    def get_pid(self):
        return self.__pid

    def get_tamanho(self):
        return self.__tamanho

    def set_tamanho(self, tamanho):
        self.__tamanho = tamanho