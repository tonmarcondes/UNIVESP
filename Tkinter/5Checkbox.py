from tkinter import *

def funcao():
    if var_azul.get() == 1:
        l1['text'] = 'Azul'
    else:
        l1['text'] = ''

    if var_branco.get() == 1:
        l2['text'] = 'Branco'
    else:
        l2['text'] = ''

    if var_vermelho.get() == 1:
        l3['text'] = 'Vermelho'
    else:
        l3['text'] = ''

    if var_amarelo.get() == 1:
        l4['text'] = 'Amarelo'
    else:
        l4['text'] = ''

janela = Tk()

janela.iconbitmap('stamp.ico')
#janela.iconphoto(True, PhotoImage(file='stamp.png'))

janela.title('Teste')
janela.geometry('900x600+0+0')
janela.configure(background='#aaaaff')

l1 = Label(janela, text='', font='Arial 22', background='#aaaaff', foreground='#0000ff')
l1.place(x=200, y=50)
l2 = Label(janela, text='', font='Arial 22', background='#aaaaff', foreground='#ffffff')
l2.place(x=350, y=50)
l3 = Label(janela, text='', font='Arial 22', background='#aaaaff', foreground='#ff0000')
l3.place(x=500, y=50)
l4 = Label(janela, text='', font='Arial 22', background='#aaaaff', foreground='#ffff00')
l4.place(x=650, y=50)

var_azul = IntVar()
Checkbutton(janela, text='Azul', background='#aaaaff', variable=var_azul).place(x=300, y=200)

var_branco = IntVar()
Checkbutton(janela, text='Branco', background='#aaaaff', variable=var_branco).place(x=300, y=230)

var_vermelho = IntVar()
Checkbutton(janela, text='Vermelho', background='#aaaaff', variable=var_vermelho).place(x=300, y=260)

var_amarelo = IntVar()
Checkbutton(janela, text='Amarelo', background='#aaaaff', variable=var_amarelo).place(x=300, y=290)

Button(janela, text='Verifica Cor', command=funcao).place(x=300, y=350)

mainloop()