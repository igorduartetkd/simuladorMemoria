from memoria import Memoria
from metodo import Metodo
from espacoMemoria import EspacoMemoria
from tipoEspaco import TipoEspaco
import unittest


class MemoriaTest(unittest.TestCase):
    def get_memoria(self, metodo):
        memoria = Memoria(200, metodo)
        pids = list()
        pids.append(memoria.criar_processo(10))  # 0
        pids.append(memoria.criar_processo(20))  # 1
        pids.append(memoria.criar_processo(30))  # 2
        pids.append(memoria.criar_processo(40))  # 3
        pids.append(memoria.criar_processo(40))  # 4
        pids.append(memoria.criar_processo(30))  # 5
        pids.append(memoria.criar_processo(20))  # 6
        pids.append(memoria.criar_processo(10))  # 7
        return memoria, pids

    def get_msg_erro(self, esperado, obtido):
        return 'Processo nao foi alocado na posicao correta: esperado: {} | obtido: {}'.format(esperado, obtido)

    def test_first_fit(self):
        memoria, pids = self.get_memoria(Metodo.FIRST_FIT)
        memoria.remover_processo(pids[3])
        memoria.criar_processo(40)
        memoria.remover_processo(pids[1])
        memoria.remover_processo(pids[5])
        pid = memoria.criar_processo(20)
        alocacoes = memoria.get_alocacoes()
        alocacoes = [a for a in alocacoes if a.get_processo().get_pid() == pid]
        assert len(alocacoes) == 1 , 'Processo nao foi encontrado nas alocacoes'
        alocacao = alocacoes[0]
        pos_esperada = 11
        mensagem_erro = self.get_msg_erro(pos_esperada, alocacao.get_inicio())
        assert alocacao.get_inicio() == pos_esperada, mensagem_erro


    def test_first_fit_2(self):
        memoria = Memoria(20, Metodo.FIRST_FIT)
        memoria.criar_processo(1)
        memoria.criar_processo(2)
        memoria.criar_processo(3)
        memoria.criar_processo(4)
        memoria.remover_processo(1)
        pid = memoria.criar_processo(1)
        alocacoes = memoria.get_alocacoes()
        alocacoes = [a for a in alocacoes if a.get_processo().get_pid() == pid]
        assert len(alocacoes) == 1 , 'Processo nao foi encontrado nas alocacoes'
        alocacao = alocacoes[0]
        pos_esperada = 2
        mensagem_erro = self.get_msg_erro(pos_esperada, alocacao.get_inicio())
        assert alocacao.get_inicio() == pos_esperada, mensagem_erro

    def test_next_fix(self):
        memoria,pids = self.get_memoria(Metodo.NEXT_FIT)
        memoria.remover_processo(pids[0])
        memoria.remover_processo(pids[2])
        memoria.remover_processo(pids[4])
        memoria.remover_processo(pids[7])
        memoria.remover_processo(pids[5])
        memoria.criar_processo(70)
        pid = memoria.criar_processo(10)
        alocacoes = memoria.get_alocacoes()
        alocacoes = [a for a in alocacoes if a.get_processo().get_pid() == pid]
        assert len(alocacoes) == 1, 'Processo nao foi encontrado nas alocacoes'
        alocacao = alocacoes[0]
        pos_esperada = 191
        mensagem_erro = self.get_msg_erro(pos_esperada, alocacao.get_inicio())
        assert alocacao.get_inicio() == pos_esperada, mensagem_erro


    def test_best_fit(self):
        memoria,pids = self.get_memoria(Metodo.BEST_FIT)
        memoria.remover_processo(pids[1])
        memoria.remover_processo(pids[2])
        memoria.remover_processo(pids[3])
        memoria.remover_processo(pids[5])
        memoria.remover_processo(pids[6])
        pid = memoria.criar_processo(50)
        alocacoes = memoria.get_alocacoes()
        alocacoes = [a for a in alocacoes if a.get_processo().get_pid() == pid]
        assert len(alocacoes) == 1, 'Processo nao foi encontrado nas alocacoes'
        alocacao = alocacoes[0]
        pos_esperada = 141
        mensagem_erro = self.get_msg_erro(pos_esperada, alocacao.get_inicio())
        assert alocacao.get_inicio() == pos_esperada, mensagem_erro



    def test_worst_fit(self):
        memoria,pids = self.get_memoria(Metodo.WORST_FIT)
        memoria.remover_processo(pids[1])
        memoria.remover_processo(pids[2])
        memoria.remover_processo(pids[4])
        memoria.remover_processo(pids[5])
        memoria.remover_processo(pids[6])
        pid = memoria.criar_processo(50)
        alocacoes = memoria.get_alocacoes()
        alocacoes = [a for a in alocacoes if a.get_processo().get_pid() == pid]
        assert len(alocacoes) == 1, 'Processo nao foi encontrado nas alocacoes'
        alocacao = alocacoes[0]
        pos_esperada = 101
        mensagem_erro = self.get_msg_erro(pos_esperada, alocacao.get_inicio())
        assert alocacao.get_inicio() == pos_esperada, mensagem_erro

    def test_get_espacos_ordem(self):
        memoria, pids = self.get_memoria(Metodo.FIRST_FIT)
        memoria.remover_processo(pids[1])
        memoria.remover_processo(pids[7])
        espacos = memoria.get_espacos_ordem()
        assert len(espacos) == 8, 'Quantidade de espacos incorreta'
        assert espacos[0].get_tipo() == TipoEspaco.ALOCACAO, 'Esperado uma alocacao obtido uma lacuna'
        assert espacos[1].get_tipo() == TipoEspaco.LACUNA, 'Esperado uma lacuna obtido uma alocacao'
        assert espacos[6].get_tipo() == TipoEspaco.ALOCACAO, 'Esperado uma alocacao obtido uma lacuna'
        assert espacos[7].get_tipo() == TipoEspaco.LACUNA, 'Esperado uma lacuna obtido uma alocacao'


