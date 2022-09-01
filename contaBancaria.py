class ContaBancaria:

    def __init__(self, agencia, conta, favorecido):
        self.agencia = agencia
        self.conta = conta
        self.__favorecido = favorecido
        self.__saldo = 0