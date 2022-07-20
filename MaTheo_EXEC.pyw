from tkinter import *
from tkinter import ttk
from tkinter import font
from teoria_conjunt import *
#from filo_e_hist import *

tk = Tk()
tk.title("MaTheo")#MaTheo, das iniciais de "Mathematical Theorems"
p1 = PhotoImage(file = 'icon_octaedro_window.png')
tk.iconphoto(False, p1)
tk.geometry('780x488+275+175')

tk.resizable(width=0, height=0)
tk.configure(background="#2f4f34", padx=1, pady=1)

frame_main = Frame(tk, borderwidth=2, relief="sunke", background="#2f4f34")
frame_main.place(x=3, y=3,height=460, width=772)

photo_main = PhotoImage(file='img_main.png')
label_photo = Label(tk, bg="#2f4f34", image=photo_main, compound='bottom')
label_photo.place(x=4, y=4)

ft = font.Font(family="Ink Free", size=10, weight="normal", slant="italic")

menu_bar = Menu(tk)
menu_main = Menu(menu_bar, tearoff=False, background="#2f4f34", activebackground="#2f4f34", font=ft, fg="#ffffff", activeforeground="#ff7f50")
menu_main.add_command(label="Pesquisar Teoremas", command=None)#CRIAR BOTÃO MENU CONTENDO TODAS AS FÓRMULAS------------------------------------------
menu_main.add_command(label="Tabelas Matemáticas", command=None)#ABRIR NOVA JANELA CONTENDO AS TABELAS(DESEJÁVEL DISPONIBILIZAR DOWNLOAD)------------
menu_main.add_command(label="Materiais Didáticos", command=None)#ABRIR NOVA JANELA CONTENDO EBOOKS---------------------------------------------------
menu_main.add_command(label="Favoritos", command=None)#ARRASTAR TÓPICOS PARA A ÁREA DE TRABALHO DO SOFTWARE(QUADRO DE FÓRMULAS)----------------------
menu_main.add_separator()
menu_main.add_command(label="Fechar", command=tk.quit)
menu_bar.add_cascade(label=" ☰ ", menu=menu_main)
#--------------------------------------------------------------------------------------------------------------------------------------------------
#TODOS OS TÓPICOS DOS MENUS AQUI(EXCETO O MENU 'SOBRE') ABRIRÃO NOVAS JANELAS PARA QUE SE POSSA UTILIZAR VÁRIOS TÓPICOS SEM PRECISAR FECHAR O ATUAL
menu_2 = Menu(menu_bar, tearoff=False, background="#2f4f34", activebackground="#2f4f34", font=ft, fg="#ffffff", activeforeground="#ff7f50")
menu_2.add_command(label="Teoria dos Conjuntos", command=teste)
menu_2.add_command(label="Conjuntos Numéricos", command=None)
menu_2.add_command(label="Expressões e Equações Algébricas", command=None)
menu_2.add_command(label="Potenciação e Radiciação", command=None)
menu_2.add_command(label="Equações e Inequações do 1° e 2° Grau", command=None)
menu_2.add_command(label="Equações Biquadradas e Equações Irracionais", command=None)
menu_2.add_command(label="Estudos de Funções", command=None)
menu_2.add_command(label="Trigonomeria", command=None)
menu_2.add_command(label="Geometria Plana", command=None)
menu_2.add_command(label="Logaritmos e Equações Exponenciais", command=None)
menu_2.add_command(label="Progressão Aritmética", command=None)
menu_2.add_command(label="Progressão Geométrica", command=None)
menu_2.add_command(label="Análise Combinatória", command=None)
menu_2.add_command(label="Binômio de Newton", command=None)
menu_2.add_command(label="Probabilidades", command=None)
menu_2.add_command(label="Matrizes", command=None)
menu_2.add_command(label="Determinantes", command=None)
menu_2.add_command(label="Sistemas Lineares", command=None)
menu_2.add_command(label="Geometria Analítica", command=None)
menu_2.add_command(label="Polinômios", command=None)
menu_2.add_command(label="Números Complexos", command=None)
menu_2.add_command(label="Teoria dos Conjuntos", command=None)
menu_2.add_command(label="Geometria Espacial", command=None)
menu_bar.add_cascade(label="   Ensino Fundamental e Médio   ", menu=menu_2)

menu_3 = Menu(menu_bar, tearoff=False, background="#2f4f34", activebackground="#2f4f34", font=ft, fg="#ffffff", activeforeground="#ff7f50")
menu_3.add_command(label="Lógica", command=None)
menu_3.add_command(label="Conversões de Bases", command=None)
menu_3.add_command(label="Cálculo", command=None)
menu_bar.add_cascade(label="   Ensino Superior   ", menu=menu_3)

menu_4 = Menu(menu_bar, tearoff=False, background="#2f4f34", activebackground="#2f4f34", font=ft, fg="#ffffff", activeforeground="#ff7f50")
menu_4.add_command(label="Razão e Proporção", command=None)
menu_4.add_command(label="Grandezas e Divisões Proporcionais", command=None)
menu_4.add_command(label="Regra de Sociedade", command=None)
menu_4.add_command(label="Regra de Três", command=None)
menu_4.add_command(label="Percentagem", command=None)
menu_4.add_command(label="Juros Simples", command=None)
menu_4.add_command(label="Desconto Simples", command=None)
menu_4.add_command(label="Juros Composto", command=None)
menu_4.add_command(label="Desconto Composto", command=None)
menu_4.add_command(label="Capitalização Simples", command=None)
menu_4.add_command(label="Capitalização Composta", command=None)
menu_4.add_command(label="Taxas", command=None)
menu_4.add_command(label="Rendas ou Séries Uniformes", command=None)
menu_4.add_command(label="Correção Monetária e Indicadores", command=None)
menu_4.add_command(label="Depreciação", command=None)
menu_4.add_command(label="Arrendamento Mercantil - Leasing", command=None)
menu_4.add_command(label="Debêntures", command=None)
menu_4.add_command(label="Amortizações", command=None)
menu_bar.add_cascade(label="   Comercial e Financeira   ", menu=menu_4)

menu_5 = Menu(menu_bar, tearoff=False, background="#2f4f34", activebackground="#2f4f34", font=ft, fg="#ffffff", activeforeground="#ff7f50")
menu_5.add_command(label="Idade Antiga e Período Clássico 6000 a.C.-500 d.C", command=None)
menu_5.add_command(label="Idade Média 500-1500", command=None)
menu_5.add_command(label="Renascimento 1500-1680", command=None)
menu_5.add_command(label="Iluminismo 1680-1800", command=None)
menu_5.add_command(label="Século XIX 1800-1900", command=None)
menu_5.add_command(label="Era Moderna 1900-Hoje", command=None)
menu_bar.add_cascade(label="   Filosofia e História da Matemática   ", menu=menu_5)

menu_6 = Menu(menu_bar, tearoff=False, background="#2f4f34", activebackground="#2f4f34", font=ft, fg="#ffffff", activeforeground="#ff7f50")
menu_bar.add_cascade(label="    Sobre    ", menu=menu_6, command=None)

tk.config(menu=menu_bar)

mainloop()
