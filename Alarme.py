import functools
import tkinter as t
from tkinter import messagebox
from tkinter import *
from tkinter.ttk import *


class Application2(t.Frame):
    def __init__(self, parent, nome, master=None):
        t.Frame.__init__(self, parent)
        self.nome = nome

        # ---------Áreas da aplicação--------

        self.primeiroContainer = Frame(self)
        self.primeiroContainer.pack()

        self.segundoContainer = Frame(self)
        self.segundoContainer.pack()

        self.terceiroContainer = Frame(self)
        self.terceiroContainer.pack()

        self.quartoContainer = Frame(self)
        self.quartoContainer.pack()

        self.lista = Listbox(self.terceiroContainer, width=80, height=15)
        self.lista.pack(side=RIGHT)

        # ---------Botões--------

        btnAdicionar = Button(self.primeiroContainer, text='➕ Adicionar', command=self.testeAdd)
        btnAdicionar.grid(row=5, column=3, padx=0, pady=3, ipadx=10, sticky=S)

        btnEditar = Button(self.primeiroContainer, text='✏️ Editar', command=self.edit)
        btnEditar.grid(row=5, column=4, padx=0, pady=3, ipadx=10)

        btnCopiar = Button(self.primeiroContainer, text='⚠️ Copiar', command=self.copy)
        btnCopiar.grid(row=5, column=5, padx=0, pady=3, ipadx=10)

        btnApagar = Button(self.primeiroContainer, text='❌ Apagar', command=self.testeDel)
        btnApagar.grid(row=5, column=6, padx=0, pady=3, ipadx=10)

        # ---------método da janela de novo alarme--------

    def abrir_janela(self):

        # ---------Configurações Básicas--------

        global janela2
        janela2 = Toplevel()
        janela2.title('Novo Dispertador')
        janela2.geometry("330x300")

        # ---------Criação de váriaveis textusais dos botões--------

        global Ddomingo, Dsegunda, Dterca, Dquarta, Dquinta, Dsexta, Dsabado
        Ddomingo = IntVar()
        Dsegunda = IntVar()
        Dterca = IntVar()
        Dquarta = IntVar()
        Dquinta = IntVar()
        Dsexta = IntVar()
        Dsabado = IntVar()

        # ---------Botões dias--------

        btnDomingo = Checkbutton(janela2, text='Domingo', variable=Ddomingo, onvalue=True, offvalue=False)
        btnDomingo.grid(row=0, column=0, padx=0, pady=1, ipadx=5, sticky=S)

        btnSegunda = Checkbutton(janela2, text='Segunda', variable=Dsegunda, onvalue=True, offvalue=False)
        btnSegunda.grid(row=0, column=1, padx=0, pady=1, ipadx=5)

        btnTerca = Checkbutton(janela2, text='Terça', variable=Dterca, onvalue=True, offvalue=False)
        btnTerca.grid(row=0, column=2, padx=0, pady=3, ipadx=10)

        btnQuarta = Checkbutton(janela2, text='Quarta', variable=Dquarta, onvalue=True, offvalue=False)
        btnQuarta.grid(row=1, column=0, padx=0, pady=3, ipadx=10)

        btnQuinta = Checkbutton(janela2, text='Quinta', variable=Dquinta, onvalue=True, offvalue=False)
        btnQuinta.grid(row=1, column=1, padx=0, pady=3, ipadx=10)

        btnSexta = Checkbutton(janela2, text='Sexta', variable=Dsexta, onvalue=True, offvalue=False)
        btnSexta.grid(row=1, column=2, padx=0, pady=3, ipadx=10)

        btnSabado = Checkbutton(janela2, text='Sabado', variable=Dsabado, onvalue=True, offvalue=False)
        btnSabado.grid(row=2, column=0, padx=0, pady=3, ipadx=10)

        # ---------Sistema para opções de escolha de horário--------

        horas = []
        for i in range(0, 25):
            if i < 10:
                horas.append((f"0{i}"))
            else:
                horas.append(i)

        minutos = []
        for i in range(0, 60):
            if i < 10:
                minutos.append((f"0{i}"))
            else:
                minutos.append(i)

        # ---------Texto de escolha--------

        Label(janela2, text="Selecione a Hora e Minuto :", font=("Times New Roman", 10)) \
            .grid(column=0, row=5, padx=10, pady=25)

        # ---------váriaveis globais de hora e minuto--------

        global Ehora, Eminutos

        # ---------Caixas de seleções tempo--------

        Hrs = StringVar()
        Ehora = Combobox(janela2, width=5, textvariable=Hrs)
        Ehora['values'] = horas
        Ehora.grid(row=5, column=1, padx=1, pady=2)

        Min = StringVar()
        Eminutos = Combobox(janela2, width=5, textvariable=Min)
        Eminutos['values'] = minutos
        Eminutos.grid(row=5, column=2, padx=1, pady=2)

        # ---------Botão de adicionar--------

        botao_add = Button(janela2, text='Adicionar Alarme', command=self.mostrar)
        botao_add.grid(row=20, column=0)

        # ---------função de adicionar as informações no novo alarme--------

    def mostrar(self):

        # ---------lista de dias--------

        diasMarcados = []

        # ---------seleções de dias possiveis--------

        if Ddomingo.get() == 1:
            diasMarcados.append("Domingo")
        if Dsegunda.get() == 1:
            diasMarcados.append("Segunda")
        if Dterca.get() == 1:
            diasMarcados.append("Terça")
        if Dquarta.get() == 1:
            diasMarcados.append("Quarta")
        if Dquinta.get() == 1:
            diasMarcados.append("Quinta")
        if Dsexta.get() == 1:
            diasMarcados.append("Sexta")
        if Dsabado.get() == 1:
            diasMarcados.append("Sabado")

        # ---------formatação de informações--------

        dd = (", ".join(map(str, diasMarcados)))
        hh = Ehora.get()
        mm = Eminutos.get()

        # ---------Sistema básico de tratamento de erros--------

        criacao = False

        if len(diasMarcados) == 0:
            alarme = "error - Dia não marcado"
            messagebox.showwarning("Error", "Dia não definido!", parent=janela2)

        elif hh == '':
            alarme = "error - Hora não marcada"
            messagebox.showwarning("Error", "Hora não definida!", parent=janela2)

        elif mm == '':
            alarme = "error - Minuto não definido"
            messagebox.showwarning("Error", "Minuto não definido!", parent=janela2)

        else:
            criacao = True
            alarme = f'{dd} | {hh}:{mm}'

        # ---------Criação final do alarme--------

        if criacao == True:
            self.lista.insert(1, alarme)
            janela2.destroy()

        # ---------Funções do botões princiapais--------

    def testeAdd(self):
        # self.abrir_janela()
        self.lista.insert(1, self.abrir_janela())

    def testeDel(self):
        for item in self.lista.curselection():
            self.lista.delete(item)

    def edit(self):
        for item in self.lista.curselection():
            self.lista.delete(item)
            self.lista.insert(str(item), self.abrir_janela())

    def copy(self):
        for item in self.lista.curselection():
            self.lista.insert('end', self.lista.get(item))

    def telaCron(self):
        print(1)

class Application3(t.Frame):
    def __init__(self, parent, nome, master=None):
        t.Frame.__init__(self, parent)
        self.nome = nome
        self.primeiroContainer = Frame(self)
        self.primeiroContainer.pack()
        t.Button(self.primeiroContainer, text='➕ 3').pack()

        btnAdicionar = Button(self.primeiroContainer, text='➕ Adicionar')
        btnAdicionar.pack(pady=3, ipadx=10)



class Application(t.Frame):
    def __init__(self, master=None, parent=None, *subtelas):
        t.Frame.__init__(self, parent)
        self.current_frame = self

        # ---------Áreas da aplicação--------

        self.primeiroContainer = Frame(master)
        self.primeiroContainer.pack()

        # ---------Botões--------

        btnCronometro = Button(self.primeiroContainer, text='Alarmes', command=self.muda_tela)
        btnCronometro.grid(row=7, column=6, padx=0, pady=3, ipadx=10)

        btnCronometro = Button(self.primeiroContainer, text='Cronometro', command=self.muda_tela2)
        btnCronometro.grid(row=7, column=7, padx=0, pady=3, ipadx=10)

    def muda_tela(self):
        self.current_frame.pack_forget()
        t1.pack()
        self.current_frame = t1

    def muda_tela2(self):
        self.current_frame.pack_forget()
        t2.pack()
        self.current_frame = t2

if __name__ == '__main__':
    root = Tk()
    root.resizable(0, 0)
    root.geometry("500x400")

    t1 = Application2(root, "pri")
    t2 = Application3(root, 'Segunda tela')

    m = Application(root, t1, t2)
    m.pack()

    root.mainloop()