# Crie uma classe CarrinhoDeCompras onde os atributos serão duas listas, uma para os produtos e outra para seus respectivos preços, se o cliente é VIP ou não e o total da compra que deve ser iniciado com 0.0.
# Em seguida, crie os métodos para adicionar produtos ao carrinho e o exibir total da compra, que deverá imprimir em tela todos os produtos, os preços e, por fim, o total. Se o cliente for VIP, a compra terá 10% de desconto.

class CarrinhoCompras:
    
    def __init__(self, isVip):
        self.__isVip = isVip
        self.__dictProdutos = {}
        self.__total = 0
        
    def adicionarProduto(self,nome,preco):
        self.__dictProdutos[nome] = preco    
    
    def exibirTotalCompra(self):
        total = 0
        for item in self.__dictProdutos.items():
            nomeProduto = item[0]
            precoProduto = item[1]
            total +=precoProduto
            print(f"O Produto {nomeProduto} possui o preço {precoProduto}")
    
        if(self.__isVip == True):
            self.__total = total - (total * 0.1)
        else:
            self.__total = total

        print(f"O total é {self.__total}")
            
    def getIsVip(self):
        return self.__isVip
    
    def setIsVip(self, isVip):
        self.__isVip = isVip
        
    def getDictProdutos(self):
        return self.__dictProdutos
    
    def setDictProdutos(self, dictProdutos):
        self.__dictProdutos = dictProdutos  
        
    def getTotal(self):
        return self.__total
    
    def setTotal(self, total):
        self.__total = total    