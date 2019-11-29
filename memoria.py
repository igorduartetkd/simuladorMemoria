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
        self.__aux_next = 0

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
            tam = self.__alocacoes[index[0]].get_processo().get_tamanho()
            del self.__alocacoes[index[0]]
            print("Processo {} removido. Tamanho: {}".format(pid, tam))
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
        i_lacunas_adequadas = [self.__lacunas.index(lacuna) for lacuna in self.__lacunas if lacuna.get_tamanho() >= alocacao.get_processo().get_tamanho()]

        if i_lacunas_adequadas:
            distancias = {i: self.__lacunas[i].get_inicio() - self.__aux_next for i in i_lacunas_adequadas}  # calculando distancias de onde parou
            distancias_negativas = {k: v + self.__tamanho for k, v in distancias.items() if v < 0}  # removendo valores negativos
            distancias = {k: v for k, v in distancias.items() if v >= 0}  # removendo valores negativos
            distancias.update(distancias_negativas)
            i = min(distancias, key=distancias.get) # pegando a lacuna mais proxima que cabe
            alocacao.set_inicio(self.__lacunas[i].get_inicio())
            self.__alocacoes.append(alocacao)
            self.__lacunas[i].set_inicio(alocacao.get_fim() + 1)
            if self.__lacunas[i].get_tamanho() <= 0:
                del self.__lacunas[i]
            self.__aux_next = alocacao.get_inicio()
        else:
            raise NameError('Espaco insuficiente na memoria')


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
