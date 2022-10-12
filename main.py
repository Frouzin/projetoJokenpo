import tkinter
from tkinter import *
from tkinter import ttk, Frame

# Separando Cores

co0 = "#FFFFFF"  # white / branca
co1 = "#333333"  # black / preta
co2 = "#fcc058"  # orange / laranja
co3 = "#fff873"  # yellow / amarela
co4 = "#34eb3d"  # green / verde
co5 = "#e85151"  # red / vermelha
fundo = "#3b3b3b" #gray/cinza

# Criando Tela com Tkinter

window = Tk()
window.title('')
window.geometry('280x320')
window.config(bg=fundo)


# Divisão de tela

frame_up=Frame(window, width=280, height=100, bg=co4, relief='raised')
frame_up.grid(row=0, column=0, sticky=NW)

frame_down = Frame(window, width=280, height=300, bg=co0, relief='flat')
frame_down.grid(row=1, column=0, sticky=NW)

style = ttk.Style(window)
style.theme_use('clam')

# COnfigurando o Frame

player_1 = Label(frame_up, text='You', height=1, anchor='center', font=('Arial 10 bold'), bg=co4, fg=co1)
player_1.place(x=20, y=70)

player_1_line = Label(frame_up, text='', height=10, anchor='center', font=('Arial 10 bold'), bg=co0, fg=co1)
player_1_line.place(x=0, y=0)

# Codigo de atualização da Tela (sempre deixar no final do código)
window.mainloop()
