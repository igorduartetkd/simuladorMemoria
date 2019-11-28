#processo.py


class Processo:
    id = 1

    def __init__(self, tamanho):
        self.__pid = Processo.id
        Processo.id += 1
        self.__tamanho = tamanho
        print("Processo {} criado".format(self.__pid))

    # GETTERS AND SETTERS
    def get_pid(self):
        return self.__pid

    def get_tamanho(self):
        return self.__tamanho

    def set_tamanho(self, tamanho):
        self.__tamanho = tamanho