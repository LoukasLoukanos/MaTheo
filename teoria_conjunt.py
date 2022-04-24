from tkinter import *
from tkinter import ttk
from typing import Counter, Type

def teste():
    b01 = Tk()
    b01.title("MaTheo   Teoria dos Conjuntos")#MaTheo, das iniciais de "Mathematical Theorems"
    b01.geometry('450x278+250+100') 
    #b01.resizable(width=0, height=0)
    b01.configure(background="#2c2a3a", padx=1, pady=1)

    #_______________UNIÕES___________________________________________________________________________
    #remover caracteres:------------------------------------------------------
    def chr_remove(old, to_remove):
        new_string = old
        for x in to_remove:
            new_string = new_string.replace(x,"")
            return new_string

    #Contar e formatar as uniões para a chamada da função cut_repetitions()---
    def count_elements(uni):
        uni = str(uni)
        uni = chr_remove(uni, "'")
        uni = chr_remove(uni, ",")
        uni = uni[1:-1]
        unity_count = str(uni)
        unity_count = len(unity_count.split())
        return(int(unity_count))
    
    def format_elements(uni):
        uni = str(uni)
        uni = chr_remove(uni, "'")
        uni = chr_remove(uni, ",")
        #uni = uni[1:-1]
        uni = chr_remove(uni, "[")
        uni = chr_remove(uni, "]")
        uni = str(uni)
        uni = uni.split()
        return(uni)
        
    #função que retira elementos repetidos das uniões--------------------------
    def cut_repetitions(uni, count_uni):
        num_y = num_x = 0
        values = True
        unity = uni
        unity_count = count_uni
        while values:
            if unity[num_x] == unity[num_y] and num_x != num_y:
                x = unity[num_y]
                x = "'"+x+"'"

                unity = str(unity)
                unity = unity[1:-1]
                unity = unity.replace(x, "")
                unity = unity + ", " + x
                unity = chr_remove(unity, "'")
                unity = chr_remove(unity, ",")
                
                unity = str(unity)
                unity = unity.split()

                unity = str(unity)
                unity_count = count_elements(unity)
            
                unity = chr_remove(unity, "'")
                unity = chr_remove(unity, ",")
                unity = chr_remove(unity, "[")
                unity = chr_remove(unity, "]")
                unity = str(unity)
                unity = unity.split()

                num_x = 0
                num_y = 0

            num_y = num_y + 1
            if num_y >= unity_count:
                num_y = 0
                num_x = num_x + 1
                if num_x >= unity_count:
                    values = False
                    return(unity)

    #formatar após a chamada da função cut_repetitions-------------------------
    def format_after_cut_repetitions(conj):
        conj = tuple(conj)
        conj = sorted(conj)
        conj = str(conj)
        conj = conj[1:-1]
        conj = chr_remove(conj, "'")
        return(conj)

    global conj_array, elem_array, conjunt, num_conj, ind_elem, process, matriz, conj
    conj_array = []
    elem_array = []
    conjunt =  -1
    num_conj = 0
    ind_elem = 0
    process = 1
    matriz = {}

    #texto informando para definir um nome para o conjunto
    label_conj_text = Label(b01, text="Definir o nome do conjunto:", font="arial 8", fg="#ffffff", bg="#2c2a3a", padx=3)
    label_conj_text.place(x=10, y=20)

    #número atual do conjunto a ser definido
    conj_num = num_conj+1
    conj_numvar = StringVar()
    conj_numvar.set(conj_num)
    label_conj_num = Label(b01, textvariable=conj_numvar, font="arial 8", fg="#ffffff", bg="#2c2a3a", padx=3)
    label_conj_num.place(x=148, y=20)
        
    #entrada do nome do conjunto
    conj = Entry(b01, font="arial 8 bold", fg="#ffffff", bg="#2c2a3a", width=3)
    conj.place(x=178, y=20)

    def button_adc_elem():
        global elem_array
        elem_array = []
        global num_conj
        global conjunt
        fr_conj= Frame(b01, borderwidth=1, relief="flat",background="#2c2a3a") #relief=flat,raised,sunke,solid(tipo de borda)
        fr_conj.place(x=10, y=20, width=1000, height=1000)

        conjunt = conjunt + 1
            
        #aparecer texto informando os conjuntos ja definidos
        label_conj_text02 = Label(b01, text="Conjuntos:", font="arial 8", fg="#ffffff", bg="#2c2a3a", padx=3)
        label_conj_text02.place(x=10, y=20)
        
#-------ERRO DO TKINTER??? TEXTVARIAVEL NÃO APARECE QUANDO ESTÁ NO ESCOPO DE FUNÇÃO???------------------------------------------------------------
        #aparecer conjuntos ja definidos
        conj_defin = StringVar()
        conj_defin.set(conj_array)
        label_conj_num = Label(b01, textvariable=conj_defin, font="arial 8 bold", fg="#ffffff", bg="#2c2a3a", padx=3)
        label_conj_num.place(x=10, y=38)

        #texto informando para definir a quantidade de elementos
        label_conj_text = Label(b01, text="Definir a quantidade de elementos do conjunto", font="arial 8", fg="#ffffff", bg="#2c2a3a", padx=3)
        label_conj_text.place(x=10, y=60)

        #nome do conjunto a ser definido a quantidade de elementos
        conj_nom = conj_array[conjunt]
        conj_nomvar = StringVar()
        conj_nomvar.set(conj_nom)
        label_conj_nom = Label(b01, textvariable=conj_nomvar, font="arial 8 bold", fg="#ffffff", bg="#2c2a3a", padx=3)
        label_conj_nom.place(x=240, y=60)
        
        #entrada da quantidade de elementos
        count = Entry(b01, font="arial 8 bold", fg="#ffffff", bg="#2c2a3a", width=3)
        count.place(x=60, y=82)

        def elements():
            global ind_elem
            global num_conj
            count_elem = count.get()
            count_elem = int(count_elem)
            if ind_elem < count_elem:

                fr_conj= Frame(b01, borderwidth=1, relief="flat",background="#2c2a3a") #relief=flat,raised,sunke,solid(tipo de borda)
                fr_conj.place(x=10, y=60, width=1000, height=1000)

                #texto informando para definir os elementos
                label_conj_text = Label(b01, text="Adicione o", font="arial 8", fg="#ffffff", bg="#2c2a3a", padx=3)
                label_conj_text.place(x=10, y=60)

                conj_text = process
                conj_textvar = StringVar()
                conj_textvar.set(conj_text)
                label_conj_text = Label(b01, textvariable=conj_textvar, font="arial 8", fg="#ffffff", bg="#2c2a3a", padx=3)
                label_conj_text.place(x=60, y=60)

                label_conj_text = Label(b01, text="° elemento do conjunto", font="arial 8",fg="#ffffff", bg="#2c2a3a", padx=3)
                label_conj_text.place(x=70, y=60)

                conj_nom = conj_array[ind_elem]
                conj_nomvar = StringVar()
                conj_nomvar.set(conj_nom)
                label_conj_nom = Label(b01, textvariable=conj_nomvar, font="arial 8 bold", fg="#ffffff", bg="#2c2a3a", padx=3)
                label_conj_nom.place(x=190, y=60)

                entry_elem = Entry(b01, font="arial 8 bold", fg="#ffffff", bg="#2c2a3a", width=3)
                entry_elem.place(x=60, y=82)

                def adc_elements():
                    global ind_elem
                    global process
                    element = entry_elem.get()
                    element = str(element)
                    elem_array.append(element) 
                
                    matriz[conj_array[ind_elem]] = elem_array
                    process = process + 1

                    if process > count_elem:
                        if ind_elem != num_conj:
                            num_elem_of_conjunt = count_elements(matriz[conj_array[ind_elem]])
                            elem_formateds = format_elements(matriz[conj_array[ind_elem]])
                            elem_cut_repetitions = cut_repetitions(elem_formateds, num_elem_of_conjunt)
                            num_elem_of_conjunt = count_elements(elem_cut_repetitions)
                            print("conjunto",conj_array[ind_elem]," sem repetições: ",elem_cut_repetitions,". Total de",num_elem_of_conjunt,"elementos.")
                            process = 1
                            ind_elem = ind_elem + 1
                            if ind_elem != num_conj:
                                button_adc_elem()
                            
                        if ind_elem == num_conj:
                            print("entrou na condição")
                            ind_x = 0
                            uniao = []
                            runnig = True
                            while runnig:
                                if ind_x < num_conj:
                                    uniao = uniao + matriz[conj_array[ind_x]]
                                    ind_x = ind_x + 1
                                else:
                                    if ind_x == num_conj:
                                        print("união de todos:", uniao)
                                        runnig = False             
                    else:
                        elements()

                but_adc_elem = Button(b01, text='Adicionar', font="arial 7", fg="#ffffff", bg="#2c2a3a", padx=3, height=1, width=14, command=adc_elements)
                but_adc_elem.place(x=90, y=80)

        but_adc = Button(b01, text='Definir quantidade', font="arial 7", fg="#ffffff", bg="#2c2a3a", padx=3, height=1, width=14, command=elements)
        but_adc.place(x=90, y=80)

    def button_definir_elementos():
        if num_conj >= 2:
            but_adc = Button(b01, text='Definir elementos', font="arial 7", fg="#ffffff", bg="#2c2a3a", padx=3, height=1, width=18, command=button_adc_elem)
            but_adc.place(x=80, y=90)

    #função do botão de definir nomes de conjuntos
    def button_adc_conj():
        global conj_array
        global num_conj
        global conj

        #aparecer texto informando os conjuntos ja definidos
        label_conj_text02 = Label(b01, text="Conjuntos:", font="arial 8", fg="#ffffff", bg="#2c2a3a", padx=3)
        label_conj_text02.place(x=10, y=45)
            
        #aparecer conjuntos ja definidos
        conj_name = conj.get()
        conj_array.append(conj_name)
        conj_defin = StringVar()
        conj_defin.set(conj_array)
        label_conj_num = Label(b01, textvariable=conj_defin, font="arial 8 bold", fg="#ffffff", bg="#2c2a3a", padx=3)
        label_conj_num.place(x=10, y=63)

        #número atual do novo conjunto a ser definido
        num_conj = num_conj + 1
        conj_num = num_conj + 1
        conj_numvar = StringVar()
        conj_numvar.set(conj_num)
        label_conj_num = Label(b01, textvariable=conj_numvar, font="arial 8", fg="#ffffff", bg="#2c2a3a", padx=3)
        label_conj_num.place(x=148, y=20)
        button_definir_elementos()

    #botão de definir nomes de conjuntos
    but_adc = Button(b01, text='Ok', font="arial 6", fg="#ffffff", bg="#2c2a3a", padx=3, height=1, width=5, command=button_adc_conj)
    but_adc.place(x=206, y=20)

    mainloop()
