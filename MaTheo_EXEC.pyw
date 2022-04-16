from tkinter import *
from tkinter import ttk
#from teoria_conjuntos import *
#from filo_e_hist import *

tk = Tk()
tk.title("MaTheo")#MaTheo, das iniciais de "Mathematical Theorems"
p1 = PhotoImage(file = 'icon_octaedro_window.png')
tk.iconphoto(False, p1)
tk.geometry('780x488+275+175')

tk.resizable(width=0, height=0)
tk.configure(background="#252d44", padx=1, pady=1)

frame_main = Frame(tk, borderwidth=2, relief="sunke", background="#1d2438")
frame_main.place(x=3, y=3,height=460, width=772)

photo_main = PhotoImage(file='img_main.png')
label_photo = Label(tk, bg="#1d2438", image=photo_main, compound='bottom')
label_photo.place(x=4, y=4)

menu_bar = Menu(tk, background="#1d2438", fg="#ffffff")
menu_main = Menu(menu_bar, tearoff=False, background="#ffffff", activebackground="#1d2438", font="Arial 8", fg="#000000", activeforeground="#ffffff")
menu_main.add_command(label="Pesquisar teorema(Criar botão menu)", command=None)
menu_main.add_command(label="Tabelas matemáticas", command=None)
menu_main.add_command(label="Materiais didáticos", command=None)
menu_main.add_separator()
menu_main.add_command(label="Fechar", command=tk.quit)
menu_bar.add_cascade(label=" ☰ ", menu=menu_main)

menu_2 = Menu(menu_bar, tearoff=False, background="#ffffff", activebackground="#1d2438", font="Arial 8", fg="#000000", activeforeground="#ffffff")
menu_2.add_command(label="Teoria dos Conjuntos", command=None)
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

menu_3 = Menu(menu_bar, tearoff=False, background="#ffffff", activebackground="#1d2438", font="Arial 8", fg="#000000", activeforeground="#ffffff")
menu_3.add_command(label="Lógica", command=None)
menu_3.add_command(label="Conversões de Bases", command=None)
menu_3.add_command(label="Cálculo", command=None)
menu_bar.add_cascade(label="   Ensino Superior   ", menu=menu_3)

menu_4 = Menu(menu_bar, tearoff=False, background="#ffffff", activebackground="#1d2438", font="Arial 8", fg="#000000", activeforeground="#ffffff")
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

menu_5 = Menu(menu_bar, tearoff=False, background="#ffffff", activebackground="#1d2438", font="Arial 8", fg="#000000", activeforeground="#ffffff")
menu_5.add_command(label="Idade Antiga e Período Clássico 6000 a.C.-500 d.C", command=None)
menu_5.add_command(label="Idade Média 500-1500", command=None)
menu_5.add_command(label="Renascimento 1500-1680", command=None)
menu_5.add_command(label="Iluminismo 1680-1800", command=None)
menu_5.add_command(label="Século XIX 1800-1900", command=None)
menu_5.add_command(label="Era Moderna 1900-Hoje", command=None)
menu_bar.add_cascade(label="   Filosofia e História da Matemática   ", menu=menu_5)

menu_6 = Menu(menu_bar, tearoff=False, background="#ffffff", activebackground="#1d2438", font="Arial 8", fg="#000000", activeforeground="#ffffff")
menu_bar.add_cascade(label="    Sobre    ", menu=menu_6, command=None)

tk.config(menu=menu_bar)

'''
#MATEMÁTICA DO ENSINO FUNDAMENTAL E MÉDIO::
def but01():
    b01 = Tk()
    b01.title("MaTheo   Teoria dos Conjuntos")#MaTheo, das iniciais de "Mathematical Theorems"
    b01.geometry('799x493+275+100')
    b01.resizable(width=0, height=0)
    b01.configure(background="#1d2438", padx=1, pady=1)

but_01 = Button(tk, text='Logaritmos e Equações Exponenc.', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, overrelief=None)
but_01.place(x=75, y=20)

but_02 = Button(tk, text='Equaç. e Inequaç. do 1° e 2° Grau', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_02.place(x=75, y=60)

but_03 = Button(tk, text='Equaç Biquadradas e Irracionais', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_03.place(x=75, y=100)

but_04 = Button(tk, text='Potenciação e Radiciação', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_04.place(x=75, y=140)

but_05 = Button(tk, text='Expressões Algébricas', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_05.place(x=75, y=180)

but_06 = Button(tk, text='Progreção Geométrica', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_06.place(x=75, y=220)

but_07 = Button(tk, text='Conjuntos Numéricos', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_07.place(x=75, y=260)

but_08 = Button(tk, text='Progreção Aritmética',font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_08.place(x=75, y=300)

but_09 = Button(tk, text='Geometria Plana', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_09.place(x=75, y=340)

but_10 = Button(tk, text='Trigonomeria', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_10.place(x=75, y=380)

but_11 = Button(tk, text='Funções', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_11.place(x=75, y=420)

but_12 = Button(tk, text='Equações ALgébricas', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_12.place(x=333, y=20)

but_13 = Button(tk, text='Análise Combinatória', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_13.place(x=333, y=60)

but_14 = Button(tk, text='Números Complexos', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_14.place(x=333, y=100)

but_15 = Button(tk, text='Geometria Espacial', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_15.place(x=333, y=140)

but_16 = Button(tk, text='Geometria Analítica', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_16.place(x=333, y=180)

but_17 = Button(tk, text='Binômio de Newton', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_17.place(x=333, y=220)

but_18 = Button(tk, text='Sistemas Lineares', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_18.place(x=333, y=260)

but_19 = Button(tk, text='Probabilidades', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_19.place(x=333, y=300)

but_20 = Button(tk, text='Determinantes', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_20.place(x=333, y=340)

but_21 = Button(tk, text='Estatísticas', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_21.place(x=333, y=380)

but_22 = Button(tk, text='Polinômios', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_22.place(x=333, y=420)

but_23 = Button(tk, text='Juros e Descontos Compostos', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_23.place(x=535, y=20)

#MATEMÁTICA COMERCIAL:
but_24 = Button(tk, text='Capitalização e Amortização', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_24.place(x=535, y=60)

but_25 = Button(tk, text='Juros e Descontos Simples', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_25.place(x=535, y=100)

but_26 = Button(tk, text='Conversões de Bases', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_26.place(x=535, y=140)

but_27 = Button(tk, text='Regra de Sociedade', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_27.place(x=535, y=180)

#MATEMÁTICA FINANCEIRA:
but_28 = Button(tk, text='Razão e Proporção',font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_28.place(x=535, y=220)

but_29 = Button(tk, text='Regra de Três', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_29.place(x=535, y=260)

#OUTROS
but_30 = Button(tk, text='Percentagem', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_30.place(x=535, y=300)

but_31 = Button(tk, text='Matrizes', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_31.place(x=535, y=340)

but_32 = Button(tk, text='Cálculo', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_32.place(x=535, y=380)

but_32 = Button(tk, text='Lógica', font="Papyrus 8 italic", fg="#ffffff", bg="#1d2438", height=None, width=None, command=but01, activebackground="#1d2438", activeforeground="#ffffff", borderwidth=0, relief="flat", overrelief=None)
but_32.place(x=535, y=420)
'''

mainloop()
