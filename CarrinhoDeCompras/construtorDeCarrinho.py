from carrinhoCompras import CarrinhoCompras

vip = input("O cliente é vip (S/N)")

if(vip == 'S'):
    vipBoolean = True
else:
    vipBoolean = False
    
carrinho = CarrinhoCompras(vipBoolean)

while(True):
    nomeProduto = input("Digite o nome do produto")
    valorProduto = float(input("Digite o valor do produto"))

    carrinho.adicionarProduto(nomeProduto,valorProduto)
    
    opcao = input("Deseja cadastrar mais produtos (S/N")
    if(opcao == 'N'):
        break

carrinho.exibirTotalCompra()    