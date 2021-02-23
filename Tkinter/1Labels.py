from tkinter import *

janela = Tk()

def  botao():
    n1 = int(caixa1.get())
    n2 = int(caixa2.get())
    soma =  str(n1 + n2)
    label1["text"] = "O rsultado da soma é  + soma

#width = janela.winfo_width()
#heigt = janela.winfo_height()

#janela.iconbitmap('stamp.ico')

label1 = Label(janela, text='Wellyngton Marcondes', font='Arial 20')
label1.place(x=100,y=80)

label2 = Label(janela, text='+', font='Arial 20')
label2.place(x=220,y=43)

botao1 = Button(janela, width=25, text='Botaozin', command=botao, background='#aaaaff')
botao1.place(x=150, y=150)

caixa1 = Entry(janela, width=20, background='#ffff00', font='Arial')
caixa1.place(x=30, y=50)

caixa2 = Entry(janela, width=20, background='#ffaa00', font='Arial')
caixa2.place(x=250, y=50)

janela.geometry('500x240')

mainloop()