from classe import Carrinho, Produto

carrinho = Carrinho()

p1 = Produto('camisa', 50)
p2 = Produto('chocolate', 10)
p3 = Produto('PS4', 2000)

carrinho.adicionar_produto(p1)
carrinho.adicionar_produto(p2)
carrinho.adicionar_produto(p3)
carrinho.mostrar_produtos()
print(carrinho.soma_total())