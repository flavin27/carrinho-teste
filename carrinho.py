class Carrinho:
    def __init__(self):
        self.lista_carrinho = []
    def adiciona_produto(self, produto, preco=0):
        compra = {'Produto:': (produto), 'Preço: ': float(preco)}
        self.lista_carrinho.append(compra)
        compra = None
        soma += preco
    def mostrar_lista(self):
        print(self.lista_carrinho)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

