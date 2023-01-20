from classe import Carrinho, Produto

carrinho = Carrinho()

resposta = input('Deseja adicionar um item ao carrinho? ')
c = 0
while resposta.lower() != 'nao':
    c += 1
    compra = input('Qual o nome do produto que deseja comprar?')
    preco = float(input('Qual o valor desse produto? '))
    produto = Produto(compra, preco)
    carrinho.adicionar_produto(produto)
    resposta = input('Deseja adicionar mais um item ao carrinho? ')
    if resposta.lower() == 'nao':
        resposta2 = input('Deseja retirar algum produto do carrinho? ')
        if resposta2.lower() == 'sim':
            carrinho.mostrar_produtos()
            resposta3 = int(input('Qual produto deseja retirar(informe seu número na lista): '))
            carrinho.remover_produto(resposta3)
            resposta2 = input('Deseja retirar mais algum produto do carrinho? ')
        carrinho.mostrar_produtos()
        print(f'A soma total é de: R${carrinho.soma_total()}')






