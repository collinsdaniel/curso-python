from data import Data


class Conta:

    def __init__(self, numero, titular, saldo, limite=1000.0):
        print("Construindo objeto ... {}".format(self))

        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {} na data {} ".format(self.__saldo, self.__titular, Data(1, 1, 2020).formatar()))

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor
