# A sequência de Fibonacci descrita pelo matemático italiano Leonardo de Pisa (1170-1250), conhecido como Fibonacci, é composta 
# por uma sucessão de números onde os números seguintes serão a soma dos dois números anteriores, desta forma: 
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6.765, 10.946, 17.711...
# A partir do número 3, o coeficiente de um número com o seu anterior, será aproximadamente 1.618033988749895(infinito), quanto 
# maior o índice da sequência, mais a divisão entre um termo e seu antecessor fica próxima a esse valor. Esse número é conhecido 
# como “número de ouro” ou “proporção áurea”, representado pela letra grega Fi (maiúscula Φ, minúsculas φ ou ϕ; em grego: φι, 
# transl.: phi) é a vigésima-primeira letra do alfabeto grego. ϕ = 1.618033988749895

#Exemplo:
#   c: --------------------- (a+b): 21
#   a: -------------           a:   13
#   b: --------                b:    8
# phi: --                    (c/a): 1.6180339887498947

#para entrada com a_________________________
a = float(input("digite o valor de a: "))
print("valor de a: ", a)

# phi = (a + b)/a 
# a * phi = (a + b)
# a * phi - a = b
# b = a * phi - a
b = float(a * (1.618033988749895) - a)
print("valor de b: ", b)

c = float(a + b)
print("valor de c: ", c)
phi = float(c / a)
print("phi: ", phi)

#para entrada com b_________________________
b = float(input("digite o valor de b: "))

# phi = (a + b)/a
# a + b = phi*a
# a = phi*a - b
# a -phi*a = -b
# 1*a -1.618*a = -b 

# -0.618*a = -b
# a = b/0.618033988749895
phi_false = float(0.618033988749895)
a = float((b)/phi_false)
print("valor de a: ", a)

print("valor de b: ", b)

c = float(a + b)
print("valor de c: ", c)
phi = float(c / a)
print("phi: ", phi)

#para entrada com c_________________________
c = float(input("digite o valor de c: "))

a = float(c/1.618033988749895)
print("valor de a: ", a)

b = float(c - a)
print("valor de b: ", b)

print("valor de c: ", c)

phi = float(c / a)
print("phi: ", phi)
