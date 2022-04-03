from tkinter import *
from tkinter import ttk
from typing import Counter, Type

b01 = Tk()
b01.title("MaTheo   Teoria dos Conjuntos")#MaTheo, das iniciais de "Mathematical Theorems"
b01.geometry('450x278+250+100') 
#b01.resizable(width=0, height=0)
b01.configure(background="#6e00ff", padx=1, pady=1)

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



conj_array = []
elem_array = []
conjunt =  -1
num_conj = 0
ind_elem = 0
process = 1
matriz = {}

#texto informando para definir um nome para o conjunto
conj_text = "Definir o nome do conjunto:"
conj_textvar = StringVar()
conj_textvar.set(conj_text)
label_conj_text = Label(b01, textvariable=conj_textvar, font="arial 8", fg="#ffffff", bg="#6d02f9", padx=3)
label_conj_text.place(x=10, y=20)

#númeor atual do conjunto a ser definido
conj_num = num_conj+1
conj_numvar = StringVar()
conj_numvar.set(conj_num)
label_conj_num = Label(b01, textvariable=conj_numvar, font="arial 8", fg="#ffffff", bg="#6d02f9", padx=3)
label_conj_num.place(x=148, y=20)
    
#entrada do nome do conjunto
conj = Entry(b01, font="arial 8 bold", fg="#ffffff", bg="#6d02f9", width=3)
conj.place(x=178, y=20)

def button_adc_elem():
    global elem_array
    elem_array = []
    global num_conj
    global conjunt
    fr_conj= Frame(b01, borderwidth=1, relief="flat",background="#6d02f9") #relief=flat,raised,sunke,solid(tipo de borda)
    fr_conj.place(x=10, y=20, width=1000, height=1000)

    conjunt = conjunt + 1
        
    #aparecer texto informando os conjuntos ja definidos
    conj_text02 = "Conjuntos:"
    conj_textvar02 = StringVar()
    conj_textvar02.set(conj_text02)
    label_conj_text02 = Label(b01, textvariable=conj_textvar02, font="arial 8", fg="#ffffff", bg="#6d02f9", padx=3)
    label_conj_text02.place(x=10, y=20)
    
    #aparecer conjuntos ja definidos
    conj_defin = StringVar()
    conj_defin.set(conj_array)
    label_conj_num = Label(b01, textvariable=conj_defin, font="arial 8 bold", fg="#ffffff", bg="#6d02f9", padx=3)
    label_conj_num.place(x=10, y=38)

    #texto informando para definir a quantidade de elementos
    conj_text = "Definir a quantidade de elementos do conjunto"
    conj_textvar = StringVar()
    conj_textvar.set(conj_text)
    label_conj_text = Label(b01, textvariable=conj_textvar, font="arial 8", fg="#ffffff", bg="#6d02f9", padx=3)
    label_conj_text.place(x=10, y=60)

    #nome do conjunto a ser definido a quantidade de elementos
    conj_nom = conj_array[conjunt]
    conj_nomvar = StringVar()
    conj_nomvar.set(conj_nom)
    label_conj_nom = Label(b01, textvariable=conj_nomvar, font="arial 8 bold", fg="#ffffff", bg="#6d02f9", padx=3)
    label_conj_nom.place(x=240, y=60)
    
    #entrada da quantidade de elementos
    count = Entry(b01, font="arial 8 bold", fg="#ffffff", bg="#6d02f9", width=3)
    count.place(x=60, y=82)

    def elements():
        global ind_elem
        global num_conj
        count_elem = count.get()
        count_elem = int(count_elem)
        if ind_elem < count_elem:

            fr_conj= Frame(b01, borderwidth=1, relief="flat",background="#6d02f9") #relief=flat,raised,sunke,solid(tipo de borda)
            fr_conj.place(x=10, y=60, width=1000, height=1000)

            #texto informando para definir os elementos
            conj_text = "Adicione o"
            conj_textvar = StringVar()
            conj_textvar.set(conj_text)
            label_conj_text = Label(b01, textvariable=conj_textvar, font="arial 8", fg="#ffffff", bg="#6d02f9", padx=3)
            label_conj_text.place(x=10, y=60)

            conj_text = process
            conj_textvar = StringVar()
            conj_textvar.set(conj_text)
            label_conj_text = Label(b01, textvariable=conj_textvar, font="arial 8", fg="#ffffff", bg="#6d02f9", padx=3)
            label_conj_text.place(x=60, y=60)

            conj_text = "° elemento do conjunto"
            conj_textvar = StringVar()
            conj_textvar.set(conj_text)
            label_conj_text = Label(b01, textvariable=conj_textvar, font="arial 8",fg="#ffffff", bg="#6d02f9", padx=3)
            label_conj_text.place(x=70, y=60)

            conj_nom = conj_array[ind_elem]
            conj_nomvar = StringVar()
            conj_nomvar.set(conj_nom)
            label_conj_nom = Label(b01, textvariable=conj_nomvar, font="arial 8 bold", fg="#ffffff", bg="#6d02f9", padx=3)
            label_conj_nom.place(x=190, y=60)

            entry_elem = Entry(b01, font="arial 8 bold", fg="#ffffff", bg="#6d02f9", width=3)
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

            but_adc_elem = Button(b01, text='Adicionar', font="arial 7", fg="#ffffff", bg="#6d02f9", padx=3, height=1, width=14, command=adc_elements)
            but_adc_elem.place(x=90, y=80)

    but_adc = Button(b01, text='Definir quantidade', font="arial 7", fg="#ffffff", bg="#6d02f9", padx=3, height=1, width=14, command=elements)
    but_adc.place(x=90, y=80)

def button_definir_elementos():
    if num_conj >= 2:
        but_adc = Button(b01, text='Definir elementos', font="arial 7", fg="#ffffff", bg="#6d02f9", padx=3, height=1, width=18, command=button_adc_elem)
        but_adc.place(x=80, y=90)

#função do botão de definir nomes de conjuntos
def button_adc_conj():
    global conj_array
    global num_conj
    global conj

    #aparecer texto informando os conjuntos ja definidos
    conj_text02 = "Conjuntos:"
    conj_textvar02 = StringVar()
    conj_textvar02.set(conj_text02)
    label_conj_text02 = Label(b01, textvariable=conj_textvar02, font="arial 8", fg="#ffffff", bg="#6d02f9", padx=3)
    label_conj_text02.place(x=10, y=45)
        
    #aparecer conjuntos ja definidos
    conj_name = conj.get()
    conj_array.append(conj_name)
    conj_defin = StringVar()
    conj_defin.set(conj_array)
    label_conj_num = Label(b01, textvariable=conj_defin, font="arial 8 bold", fg="#ffffff", bg="#6d02f9", padx=3)
    label_conj_num.place(x=10, y=63)

    #número atual do novo conjunto a ser definido
    num_conj = num_conj + 1
    conj_num = num_conj + 1
    conj_numvar = StringVar()
    conj_numvar.set(conj_num)
    label_conj_num = Label(b01, textvariable=conj_numvar, font="arial 8", fg="#ffffff", bg="#6d02f9", padx=3)
    label_conj_num.place(x=148, y=20)
    button_definir_elementos()

#botão de definir nomes de conjuntos
but_adc = Button(b01, text='Ok', font="arial 6", fg="#ffffff", bg="#6d02f9", padx=3, height=1, width=5, command=button_adc_conj)
but_adc.place(x=206, y=20)


'''
print("UNIÕES_____________________________________________________________________________________________________________________")
#união de A e B (AUB) com elementos repetidos:
aub = str(values_a + values_b)
count_aub = count_elements(aub)
aub = format(aub)

#união de A e C (AUC) com elementos repetidos:
auc = str(values_a + values_c)
count_auc = count_elements(auc)
auc = format(auc)
	
#união de B e C (BUC) com elementos repetidos:
buc = str(values_b + values_c)
count_buc = count_elements(buc)
buc = format(buc)
	
#união de A, B e C (AUBUC) com elementos repetidos:
aubuc_not_formatted = str(values_a + values_b + values_c) 
aubuc = aubuc_not_formatted
count_aubuc = count_elements(aubuc)
aubuc = format(aubuc)



#A sem elementos repetidos
a = cut_repetitions(values_a, count_a)
conj_a = format_after_cut_repetitions(a)
a = str(a)
count_a_after_cut = count_elements(a)
print("Elementos de A:", "{", conj_a, "}.\n", "Total de", count_a_after_cut, "elemento(s).\n")

#B sem elementos repetidos 
b = cut_repetitions(values_b, count_b)
conj_b = format_after_cut_repetitions(b)
b = str(b)
count_b_after_cut = count_elements(b)
print("Elementos de B:", "{", conj_b, "}.\n", "Total de", count_b_after_cut, "elemento(s).\n")

#AUB sem elementos repetidos
aub = cut_repetitions(aub, count_aub)
conj_aub = format_after_cut_repetitions(aub)
aub = str(aub)
count_aub_after_cut = count_elements(aub)
print("União de A e B (AUB):", "{", conj_aub, "}.\n", "Total de", count_aub_after_cut, "elemento(s).\n")

if count_c > 0:
    #C sem elementos repetidos 
    c = cut_repetitions(values_c, count_c)
    conj_c = format_after_cut_repetitions(c)
    c = str(c)
    count_c_after_cut = count_elements(c)
    print("Elementos de C:", "{", conj_c, "}.\n", "Total de", count_c_after_cut, "elemento(s).\n")
    
    #AUC sem elementos repetidos 
    auc = cut_repetitions(auc, count_auc)
    conj_auc = format_after_cut_repetitions(auc)
    auc = str(auc)
    count_auc_after_cut = count_elements(auc)
    print("União de A e C (AUC):", "{", conj_auc, "}.\n", "Total de", count_auc_after_cut, "elemento(s).\n")
	
    #BUC sem elementos repetidos 
    buc = cut_repetitions(buc, count_buc)
    conj_buc = format_after_cut_repetitions(buc)
    buc = str(buc)
    count_buc_after_cut = count_elements(buc)
    print("União de B e C (BUC):", "{", conj_buc, "}.\n", "Total de", count_buc_after_cut, "elemento(s).\n")
	
    #AUBUC sem elementos repetidos 
    aubuc = cut_repetitions(aubuc, count_aubuc)
    conj_aubuc = format_after_cut_repetitions(aubuc)
    aubuc = str(aubuc)
    count_aubuc_after_cut = count_elements(aubuc)
    print("União de A, B e C (AUBUC):", "{", conj_aubuc, "}.\n", "Total de", count_aubuc_after_cut, "elemento(s).\n")



print("_______\n\nintersecções:")
#procurar intersecções entre A e B________________________________________________
indic_a = indic_b = 0
intersec_ab = []
running_AB = True
while running_AB:
    if has_a[indic_a] == has_b[indic_b]:
        intersec_ab.append(str(has_a[indic_a]))
    if  count_a != 1:
        indic_a = indic_a + 1
    if indic_a == count_a or count_a == 1:
        if count_b == 1:
            running_AB = False
        indic_a = 0
        if count_b != 1:
            indic_b = indic_b + 1
    if indic_b == count_b and count_b != 1:
    	running_AB = False

#procurar intersecções entre A e C________________________________________________
indic_a = indic_c = 0
intersec_ac = []
running_AC = True
while running_AC:
    if count_c == -1:
        break
    if has_a[indic_a] == has_c[indic_c]:
        intersec_ac.append(str(has_a[indic_a]))
    if  count_a != 1:
        indic_a = indic_a + 1
    if indic_a == count_a or count_a == 1:
        if count_c == 1:
            running_AC = False
        indic_a = 0
        if count_c != 1:
            indic_c = indic_c + 1
    if indic_c == count_c and count_c != 1:
        running_AC = False

#procurar intersecções entre B e C________________________________________________
indic_b = indic_c = 0
intersec_bc = []
running_BC = True
while running_BC:
    if count_c == -1:
        break
    if has_b[indic_b] == has_c[indic_c]:
        intersec_bc.append(str(has_b[indic_b]))
    if  count_b != 1:
        indic_b = indic_b + 1
    if indic_b == count_b or count_b == 1:
        if count_c == 1:
            running_BC = False
        indic_b = 0
        if count_c != 1:
            indic_c = indic_c + 1
    if indic_c == count_c and count_c != 1:
        running_BC = False

#procurar intersecções entre A, B e C_____________________________________________
indic_a = indic_b = indic_c = 0
intersec_abc = []
running_ABC = True
while running_ABC:
    if count_c == -1:
        break
    if has_a[indic_a] == has_b[indic_b] == has_c[indic_c]:
        intersec_abc.append(str(has_a[indic_a]))
    if count_a != 1:
        indic_a = indic_a + 1
    if indic_a == count_a or count_a == 1:
        indic_a = 0
        if count_b != 1:
            indic_b = indic_b + 1 
        if indic_b == count_b or count_b == 1:
            indic_b = 0
            if count_c != 1:
                indic_c = indic_c + 1
                if indic_c == count_c:
                    running_ABC = False
            else:
                if count_c == 1:
                    running_ABC = False




if intersec_ab != []:
    intersec_ab = str(intersec_ab)
    count_intersec_ab = count_elements(intersec_ab)
    intersec_ab = format(intersec_ab)
    intersec_ab = cut_repetitions(intersec_ab, count_intersec_ab)
    count_intersec_ab = str(intersec_ab)
    count_intersec_ab = count_elements(count_intersec_ab)
    intersec_ab = format_after_cut_repetitions(intersec_ab)
    print("Intersecções entre A e B (A∩B):", "{", intersec_ab, "}.\n", "Total de", count_intersec_ab, "elemento(s).\n")

if intersec_ac != []:
    intersec_ac = str(intersec_ac)
    count_intersec_ac = count_elements(intersec_ac)
    intersec_ac = format(intersec_ac)
    intersec_ac = cut_repetitions(intersec_ac, count_intersec_ac)
    count_intersec_ac = str(intersec_ac)
    count_intersec_ac = count_elements(count_intersec_ac)
    intersec_ac = format_after_cut_repetitions(intersec_ac)
    print("Intersecções entre A e C (A∩C):", "{", intersec_ac, "}.\n", "Total de", count_intersec_ac, "elemento(s).\n")

if intersec_bc != []:
    intersec_bc = str(intersec_bc)
    count_intersec_bc = count_elements(intersec_bc)
    intersec_bc = format(intersec_bc)
    intersec_bc = cut_repetitions(intersec_bc, count_intersec_bc)
    count_intersec_bc = str(intersec_bc)
    count_intersec_bc = count_elements(count_intersec_bc)
    intersec_bc = format_after_cut_repetitions(intersec_bc)
    print("Intersecções entre B e C (B∩C):", "{", intersec_bc, "}.\n", "Total de", count_intersec_bc, "elemento(s).\n")

if intersec_abc != []:
    intersec_abc = str(intersec_abc)
    count_intersec_abc = count_elements(intersec_abc)
    intersec_abc = format(intersec_abc)
    intersec_abc = cut_repetitions(intersec_abc, count_intersec_abc)
    count_intersec_abc = str(intersec_abc)
    count_intersec_abc = count_elements(count_intersec_abc)
    intersec_abc = format_after_cut_repetitions(intersec_abc)
    print("Intersecções entre A, B e C (A∩B∩C):", "{", intersec_abc, "}.\n", "Total de", count_intersec_abc, "elemento(s).\n")
    
##############################################################################################################################

OU ????????????????????????????????

##############################################################################################################################

has_a = {}
has_b = {}
has_c = {}

indic_a = 0
count_a = -1

indic_b = 0
count_b = -1

indic_c = 0
count_c = -1

running = True
while running:
    print("Digite o", indic_a+1,"° elemento para o conjunto A ('b' para definir os elementos de B): ")
    has_a[indic_a] = str(input())
    if has_a[indic_a] == 'b':
        while running:
            print("Digite o", indic_b+1,"° elemento para o conjunto B ('c' para definir os elementos de C, 'q' para finalizar): ")
            has_b[indic_b] = str(input())
            if has_b[indic_b] == 'c':
                while running:
                    print("Digite o", indic_c+1,"° elemento para o conjunto C ('q' para finalizar): ")
                    has_c[indic_c] = str(input())
                    if has_c[indic_c] == 'q':
                        running = False
                    indic_c = indic_c + 1
                    count_c = count_c + 1
            if has_b[indic_b] == 'q':
                running = False
            indic_b = indic_b + 1
            count_b = count_b + 1
    indic_a = indic_a + 1
    count_a = count_a + 1

#remover caracteres:____________________________________________________
def chr_remove(old, to_remove):
    new_string = old
    for x in to_remove:
        new_string = new_string.replace(x,"")
        return new_string

print("__________________________________________________________________________________________________________________________\n\nUniões:")

num_x = 0
#___valores do hash do conjunto A → os elementos de A______
values = True
values_a = []
while values:
    values_a.append(str(has_a[num_x]))
    num_x = num_x + 1
    if num_x == count_a:
        num_x = 0
        values = False

#___valores do hash do conjunto B → os elementos de B______
values = True
values_b = []
while values:
    values_b.append(str(has_b[num_x]))
    num_x = num_x + 1
    if num_x == count_b:
        num_x = 0
        values = False

#___valores do hash do conjunto C → os elementos de C______
values = True
values_c = []
while values:
    if count_c != -1:
        values_c.append(str(has_c[num_x]))
        num_x = num_x + 1
        if num_x == count_c:
            num_x = 0
            values = False
    else:
        if count_c == -1:
            num_x = 0
            values = False

#_______________UNIÕES____________________________________________________
#___Contar e formatar as uniões para a chamada da função cut_repetitions()___
def count_elements(uni):
    #global aub
    uni = chr_remove(uni, "'")
    uni = chr_remove(uni, ",")
    uni = uni[1:-1]
    unity_count = str(uni)
    unity_count = len(unity_count.split())
    return(int(unity_count))

def format(uni):
    #global aub
    uni = chr_remove(uni, "'")
    uni = chr_remove(uni, ",")
    uni = uni[1:-1]
    uni = uni.split()
    return(uni)

#união de A e B (AUB) com elementos repetidos:
aub = str(values_a + values_b)
count_aub = count_elements(aub)
aub = format(aub)

#união de A e C (AUC) com elementos repetidos:
auc = str(values_a + values_c)
count_auc = count_elements(auc)
auc = format(auc)
	
#união de B e C (BUC) com elementos repetidos:
buc = str(values_b + values_c)
count_buc = count_elements(buc)
buc = format(buc)
	
#união de A, B e C (AUBUC) com elementos repetidos:
aubuc_not_formatted = str(values_a + values_b + values_c) 
aubuc = aubuc_not_formatted
count_aubuc = count_elements(aubuc)
aubuc = format(aubuc)
    
#função que retira elementos repetidos das uniões
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

#____________________________chamada da função cut_repetitions____________________________
def format_after_cut_repetitions(conj):
    conj = tuple(conj)
    conj = sorted(conj)
    conj = str(conj)
    conj = conj[1:-1]
    conj = chr_remove(conj, "'")
    return(conj)

#A sem elementos repetidos
a = cut_repetitions(values_a, count_a)
conj_a = format_after_cut_repetitions(a)
a = str(a)
count_a_after_cut = count_elements(a)
print("Elementos de A:", "{", conj_a, "}.\n", "Total de", count_a_after_cut, "elemento(s).\n")

#B sem elementos repetidos 
b = cut_repetitions(values_b, count_b)
conj_b = format_after_cut_repetitions(b)
b = str(b)
count_b_after_cut = count_elements(b)
print("Elementos de B:", "{", conj_b, "}.\n", "Total de", count_b_after_cut, "elemento(s).\n")

#AUB sem elementos repetidos
aub = cut_repetitions(aub, count_aub)
conj_aub = format_after_cut_repetitions(aub)
aub = str(aub)
count_aub_after_cut = count_elements(aub)
print("União de A e B (AUB):", "{", conj_aub, "}.\n", "Total de", count_aub_after_cut, "elemento(s).\n")

if count_c > 0:
    #C sem elementos repetidos 
    c = cut_repetitions(values_c, count_c)
    conj_c = format_after_cut_repetitions(c)
    c = str(c)
    count_c_after_cut = count_elements(c)
    print("Elementos de C:", "{", conj_c, "}.\n", "Total de", count_c_after_cut, "elemento(s).\n")
    
    #AUC sem elementos repetidos 
    auc = cut_repetitions(auc, count_auc)
    conj_auc = format_after_cut_repetitions(auc)
    auc = str(auc)
    count_auc_after_cut = count_elements(auc)
    print("União de A e C (AUC):", "{", conj_auc, "}.\n", "Total de", count_auc_after_cut, "elemento(s).\n")
	
    #BUC sem elementos repetidos 
    buc = cut_repetitions(buc, count_buc)
    conj_buc = format_after_cut_repetitions(buc)
    buc = str(buc)
    count_buc_after_cut = count_elements(buc)
    print("União de B e C (BUC):", "{", conj_buc, "}.\n", "Total de", count_buc_after_cut, "elemento(s).\n")
	
    #AUBUC sem elementos repetidos 
    aubuc = cut_repetitions(aubuc, count_aubuc)
    conj_aubuc = format_after_cut_repetitions(aubuc)
    aubuc = str(aubuc)
    count_aubuc_after_cut = count_elements(aubuc)
    print("União de A, B e C (AUBUC):", "{", conj_aubuc, "}.\n", "Total de", count_aubuc_after_cut, "elemento(s).\n")

print("__________________________________________________________________________________________________________________________\n\nintersecções:")

#procurar intersecções entre A e B________________________________________________
indic_a = indic_b = 0
intersec_ab = []
running_AB = True
while running_AB:
    if has_a[indic_a] == has_b[indic_b]:
        intersec_ab.append(str(has_a[indic_a]))
    if  count_a != 1:
        indic_a = indic_a + 1
    if indic_a == count_a or count_a == 1:
        if count_b == 1:
            running_AB = False
        indic_a = 0
        if count_b != 1:
            indic_b = indic_b + 1
    if indic_b == count_b and count_b != 1:
    	running_AB = False

#procurar intersecções entre A e C________________________________________________
indic_a = indic_c = 0
intersec_ac = []
running_AC = True
while running_AC:
    if count_c == -1:
        break
    if has_a[indic_a] == has_c[indic_c]:
        intersec_ac.append(str(has_a[indic_a]))
    if  count_a != 1:
        indic_a = indic_a + 1
    if indic_a == count_a or count_a == 1:
        if count_c == 1:
            running_AC = False
        indic_a = 0
        if count_c != 1:
            indic_c = indic_c + 1
    if indic_c == count_c and count_c != 1:
        running_AC = False

#procurar intersecções entre B e C________________________________________________
indic_b = indic_c = 0
intersec_bc = []
running_BC = True
while running_BC:
    if count_c == -1:
        break
    if has_b[indic_b] == has_c[indic_c]:
        intersec_bc.append(str(has_b[indic_b]))
    if  count_b != 1:
        indic_b = indic_b + 1
    if indic_b == count_b or count_b == 1:
        if count_c == 1:
            running_BC = False
        indic_b = 0
        if count_c != 1:
            indic_c = indic_c + 1
    if indic_c == count_c and count_c != 1:
        running_BC = False

#procurar intersecções entre A, B e C_____________________________________________
indic_a = indic_b = indic_c = 0
intersec_abc = []
running_ABC = True
while running_ABC:
    if count_c == -1:
        break
    if has_a[indic_a] == has_b[indic_b] == has_c[indic_c]:
        intersec_abc.append(str(has_a[indic_a]))
    if count_a != 1:
        indic_a = indic_a + 1
    if indic_a == count_a or count_a == 1:
        indic_a = 0
        if count_b != 1:
            indic_b = indic_b + 1 
        if indic_b == count_b or count_b == 1:
            indic_b = 0
            if count_c != 1:
                indic_c = indic_c + 1
                if indic_c == count_c:
                    running_ABC = False
            else:
                if count_c == 1:
                    running_ABC = False

if intersec_ab != []:
    intersec_ab = str(intersec_ab)
    count_intersec_ab = count_elements(intersec_ab)
    intersec_ab = format(intersec_ab)
    intersec_ab = cut_repetitions(intersec_ab, count_intersec_ab)
    count_intersec_ab = str(intersec_ab)
    count_intersec_ab = count_elements(count_intersec_ab)
    intersec_ab = format_after_cut_repetitions(intersec_ab)
    print("Intersecções entre A e B (A∩B):", "{", intersec_ab, "}.\n", "Total de", count_intersec_ab, "elemento(s).\n")

if intersec_ac != []:
    intersec_ac = str(intersec_ac)
    count_intersec_ac = count_elements(intersec_ac)
    intersec_ac = format(intersec_ac)
    intersec_ac = cut_repetitions(intersec_ac, count_intersec_ac)
    count_intersec_ac = str(intersec_ac)
    count_intersec_ac = count_elements(count_intersec_ac)
    intersec_ac = format_after_cut_repetitions(intersec_ac)
    print("Intersecções entre A e C (A∩C):", "{", intersec_ac, "}.\n", "Total de", count_intersec_ac, "elemento(s).\n")

if intersec_bc != []:
    intersec_bc = str(intersec_bc)
    count_intersec_bc = count_elements(intersec_bc)
    intersec_bc = format(intersec_bc)
    intersec_bc = cut_repetitions(intersec_bc, count_intersec_bc)
    count_intersec_bc = str(intersec_bc)
    count_intersec_bc = count_elements(count_intersec_bc)
    intersec_bc = format_after_cut_repetitions(intersec_bc)
    print("Intersecções entre B e C (B∩C):", "{", intersec_bc, "}.\n", "Total de", count_intersec_bc, "elemento(s).\n")

if intersec_abc != []:
    intersec_abc = str(intersec_abc)
    count_intersec_abc = count_elements(intersec_abc)
    intersec_abc = format(intersec_abc)
    intersec_abc = cut_repetitions(intersec_abc, count_intersec_abc)
    count_intersec_abc = str(intersec_abc)
    count_intersec_abc = count_elements(count_intersec_abc)
    intersec_abc = format_after_cut_repetitions(intersec_abc)
    print("Intersecções entre A, B e C (A∩B∩C):", "{", intersec_abc, "}.\n", "Total de", count_intersec_abc, "elemento(s).\n")

'''

mainloop()