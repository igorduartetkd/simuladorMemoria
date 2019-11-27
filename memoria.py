#memoria.py

from alocacao import Alocacao
from processo import Processo
from metodo import Metodo
from lacuna import Lacuna


class Memoria:

    def __init__(self, tamanho, metodo):
        self.__tamanho = tamanho
        self.__metodo = metodo
        self.__alocacoes = []
        try:
            lacuna = Lacuna(tamanho, 1, tamanho)
        except NameError:
            raise
        self.__lacunas = [lacuna]

    # GETTERS AND SETTERS

    def get_tamanho(self):
        return self.__tamanho

    def get_metodo(self):
        return self.__metodo

    def get_alocacoes(self):
        return self.__alocacoes

    def get_lacunas(self):
        return self.__lacunas

    def get_porcentagem_uso(self):
        tamanhos = sum([alocacao.get_processo().get_tamanho() for alocacao in self.__alocacoes])
        return tamanhos * 100 / self.__tamanho

    # FUNCOES

    def criar_processo(self, tamanho):
        processo = Processo(tamanho)
        alocacao = Alocacao(processo)
        if self.__metodo == Metodo.FIRST_FIT:
            self.__first_fit(alocacao)
        elif self.__metodo == Metodo.NEXT_FIT:
            self.__next_fit(alocacao)
        elif self.__metodo == Metodo.BEST_FIT:
            self.__best_fit(alocacao)
        elif self.__metodo == Metodo.WORST_FIT:
            self.__worst_fit(alocacao)

    def remover_processo(self, pid):
        index = [self.__alocacoes.index(a) for a in self.__alocacoes if a.get_processo().get_pid() == pid]
        if index:
            del self.__alocacoes[index[0]]
            print("Processo {} removido".format(pid))
        else:
            print("Processo {} inexistente".format(pid))

    # IMPLEMENTACAO DOS ALGORITMOS

    def __first_fit(self, alocacao):
        return

    def __next_fit(self, alocacao):
        return

    def __best_fit(self, alocacao):
        return

    def __worst_fit(self, alocacao):
        return