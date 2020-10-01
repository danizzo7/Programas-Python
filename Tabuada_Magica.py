from tkinter import *
from Constantes import *
import os

raiz = Tk()
valor = 0

class Janela:
    def __init__(self, raiz):
        self.fr1 = Frame(raiz, background = cinza1)
        self.fr1.pack()
        self.fr2 = Frame(raiz, background = cinza1)
        self.fr2.pack()
        self.fr3 = Frame(raiz, background = cinza1)
        self.fr3.pack()
        self.fr4 = Frame(raiz, background = cinza1)
        self.fr4.pack()
        self.fr5 = Frame(raiz, background=cinza1)
        self.fr5.pack()
        self.fr6 = Frame(raiz, background=cinza1)
        self.fr6.pack()
        self.fr7 = Frame(raiz, background=cinza1)
        self.fr7.pack()
        self.fr8 = Frame(raiz, background=cinza1)
        self.fr8.pack()
        self.fr9 = Frame(raiz, background=cinza1)
        self.fr9.pack()
        self.fr10 = Frame(raiz, background=cinza1)
        self.fr10.pack()
        self.fr11 = Frame(raiz, background=cinza1)
        self.fr11.pack()
        self.fr12 = Frame(raiz, background=cinza1)
        self.fr12.pack()
        self.fr13 = Frame(raiz, background=cinza1)
        self.fr13.pack()
        self.fr14 = Frame(raiz, background=cinza1)
        self.fr14.pack()

        self.lb1 = Label(self.fr1, text="TABUADA MAGICA", background=azul_claro, font=fonte1,
                         fg=azul2, pady=10)
        self.lb1.pack()
        self.lb2 = Label(self.fr2, text="Digite o valor base para a Tabuada : ", background=azul_claro, font=fonte2,
                         fg=azul2, pady=10)
        self.lb2.pack(side=LEFT)

        self.num = Entry(self.fr3, font=fonte3, width=3)
        self.num.pack(side=LEFT)

        self.lb_separador = Label(self.fr3, text="        ", bg=azul2, font=fonte3)
        self.lb_separador.pack(side=LEFT)

        self.bt_jogar = Button(self.fr3, text="CALCULAR", bg=cinza2, font=1, widt=10
                               , relief=RAISED, border=8, command=self.jogar)
        self.bt_jogar.bind("<Return>", self.jogar2)
        self.bt_jogar.focus_force()
        self.bt_jogar.pack(side=LEFT)

        self.lb_erro= Label(self.fr14, text="",font=fonte4,bg=cinza1, fg=vermelho)
        self.lb_erro.pack()

        #================1===================
        self.escolha1 =  Label(self.fr4, text="  ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10,width=3, height=1)
        self.escolha1.pack(side=LEFT)

        self.lbx1 = Label(self.fr4, text=" X ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10,width=3, height=1)
        self.lbx1.pack(side=LEFT)
        self.valor1 = 1
        self.mostra_valor1 = Label(self.fr4, background=azul_claro, font=fonte2,
                         fg=azul2, pady=10,height=1)
        self.mostra_valor1.pack(side=LEFT)
        self.mostra_valor1["text"] = str(self.valor1)

        self.lbigual1 = Label(self.fr4, text=" = ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10, width=3, height=1)
        self.lbigual1.pack(side=LEFT)

        self.result1 = Label(self.fr4, text="  ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=5, height=1)
        self.result1.pack(side=LEFT)

        # ================2===================
        self.escolha2 = Label(self.fr5, text="  ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.escolha2.pack(side=LEFT)

        self.lbx1 = Label(self.fr5, text=" X ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10,width=3, height=1)
        self.lbx1.pack(side=LEFT)

        self.valor1 = 2
        self.mostra_valor1 = Label(self.fr5, background=azul_claro, font=fonte2,
                                   fg=azul2, pady=10, height=1)
        self.mostra_valor1.pack(side=LEFT)
        self.mostra_valor1["text"] = str(self.valor1)

        self.lbigual1 = Label(self.fr5, text=" = ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.lbigual1.pack(side=LEFT)

        self.result2 = Label(self.fr5, text="  ", background=azul_claro, font=fonte2,
                            fg=azul2, pady=10, width=5, height=1)
        self.result2.pack(side=LEFT)

        # ================3===================
        self.escolha3 = Label(self.fr6, text="  ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3,height=1 )
        self.escolha3.pack(side=LEFT)

        self.lbx1 = Label(self.fr6, text=" X ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10,width=3, height=1)
        self.lbx1.pack(side=LEFT)

        self.valor1 = 3
        self.mostra_valor1 = Label(self.fr6, background=azul_claro, font=fonte2,
                                   fg=azul2, pady=10, height=1)
        self.mostra_valor1.pack(side=LEFT)
        self.mostra_valor1["text"] = str(self.valor1)

        self.lbigual1 = Label(self.fr6, text=" = ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.lbigual1.pack(side=LEFT)

        self.result3 = Label(self.fr6, text="  ", background=azul_claro, font=fonte2,
                            fg=azul2, pady=10, width=5, height=1)
        self.result3.pack(side=LEFT)
        # ================4===================
        self.escolha4 = Label(self.fr7, text="  ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.escolha4.pack(side=LEFT)

        self.lbx1 = Label(self.fr7, text=" X ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10,width=3, height=1)
        self.lbx1.pack(side=LEFT)

        self.valor1 = 4
        self.mostra_valor1 = Label(self.fr7, background=azul_claro, font=fonte2,
                                   fg=azul2, pady=10, height=1)
        self.mostra_valor1.pack(side=LEFT)
        self.mostra_valor1["text"] = str(self.valor1)

        self.lbigual1 = Label(self.fr7, text=" = ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.lbigual1.pack(side=LEFT)

        self.result4 = Label(self.fr7, text="  ", background=azul_claro, font=fonte2,
                             fg=azul2, pady=10, width=5, height=1)
        self.result4.pack(side=LEFT)

        # ================5===================
        self.escolha5 = Label(self.fr8, text="  ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.escolha5.pack(side=LEFT)

        self.lbx1 = Label(self.fr8, text=" X ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10,width=3, height=1)
        self.lbx1.pack(side=LEFT)

        self.valor1 = 5
        self.mostra_valor1 = Label(self.fr8, background=azul_claro, font=fonte2,
                                   fg=azul2, pady=10, height=1)
        self.mostra_valor1.pack(side=LEFT)
        self.mostra_valor1["text"] = str(self.valor1)

        self.lbigual1 = Label(self.fr8, text=" = ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.lbigual1.pack(side=LEFT)

        self.result5 = Label(self.fr8, text="  ", background=azul_claro, font=fonte2,
                             fg=azul2, pady=10, width=5, height=1)
        self.result5.pack(side=LEFT)
    # ================6===================
        self.escolha6 = Label(self.fr9, text="  ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.escolha6.pack(side=LEFT)

        self.lbx1 = Label(self.fr9, text=" X ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10, width=3, height=1)
        self.lbx1.pack(side=LEFT)

        self.valor1 = 6
        self.mostra_valor1 = Label(self.fr9, background=azul_claro, font=fonte2,
                                   fg=azul2, pady=10, height=1)
        self.mostra_valor1.pack(side=LEFT)
        self.mostra_valor1["text"] = str(self.valor1)

        self.lbigual1 = Label(self.fr9, text=" = ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.lbigual1.pack(side=LEFT)

        self.result6 = Label(self.fr9, text="  ", background=azul_claro, font=fonte2,
                             fg=azul2, pady=10, width=5, height=1)
        self.result6.pack(side=LEFT)

    # ================7===================
        self.escolha7 = Label(self.fr10, text="  ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.escolha7.pack(side=LEFT)

        self.lbx1 = Label(self.fr10, text=" X ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10,width=3, height=1)
        self.lbx1.pack(side=LEFT)

        self.valor1 = 7
        self.mostra_valor1 = Label(self.fr10, background=azul_claro, font=fonte2,
                                   fg=azul2, pady=10, height=1)
        self.mostra_valor1.pack(side=LEFT)
        self.mostra_valor1["text"] = str(self.valor1)

        self.lbigual1 = Label(self.fr10, text=" = ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.lbigual1.pack(side=LEFT)

        self.result7 = Label(self.fr10, text="  ", background=azul_claro, font=fonte2,
                             fg=azul2, pady=10, width=5, height=1)
        self.result7.pack(side=LEFT)

    # ================8===================
        self.escolha8 = Label(self.fr11, text="  ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.escolha8.pack(side=LEFT)

        self.lbx1 = Label(self.fr11, text=" X ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10,width=3, height=1)
        self.lbx1.pack(side=LEFT)

        self.valor1 = 8
        self.mostra_valor1 = Label(self.fr11, background=azul_claro, font=fonte2,
                                   fg=azul2, pady=10, height=1)
        self.mostra_valor1.pack(side=LEFT)
        self.mostra_valor1["text"] = str(self.valor1)

        self.lbigual1 = Label(self.fr11, text=" = ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.lbigual1.pack(side=LEFT)

        self.result8 = Label(self.fr11, text="  ", background=azul_claro, font=fonte2,
                             fg=azul2, pady=10, width=5, height=1)
        self.result8.pack(side=LEFT)
    # ================9===================
        self.escolha9 = Label(self.fr12, text="  ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.escolha9.pack(side=LEFT)

        self.lbx1 = Label(self.fr12, text=" X ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10,width=3, height=1)
        self.lbx1.pack(side=LEFT)

        self.valor1 = 9
        self.mostra_valor1 = Label(self.fr12, background=azul_claro, font=fonte2,
                                   fg=azul2, pady=10, height=1)
        self.mostra_valor1.pack(side=LEFT)
        self.mostra_valor1["text"] = str(self.valor1)

        self.lbigual1 = Label(self.fr12, text=" = ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.lbigual1.pack(side=LEFT)

        self.result9 = Label(self.fr12, text="  ", background=azul_claro, font=fonte2,
                             fg=azul2, pady=10, width=5, height=1)
        self.result9.pack(side=LEFT)

    # ================10===================
        self.escolha10 = Label(self.fr13, text="  ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.escolha10.pack(side=LEFT)

        self.lbx1 = Label(self.fr13, text=" X ", background=azul_claro, font=fonte2,
                          fg=azul2, pady=10,width=3, height=1)
        self.lbx1.pack(side=LEFT)
        self.valor1 = 10
        self.mostra_valor1 = Label(self.fr13, background=azul_claro, font=fonte2,
                                   fg=azul2, pady=10, height=1)
        self.mostra_valor1.pack(side=LEFT)
        self.mostra_valor1["text"] = str(self.valor1)

        self.lbigual1 = Label(self.fr13, text=" = ", background=azul_claro, font=fonte2,
                              fg=azul2, pady=10, width=3, height=1)
        self.lbigual1.pack(side=LEFT)

        self.result10 = Label(self.fr13, text="  ", background=azul_claro, font=fonte2,
                             fg=azul2, pady=10, width=5, height=1)
        self.result10.pack(side=LEFT)

    def jogar(self):

        try:
            self.lb_erro["text"] = ""
            num = int(self.num.get())

            if num >= 1 and num <= 10:
                self.escolha1["text"] = num
                self.result1["text"] = int(num * 1)
                self.escolha2["text"] = num
                self.result2["text"] = int(num * 2)
                self.escolha3["text"] = num
                self.result3["text"] = int(num * 3)
                self.escolha4["text"] = num
                self.result4["text"] = int(num * 4)
                self.escolha5["text"] = num
                self.result5["text"] = int(num * 5)
                self.escolha6["text"] = num
                self.result6["text"] = int(num * 6)
                self.escolha7["text"] = num
                self.result7["text"] = int(num * 7)
                self.escolha8["text"] = num
                self.result8["text"] = int(num * 8)
                self.escolha9["text"] = num
                self.result9["text"] = int(num * 9)
                self.escolha10["text"] =num
                self.result10["text"] = int(num * 10)

            else:
                self.lb_erro["text"] = "Digite apenas números de 1 a 10"
        except:
            self.lb_erro["text"] = "Digite apenas NUMEROS de 1 a 10"

    def jogar2(self, event):

        try:
            self.lb_erro["text"] = ""
            num = int(self.num.get())

            if num >= 1 and num <= 10:
                self.escolha1["text"] = num
                self.result1["text"] = int(num * 1)
                self.escolha2["text"] = num
                self.result2["text"] = int(num * 2)
                self.escolha3["text"] = num
                self.result3["text"] = int(num * 3)
                self.escolha4["text"] = num
                self.result4["text"] = int(num * 4)
                self.escolha5["text"] = num
                self.result5["text"] = int(num * 5)
                self.escolha6["text"] = num
                self.result6["text"] = int(num * 6)
                self.escolha7["text"] = num
                self.result7["text"] = int(num * 7)
                self.escolha8["text"] = num
                self.result8["text"] = int(num * 8)
                self.escolha9["text"] = num
                self.result9["text"] = int(num * 9)
                self.escolha10["text"] =num
                self.result10["text"] = int(num * 10)

            else:
                self.lb_erro["text"] = "Digite apenas números de 1 a 10"
        except:
            self.lb_erro["text"] = "Digite apenas NUMEROS de 1 a 10"


#raiz.geometry("840x650+300+30")
raiz.geometry("840x700+300+10")
raiz.iconbitmap("imagens/Tab.ico")
raiz.title("Tabuada Mágica")
raiz["background"] = azul2

janela = Janela(raiz)

raiz.mainloop()
