# espaco_memoria

class EspacoMemoria:
    def __init__(self, tipo, inicio, fim, tamanho):
        self._tipo = tipo
        self._inicio = inicio
        self._fim = fim
        self._tamanho = tamanho

    def get_tipo(self):
        return self._tipo

    def get_inicio(self):
        return self._inicio

    def get_fim(self):
        return self._fim

    def get_tamanho(self):
        return self._tamanho
