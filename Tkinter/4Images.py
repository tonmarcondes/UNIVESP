from tkinter import *

janela = Tk()

janela.iconbitmap('stamp.ico')
#janela.iconphoto(True, PhotoImage(file=('stamp.png')))

imagem3 = PhotoImage(file='gramado.png')
gramado = Label(janela, image=imagem3)
gramado.place(x=10, y=10)

imagem1 = PhotoImage(file='bola.png')
bola = Label(janela, image=imagem1)
bola.place(x=10, y=10)

imagem2 = PhotoImage(file='fusca.png')
fusca = Label(janela, image=imagem2)
fusca.place(x=400, y=10)

janela.geometry('900x500+0+0')
janela.mainloop()