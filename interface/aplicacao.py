from tkinter import *
from tkinter import ttk
from memoria import Memoria
from memoria import Metodo
from functools import partial
from tipoEspaco import TipoEspaco
from alocacao import Alocacao

class Aplicacao(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.master.title("Simulador de memoria")
        self.tela_inicial(parent)
        self.parent = parent
        self.tamanho = 0
        self.metodo = Metodo.FIRST_FIT


    def tela_inicial(self, parent):
        self.itens_tela_inicial = []
        self.container1 = Frame(parent)
        self.container1["pady"] = 10
        self.container1.pack()
        self.itens_tela_inicial.append(self.container1)

        self.container2 = Frame(parent)
        self.container2["pady"] = 20
        self.container2.pack()
        self.itens_tela_inicial.append(self.container2)

        self.container3 = Frame(parent)
        self.container3.pack()
        self.itens_tela_inicial.append(self.container3)

        self.container4 = Frame(parent)
        self.container4.pack()
        self.itens_tela_inicial.append(self.container4)

        self.msg1 = Label(self.container1, text="Criar memoria")
        self.msg1["font"] = ("Arial", "12", "bold")
        self.msg1.pack()
        self.itens_tela_inicial.append(self.msg1)

        self.msg2 = Label(self.container2, text="Tamanho")
        self.msg2.pack(side=LEFT)
        self.itens_tela_inicial.append(self.msg2)

        validacao = parent.register(self.is_number)
        self.gui_tamanho = Entry(self.container2, validate="key", validatecommand=(validacao, '%S'))
        self.gui_tamanho["width"] = 8
        self.gui_tamanho.pack(side=LEFT)
        self.itens_tela_inicial.append(self.gui_tamanho)

        self.msg22 = Label(self.container2, text="MB")
        self.msg22.pack(side=LEFT)
        self.itens_tela_inicial.append(self.msg22)

        self.msg2 = Label(self.container3, text="Algoritmo:")
        self.msg2.pack(side=LEFT)
        self.itens_tela_inicial.append(self.msg2)

        self.combo_algoritmo = ttk.Combobox(self.container3, values=["FIRST FIT",
                                                                     "NEXT FIT",
                                                                     "BEST FIT",
                                                                     "WORST FIT"])
        self.combo_algoritmo.set("FIRST FIT")
        self.combo_algoritmo.bind('<<ComboboxSelected>>', self.combo_selected)
        self.combo_algoritmo.pack(side=RIGHT)
        self.itens_tela_inicial.append(self.combo_algoritmo)

        self.criar = Button(self.container4)
        self.criar["text"] = "Criar"
        self.criar["width"] = 5
        self.criar["command"] = partial(self.criar_memoria, parent)
        self.criar.pack()
        self.itens_tela_inicial.append(self.criar)

    def tela_principal(self, parent):
        self.itens_tela_principal = []
        self.container1 = Frame(parent)
        self.container1["pady"] = 10
        self.container1["padx"] = 250
        self.container1.pack()
        self.itens_tela_principal.append(self.container1)

        self.container2 = Frame(parent)
        self.container2.pack()
        self.itens_tela_principal.append(self.container2)

        self.container21 = Frame(parent)
        self.container21.pack()
        self.itens_tela_principal.append(self.container21)

        self.container3 = Frame(parent)
        self.container3["pady"] = 50
        self.container3["padx"] = 250
        self.container3.pack()
        self.itens_tela_principal.append(self.container3)

        self.container4 = Frame(parent)
        self.container4["pady"] = 10
        self.container4["padx"] = 200
        self.container4.pack()
        self.itens_tela_principal.append(self.container4)

        self.container5 = Frame(parent)
        self.container5["pady"] = 10
        self.container5["padx"] = 200
        self.container5.pack()
        self.itens_tela_principal.append(self.container5)

        self.msg1 = Label(self.container1, text="Memoria {} MB".format(self.tamanho))
        self.msg1["font"] = ("Arial", "12", "bold")
        self.msg1.pack()
        self.itens_tela_principal.append(self.msg1)

        self.gerar_representacao()

        self.msg2 = Label(self.container3, text="Criar processo")
        self.msg2["font"] = ("Arial", "10", "bold")
        self.msg2.pack()
        self.itens_tela_principal.append(self.msg2)

        self.msg3 = Label(self.container3, text="Algoritmo: {}".format(Metodo.get_name(self.metodo)))
        self.msg3["font"] = ("Arial", "10")
        self.msg3.pack()
        self.itens_tela_principal.append(self.msg3)

        self.msg3 = Label(self.container4, text="tamanho: ")
        self.msg3.pack(side=LEFT)
        self.itens_tela_principal.append(self.msg3)

        validacao = parent.register(self.is_number)
        self.gui_tamanho = Entry(self.container4, validate="key", validatecommand=(validacao, '%S'))
        self.gui_tamanho["width"] = 10
        self.gui_tamanho.pack(side=LEFT)
        self.itens_tela_principal.append(self.gui_tamanho)

        self.msg4 = Label(self.container4, text="MB")
        self.msg4.pack(side=LEFT)
        self.itens_tela_inicial.append(self.msg4)

        self.criar = Button(self.container4)
        self.criar["text"] = "Criar"
        self.criar["width"] = 5
        self.criar["command"] = partial(self.criar_processo, parent)
        self.criar.pack(side=LEFT)
        self.itens_tela_principal.append(self.criar)

        self.voltar = Button(self.container5)
        self.voltar["text"] = "VOLTAR"
        self.voltar["width"] = 5
        self.voltar["command"] = partial(self.voltar_tela_inicial, parent)
        self.voltar.pack()
        self.itens_tela_principal.append(self.voltar)

    def criar_memoria(self, parent):
        tamanho = self.gui_tamanho.get()
        if tamanho:
            tamanho = int(tamanho)
            if tamanho > 0:
                self.tamanho = tamanho
                self.memoria = Memoria(tamanho, self.metodo)
                self.apagar_itens(self.itens_tela_inicial)
                self.tela_principal(parent)
            else:
                self.gui_tamanho.delete(0, 'end')

    def criar_processo(self, parent):
        try:
            tamanho = self.gui_tamanho.get()
            if tamanho:
                tamanho = int(tamanho)
                if tamanho > 0:
                    self.memoria.criar_processo(tamanho)
                    self.apagar_itens(self.itens_tela_principal)
                    self.tela_principal(parent)
                else:
                    self.gui_tamanho.delete(0, 'end')
        except NameError:
            self.popup_erro_processo()

    def voltar_tela_inicial(self, parent):
            del self.memoria
            self.apagar_itens(self.itens_tela_principal)
            self.tela_inicial(parent)

    def popupmsg(self, processo):
        msg = "Deseja remover o processo {}?".format(processo)
        self.popup = Tk()
        self.popup.wm_title("Remover Processo")
        label = Label(self.popup, text=msg)
        label.pack(side="top", pady=10)
        B1 = Button(self.popup, text="Sim")
        B1["command"] = partial(self.remover_processo, processo)
        B1.pack(side=LEFT)
        B2 = Button(self.popup, text="Nao", command=self.popup.destroy)
        B2.pack(side=RIGHT)
        self.popup.mainloop()

    def popup_erro_processo(self, ):
        msg = "Erro ao alocar espaco em memoria para o processo"
        self.popup = Tk()
        self.popup.wm_title("ERRO")
        label = Label(self.popup, text=msg)
        label.pack(side="top", pady=10)
        B2 = Button(self.popup, text="OK", command=self.popup.destroy)
        B2.pack()
        self.popup.mainloop()

    def gerar_representacao(self):
        tamanho = 100

        espacos = self.memoria.get_espacos_ordem()
        for espaco in espacos:
            self.e = Button(self.container2)
            if espaco.get_tipo() == TipoEspaco.ALOCACAO:
                self.e["text"] = "pid\n{}".format(espaco.get_processo().get_pid())
                self.e["background"] = "blue"
                self.e["command"] = lambda pid=espaco.get_processo().get_pid(): self.popupmsg(pid)
            else:
                self.e["background"] = "white"
            self.e["height"] = 5
            self.e["padx"] = 0
            width = int(tamanho * espaco.get_tamanho() / self.tamanho)
            if width == 0:
                width = 1
            self.e["width"] = width
            self.e.pack(side=LEFT)
            self.itens_tela_principal.append(self.e)

            self.t = Label(self.container21)
            self.t["text"] = "{}MB".format(espaco.get_tamanho())
            self.t["height"] = 1
            self.t["pady"] = 0
            self.t["padx"] = 2
            self.t["width"] = width
            self.t.pack(side=LEFT)
            self.itens_tela_principal.append(self.t)

    def remover_processo(self, pid):
        self.memoria.remover_processo(pid)
        self.apagar_itens(self.itens_tela_principal)
        self.tela_principal(root)
        self.popup.destroy()

    def apagar_itens(self, itens):
        for item in itens:
            item.pack_forget()

    def is_number(self, string):
        return string.isdigit()

    def combo_selected(self, event=None):
        metodo = self.combo_algoritmo.get()
        if metodo == 'FIRST FIT':
            self.metodo = Metodo.FIRST_FIT
        elif metodo == 'NEXT FIT':
            self.metodo = Metodo.NEXT_FIT
        elif metodo == 'BEST FIT':
            self.metodo = Metodo.BEST_FIT
        elif metodo == 'WORST FIT':
            self.metodo = Metodo.WORST_FIT



if __name__ == '__main__':
    root = Tk()
    root.geometry("900x600")
    root.resizable(0, 0)
    aplicacao = Aplicacao(root)
    root.mainloop()