import tkinter
import random
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

# COnfigurando o Tela de Pontuação

player_1 = Label(frame_up, text='You', height=1, anchor='center', font='Arial 10 bold', bg=co4, fg=co1)
player_1.place(x=20, y=70)
player_1_line = Label(frame_up, text='', height=10, anchor='center', font='Arial 10 bold', bg=co0, fg=co1)
player_1_line.place(x=0, y=0)
player_1_point = Label(frame_up, text='0', height=1, anchor='center', font='Arial 30 bold', bg=co4, fg=co1)
player_1_point.place(x=50, y=20)

Mid = Label(frame_up, text=':', height=1, anchor='center', font='Arial 30 bold', bg=co4, fg=co1)
Mid.place(x=130, y=20)

player_2_point = Label(frame_up, text='0', height=1, anchor='center', font='Arial 30 bold', bg=co4, fg=co1)
player_2_point.place(x=200, y=20)
player_2 = Label(frame_up, text='PC', height=1, anchor='center', font='Arial 10 bold', bg=co4, fg=co1)
player_2.place(x=235, y=70)
player_2_line = Label(frame_up, text='', height=10, anchor='center', font='Arial 10 bold', bg=co0, fg=co1)
player_2_line.place(x=275, y=0)

line = Label(frame_up, text='', width=275, anchor='center', font='Arial 1 bold', bg=co0, fg=co1)
line.place(x=0, y=95)

global you
global pc

points_You = 0
points_Pc = 0
rodadas = 0
# Lógica do Jogo
def jogar(i):

    if rodadas > 0:
        print(rodadas)
        options = {'Pedra', 'Papel', 'Tesoura'}
        pc = random.choice(options)
        you = i

        print(you, pc)

    else:
        end_Game()

# Configurando tela de Game
def play_Game():

    rock = Button(frame_down, command=lambda: jogar(rock), width=35, text='pedra', compound='center', bg=co1, fg=co0, font='Arial 10 bold')
    rock.place(x=0, y=60)

    scissors = Button(frame_down, command=lambda: jogar(papers), width=35, text='papel', compound='center', bg=co1, fg=co0, font='Arial 10 bold')
    scissors.place(x=0, y=90)

    papers = Button(frame_down, command=lambda: jogar(scissors), width=35, text='tesoura', compound='center', bg=co1, fg=co0, font='Arial 10 bold')
    papers.place(x=0, y=120)



# Fim de Jogo
def end_Game():
    pass

    play = Button(frame_down, command = play_Game(), width=10, text='Jogar', compound='center', bg=co2, fg=co1, font='Arial 10 bold')
    play.place(x=0, y=30)



# Codigo de atualização da Tela (sempre deixar no final do código)
window.mainloop()
