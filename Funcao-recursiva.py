#!/usr/bin/python
#*****************************************************************************************************************************************************
# Linguagem ..........: Python
# Criado por..........: Bruno Teixeira
# Data da Criação.....: 10/02/2021
# Exercicios...........: Crie uma função recursiva para descobrir o menor número inteiro divisível por 2, 3 e 10 ao mesmo tempo.
# Quando encontrá-lo, imprima-o na tela.
#*****************************************************************************************************************************************************
def recursiva(n=1):
    '''
    :param n: número que será incrementado para utilização na função de forma recursiva.
    :return: retorna o menor número inteiro divisível por 2, 3 e 10.
    '''
    if n % 2 == 0 and n % 3 == 0 and n % 10 == 0:
        return n
    else:
        return recursiva(n + 1)
print(f"O número {recursiva()} é o menor número inteiro divisivel por 2, 3 e 10 ao mesmo tempo.")