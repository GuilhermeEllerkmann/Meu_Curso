class Carrinho:
    def __init__(self):
        self._produtos = []

    def total(self):
        return sum([p.preco for p in self._produtos])
    
    def insere_produtos(self, *args):
        self._produtos.extend(args)
    
    def listar_produtos(self):
        print()
        for produto in self._produtos:
            print(produto.produto, produto.preco)
        print()


class Produtos:
    def __init__(self, produto, preco):
        self.produto = produto
        self.preco = preco


carrinho = Carrinho()
p1, p2 = Produtos('Camisinha', 30), Produtos('Lub', 30)
carrinho.insere_produtos(p1,p2)
carrinho.listar_produtos()
print(carrinho.total())
