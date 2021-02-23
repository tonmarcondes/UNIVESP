from tkinter import *

janela = Tk()

def funcao1():
    label_1['foreground'] = '#00f'

def funcao2():
    label_1['foreground'] = '#f00'

def funcao3():
    label_1['foreground'] = '#0f0'

def funcao4():
    label_1['foreground'] = '#ff0'

janela.title('Menus')
janela.iconbitmap('stamp.ico')
janela.geometry('500x500+0+0')

label_1 = Label(janela, text='Mude a cor no menu', font='Arial 25', foreground='#000')
label_1.place(x=80, y=150)

m = Menubutton(janela, text='Meu menu', font='Arial 20', background='#fff')
m.place(x=260, y=30)
m.menu = Menu(m)
m['menu'] = m.menu

m.menu.add_command(label='Azul', command=funcao1)
m.menu.add_command(label='Vermelho', command=funcao2)
m.menu.add_command(label='verde', command=funcao3)
m.menu.add_command(label='Amarelo', command=funcao4)

m.place(x=180, y=10)
mainloop()
