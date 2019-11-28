# memoria.py

from alocacao import Alocacao
from processo import Processo
from metodo import Metodo
from lacuna import Lacuna


class Memoria:

    def __init__(self, tamanho, metodo):
        self.__tamanho = tamanho
        self.__metodo = metodo
        self.__alocacoes = []
        lacuna = Lacuna(tamanho, 1, tamanho)
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
        try:
            if self.__metodo == Metodo.FIRST_FIT:
                self.__first_fit(alocacao)
            elif self.__metodo == Metodo.NEXT_FIT:
                self.__next_fit(alocacao)
            elif self.__metodo == Metodo.BEST_FIT:
                self.__best_fit(alocacao)
            elif self.__metodo == Metodo.WORST_FIT:
                self.__worst_fit(alocacao)
        except NameError:
            raise

        return processo.get_pid()

    def remover_processo(self, pid):
        index = [self.__alocacoes.index(a) for a in self.__alocacoes if a.get_processo().get_pid() == pid]
        if index:
            self.__gerar_lacunas(self.__alocacoes[index[0]])
            del self.__alocacoes[index[0]]
            print("Processo {} removido".format(pid))
        else:
            print("Processo {} inexistente".format(pid))

    # IMPLEMENTACAO DOS ALGORITMOS

    def __first_fit(self, alocacao):
        indice_lacuna = -1
        for lacuna in self.__lacunas:
            if lacuna.get_tamanho() >= alocacao.get_processo().get_tamanho():
                alocacao.set_inicio(lacuna.get_inicio())
                self.__alocacoes.append(alocacao)
                lacuna.set_inicio(alocacao.get_fim() + 1)
                indice_lacuna = self.__lacunas.index(lacuna)
                break
        if indice_lacuna == -1:
            raise NameError('Espaco insuficiente na memoria')
        if self.__lacunas[indice_lacuna].get_tamanho() <= 0:
            del self.__lacunas[indice_lacuna]

    def __next_fit(self, alocacao):
        return

    def __best_fit(self, alocacao):
        return

    def __worst_fit(self, alocacao):
        return

    # AUXILIARES
    def __gerar_lacunas(self, alocacao):
        ind_ini = [self.__lacunas.index(i) for i in self.__lacunas if i.get_fim() == alocacao.get_inicio() - 1]
        ind_fim = [self.__lacunas.index(i) for i in self.__lacunas if i.get_inicio() - 1 == alocacao.get_fim()]
        if ind_ini and ind_fim:
            self.__lacunas[ind_ini[0]].set_fim(self.__lacunas[ind_fim[0]].get_fim())
            del self.__lacunas[ind_fim[0]]
        elif ind_ini and not ind_fim:
            self.__lacunas[ind_ini[0]].set_fim(alocacao.get_fim())
        elif not ind_ini and ind_fim:
            self.__lacunas[ind_fim[0]].set_inicio(alocacao.get_inicio())
        else:
            self.__lacunas.append(Lacuna(alocacao.get_processo().get_tamanho(),
                                         alocacao.get_inicio(),
                                         alocacao.get_fim()))


memoria = Memoria(10, Metodo.FIRST_FIT)
memoria.criar_processo(1)
memoria.criar_processo(4)
memoria.criar_processo(5)
print([(alocacao.get_inicio(), alocacao.get_fim(), alocacao.get_processo().get_pid()) for alocacao in memoria.get_alocacoes()])
print([(lacuna.get_inicio(), lacuna.get_fim(), lacuna.get_tamanho()) for lacuna in memoria.get_lacunas()])
memoria.remover_processo(2)
print([(alocacao.get_inicio(), alocacao.get_fim(), alocacao.get_processo().get_pid()) for alocacao in memoria.get_alocacoes()])
print([(lacuna.get_inicio(), lacuna.get_fim(), lacuna.get_tamanho()) for lacuna in memoria.get_lacunas()])
memoria.criar_processo(3)
print([(alocacao.get_inicio(), alocacao.get_fim(), alocacao.get_processo().get_pid()) for alocacao in memoria.get_alocacoes()])
print([(lacuna.get_inicio(), lacuna.get_fim(), lacuna.get_tamanho()) for lacuna in memoria.get_lacunas()])