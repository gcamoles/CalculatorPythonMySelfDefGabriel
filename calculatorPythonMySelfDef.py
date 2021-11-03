#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#oficial
print ("\nCalculadora Python")

def addNum(x, y):
    return x + y

def subNum(x, y):
    return x - y

def multNum(x, y):
    return x * y

def divNum(x, y):
    return x / y

print("\nSelecione o número da operação deseada: \n")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")

opcao = input('\nDigite sua opção (1/2/3/4): ')

x = float(input('\nDigite o primeiro número: '))
y = float(input('\nDigite o segundo número: '))

if opcao == '1':
    print("\n")
    print(x, "+", y, "=", addNum(x, y))
    print("\n")
elif opcao == '2':
    print("\n")
    print(x, "-", y, "=", subNum(x, y))
    print("\n")
elif opcao == '3':
    print("\n")
    print(x, "*", y, "=", multNum(x, y))
    print("\n")
elif opcao == '4':
    print("\n")
    print(x, "/", y, "=", divNum(x, y))
    print("\n")
else:
    print("\nOpção inválida!")

