from datetime import datetime

class Categoria:
    def __init__(self,categoria):
        self.categoria = categoria

class Produtos:
    def __init__(self, nome, preço, categoria):
        self.nome = nome
        self.preço = preço
        self.categoria = categoria

class Estoque:
    def __init__(self, produto: Produtos, quantidade):
        self.produto = produto
        self.quantidade = quantidade

class Venda:
    def __init__(self, itensVendidos: Produtos, vendedor, comprador, quantidadeVendida, data = datetime.now().strftime("%d/%m/%Y")):
        self.itensVendidos = itensVendidos
        self.vendedor = vendedor
        self.comprador = comprador
        self.quantidadeVendida = quantidadeVendida
        self.data = data

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, categoria):
        self.nome = nome
        self.cnpj = cnpj
        self.categoria = categoria
        self.telefone = telefone

class Pessoa:
    def __init__(self, nome, cpf, telefone, email, endereço):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereço = endereço

class Funcionario(Pessoa):
    def __init__(self, clt, nome, telefone, cpf, email, endereço):
        self.clt = clt
        super(Funcionario, self).__init__(nome, cpf, telefone, email, endereço)