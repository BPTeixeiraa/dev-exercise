#!/usr/bin/python
#*****************************************************************************************************************************************************
# Linguagem ..........: Python
# Criado por..........: Bruno Teixeira
# Data da Criação.....: 10/02/2021
# Exercicios...........: Tendo os arrays ['ES', 'MG', 'RJ', 'SP', 'MT'] e ['Mato Grosso', 'São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo'],
# percorra os vetores dados e crie um outro com a seguinte estrutura: ['MT' => ''Mato Grosso'', 'ES'=>'Espírito Santo', 'MG'=>'Minas Gerais', 'RJ'=>'Rio de Janeiro', 'SP'=>'São Paulo'].
# Depois de criado terceiro vetor, leia-o e imprima em cada linha a chave de cada posição e seu respectivo valor separados por "-".
#*****************************************************************************************************************************************************
# Fiz a solução do exercicio utilizando 2 métodos (a e b), o primeiro foi utilizando 2 funções built-in e o segundo somente usando estrutura de repetição.

uf_cidade  = ['Mato Grosso', 'São Paulo', 'Rio de Janeiro', 'Minas Gerais', 'Espírito Santo']
uf_sigla  = ['ES', 'MG', 'RJ', 'SP', 'MT']

# Usando funções built-in do python: dict e zip
print ("\na) Usando funções built-in do python: dict e zip")
uf = dict(zip(uf_sigla, uf_cidade[::-1]))
for x, i in enumerate(uf):
    print (f"{i}-{uf[i]}")

# Usando somente estrutura de repetição
print ("\nb) Usando somente estrutura de repetição")
uf = {}
for i, s in enumerate(uf_sigla[::-1]):
    uf[s] = uf_cidade[i]
for sigla, cidade in uf.items():
    print(f"{sigla}-{cidade}")