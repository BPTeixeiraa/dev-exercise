#!/usr/bin/python
#*****************************************************************************************************************************************************
# Linguagem ..........: Python
# Criado por..........: Bruno Teixeira
# Data da Criação.....: 10/02/2021
# Exercicios...........: Pensando em todos os números naturais inferiores a 10 que são múltiplos de 3 ou 5, temos 3, 5, 6 e 9.
# Somando esses múltiplos obtemos o valor 23. Utilize um algorítimo para calcular a soma de todos os múltiplos de 3 ou 5 abaixo de 1000.
#*****************************************************************************************************************************************************
# Criando função generica para calcular a soma de todos os números naturais inferiores ao 'Limite' que são multiplos de 'multiplos'

def sum_multiplos(multiplos, limite):
    """
    :param multiplos: int ou lista de int
    :param limite: número que servira como limite para realizar o cálculo.
    :return:  int contendo a Soma de todos os múltiplos de 'multiplos' abaixo do 'limite', onde multiplo pode ser um int ou uma lista de int
    """
    if isinstance(limite, int) and isinstance (multiplos, (int, list, tuple)):
         sum = 0
         if isinstance(multiplos, int):
             for num in range(limite):
                 if num % multiplos == 0:
                     sum = sum + num
         else:
             for num in range(limite):
                 for multiplo in multiplos:
                     if num % multiplo == 0:
                         sum = sum + num
                         break
         return sum
    raise Exception("o parametro limite deve ser um 'int' e 'multiplos' deve ser um int ou uma lista/tupla de int")
multiplos = (3,5)
limite = 1000
print(f"A soma de todos os múltiplos de {multiplos} abaixo de {limite} é: {sum_multiplos(multiplos, limite)}")

# O exemplo acima da chamada da função sum_multiplos retorna o mesmo resultado do trecho comentado abaixo que é a soma de todos os múltiplos de 3 ou 5 abaixo de 1000.
#soma = 0
#for item in range(1000):
#    if (item % 3 == 0) or (item % 5 == 0):
#        soma = soma + item
#print (soma)