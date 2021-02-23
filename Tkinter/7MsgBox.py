from tkinter import *
from tkinter import messagebox

janela = Tk()

def soma():
    n1 = int(box1.get())
    n2 = int(box2.get())
    total = str(n1 + n2)
    label1['text'] = 'O resultado da soma é: '+ total 

    messagebox.showinfo('RESULTADO','A soma é: '+ total)

#janela.iconphoto(True, PhotoImage(file='stamp.png'))
janela.iconbitmap('stamp.ico')
janela.title('Box de mensagem')
janela.geometry('900x600+0+0')

box1 = Entry(janela, text='', font='Arial 18', background='#fcc', width='15')
box1.place(x=100, y=30)

box2 = Entry(janela, text='', font='Arial 18', background='#fcc', width='15')
box2.place(x=550, y=30)

label1 = Label(janela, text='Wellyngton Marcondes',font='Arial 20')
label1.place(x=300, y=170)

label2 = Label(janela, text='+',font='Arial 25')
label2.place(x=420, y=27)

Button(janela, text='Enviar', width='10', background='#ccf', command=soma).place(x=400, y=250)
mainloop()