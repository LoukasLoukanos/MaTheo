from tkinter import *
from tkinter import ttk
#from teoria_conjuntos import *
#from filo_e_hist import *

tk = Tk()
tk.title("MaTheo")#MaTheo, das iniciais de "Mathematical Theorems"
p1 = PhotoImage(file = 'icon_octaedro_window.png')
tk.iconphoto(False, p1)
tk.geometry('1038x647+230+75')

tk.resizable(width=0, height=0)
tk.configure(background="#6e00ff", padx=1, pady=1)

frame_main = Frame(tk, borderwidth=2, relief="sunke",background="#6e00ff")
frame_main.place(x=3, y=3,height=639, width=1030)

photo_main = PhotoImage(file='img_main.png')
label_photo = Label(tk, bg="#6e00ff", image=photo_main, compound='bottom')
label_photo.place(x=4, y=4)

'''
JANELA:  1028largura x 648altura

BOTÕES: [220largura] x [23altura]

|0(+espaço de 30+4)| [34(+botão de 220)] |254(+espaço de 30)| [284(+botão de 220)] |504(+espaço de 30)| [534(+botão de 220)] |754(+espaço de 30)| [784(+botão de 220)] |1004(+espaço de 30+4=1038)

|  0(+espaço de 38)|
	[ 38(+botão de 23)]
| 61(+espaço de 38)|
	[ 99(+botão de 23)]
|122(+espaço de 38)|
	[160(+botão de 23)]
|183(+espaço de 38)|
	[221(+botão de 23)]
|244(+espaço de 38)|
	[282(+botão de 23)]
|305(+espaço de 38)|
	[343(+botão de 23)]
|366(+espaço de 38)|
	[404(+botão de 23)]
|427(+espaço de 38)|
	[465(+botão de 23)]
|487(+espaço de 38)|
	[525(+botão de 23)]
|548(+espaço de 38)|
	[586(+botão de 23)]
|609(+espaço de 38=647)
'''

#MATEMÁTICA DO ENSINO FUNDAMENTAL:
def but01():
    b01 = Tk()
    b01.title("MaTheo   Teoria dos Conjuntos")#MaTheo, das iniciais de "Mathematical Theorems"
    b01.geometry('799x493+250+100')
    b01.resizable(width=0, height=0)
    b01.configure(background="#6e00ff", padx=1, pady=1)

but_01 = Button(tk, text='Teoria dos Conjuntos', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_01.place(x=34, y=38)

but_02 = Button(tk, text='Conjuntos Numéricos', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_02.place(x=34, y=99)

but_03 = Button(tk, text='Expressões Algébricas', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_03.place(x=34, y=160)

but_04 = Button(tk, text='Potenciação', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_04.place(x=34, y=221)

but_05 = Button(tk, text='Radiciação', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_05.place(x=34, y=282)

but_06 = Button(tk, text='Equações do 1° Grau', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_06.place(x=34, y=343)

but_07 = Button(tk, text='Equações do 2° Grau', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_07.place(x=34, y=404)

but_08 = Button(tk, text='Equações Biquadradas e Irracionais', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_08.place(x=34, y=465)

but_09 = Button(tk, text='Estudos de Funções I', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_09.place(x=34, y=525)

but_10 = Button(tk, text='Inequações do 1° e 2° Graus', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_10.place(x=34, y=586)

but_11 = Button(tk, text='Trigonomeria I', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_11.place(x=284, y=38)

but_12 = Button(tk, text='Geometria Plana',font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_12.place(x=284, y=99)

#MATEMÁTICA DO ENSINO MÉDIO:
but_13 = Button(tk, text='Estudos de Funções II', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_13.place(x=284, y=160)

but_14 = Button(tk, text='Logaritmos e Equações Exponenciais', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_14.place(x=284, y=221)

but_15 = Button(tk, text='Progreção Aritmética', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_15.place(x=284, y=282)

but_16 = Button(tk, text='Progreção Geométrica', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_16.place(x=284, y=343)

but_17 = Button(tk, text='Trigonometria II', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_17.place(x=284, y=404)

but_18 = Button(tk, text='Análise Combinatória', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_18.place(x=284, y=465)

but_19 = Button(tk, text='Bonômio de Newton', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_19.place(x=284, y=525)

but_20 = Button(tk, text='Probabilidades', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_20.place(x=284, y=586)

but_21 = Button(tk, text='Estatísticas', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_21.place(x=534, y=38)

but_22 = Button(tk, text='Matrizes', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_22.place(x=534, y=99)

but_23 = Button(tk, text='Determinantes', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_23.place(x=534, y=160)

but_24 = Button(tk, text='Sistemas Lineares', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_24.place(x=534, y=221)

but_25 = Button(tk, text='Geometria Analítica', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_25.place(x=534, y=282)

but_26 = Button(tk, text='Polinômios', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_26.place(x=534, y=343)

but_27 = Button(tk, text='Números Complexos', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_27.place(x=534, y=404)

but_28 = Button(tk, text='Equações ALgébricas', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_28.place(x=534, y=465)

but_29 = Button(tk, text='Geometria Espacial', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_29.place(x=534, y=525)

#MATEMÁTICA COMERCIAL:
but_30 = Button(tk, text='Razão e Proporção', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_30.place(x=534, y=586)

but_31 = Button(tk, text='Grandezas e Divisões Proporcionais', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_31.place(x=784, y=38)

but_32 = Button(tk, text='Regra de Sociedade', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_32.place(x=784, y=99)

but_33 = Button(tk, text='Regra de Três', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_33.place(x=784, y=160)

but_34 = Button(tk, text='Percentagem', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_34.place(x=784, y=221)

but_35 = Button(tk, text='Juros e Descontos Simples', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_35.place(x=784, y=282)

#MATEMÁTICA FINANCEIRA:
but_36 = Button(tk, text='Juros e Descontos Compostos', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_36.place(x=784, y=343)

but_37 = Button(tk, text='Capitalização e Amortização', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_37.place(x=784, y=404)

#OUTROS
but_38 = Button(tk, text='Lógica', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_38.place(x=784, y=465)

but_39 = Button(tk, text='Conversões de Bases', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_39.place(x=784, y=525)

def butn4():
    b40 = Tk()
    b40.title("MaTheo   Filosofia e História da Matemática")#MaTheo, das iniciais de "Mathematical Theorems"
    b40.geometry('799x493+250+100')
    b40.configure(background="#008c91", padx=1, pady=1)

    photo_bn4 = PhotoImage(file='img_bn4.png')
    lab_b40 = Label(b40, bg="#008c91", image=photo_bn4, compound='bottom')
    lab_b40.pack(side='top')

but_40 = Button(tk, text='Filosofia e História da Matemática', font="arial 8 italic bold", fg="#1e0066", bg="#6e00ff", height=1, width=30, command=but01, activebackground="#6e00ff", activeforeground="#ffffff", borderwidth=1, relief="flat", overrelief="raised")
but_40.place(x=784, y=586)

mainloop()
