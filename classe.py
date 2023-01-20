class Carrinho:
    def __init__(self):
        self.produtos  = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)

    def remover_produto(self, pos):
        self.produtos.pop(pos)
        self.c -= 1

    def mostrar_produtos(self):
        self.c = -1
        for produto in self.produtos:
            self.c += 1
            print(self.c, '-', produto.nome, produto.valor)
    
    def soma_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.valor
        return total



class Produto:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
