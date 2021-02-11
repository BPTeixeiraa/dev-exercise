#!/usr/bin/python
#*****************************************************************************************************************************************************
# Linguagem ..........: Python
# Criado por..........: Bruno Teixeira
# Data da Criação.....: 10/02/2021
# Exercicios...........: Crie uma classe contendo 3 propriedades com seus respectivos gets e sets e um método que multiplique
# as 3 retornando o produto. Deixe um exemplo de utilização da sua classe no final do código.
#*****************************************************************************************************************************************************

class POO_Exemplo:
    def __init__(self):
        # iniciando em 1 para não dar erro na multiplicação caso passe menos de 3 números.
        self.propriedade_1 = 1
        self.propriedade_2 = 2
        self.propriedade_3 = 3

    def getPropriedade1(self):
        """
        :return: Retorna o valor do atributo propriedade_1
        """
        return self.propriedade_1

    def getPropriedade2(self):
        """
        :return: Retorna o valor do atributo propriedade_2
        """
        return self.propriedade_2

    def getPropriedade3(self):
        """
        :return: Retorna o valor do atributo propriedade_3
        """
        return self.propriedade_3

    def setPropriedade1(self, num):
        '''
        :param num: numero float ou in
        :return: atribui o valor passado por parametro para o atributo propriedade_1
        '''
        if isinstance(num, (int, float)):
            self.propriedade_1 = num
            return True
        return False

    def setPropriedade2(self, num):
        '''
        :param num: numero float ou in
        :return: atribui o valor passado por parametro para o atributo propriedade_2
        '''
        if isinstance(num, (int, float)):
            self.propriedade_2 = num
            return True
        return False

    def setPropriedade3(self, num):
        '''
        :param num: numero float ou in
        :return: atribui o valor passado por parametro para o atributo propriedade_3
        '''
        if isinstance(num, (int, float)):
            self.propriedade_3 = num
            return True
        return False

    def produto(self):
        """
        :return: Retorna o produto dos atributos propriedade_1, propriedade_2 e propriedade_3.
        """
        return self.getPropriedade1() * self.getPropriedade2() * self.getPropriedade3()


# Exemplo de utilização da classe criada
if __name__ == "__main__":
    Exemplo_POO  = POO_Exemplo()
    # Atribuindo o balor 10 ao 1º atributo
    Exemplo_POO.setPropriedade1(10)
    # Atribuindo o balor 20 ao 2º atributo
    Exemplo_POO.setPropriedade2(20)
    # Atribuindo o balor 30 ao 3º atributo
    Exemplo_POO.setPropriedade3(30)
    # Exibindo informação da 1º propriedade
    print (f"propriedade_1 = {Exemplo_POO.getPropriedade1()}")
    # Exibindo informação da 2º propriedade
    print (f"propriedade_2 = {Exemplo_POO.getPropriedade2()}")
    # Exibindo informação da 3º propriedade
    print (f"propriedade_3 = {Exemplo_POO.getPropriedade3()}")
    # Exibindo resultado do método que retorna o produto dos atributos propriedade_1, propriedade_2 e propriedade_3
    print (f"Produto = {Exemplo_POO.produto()}")
