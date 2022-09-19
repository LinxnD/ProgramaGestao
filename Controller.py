from Models import *
from DAO import *
from datetime import datetime

class ControllerCategoria():
    def cadastraCategoria(self, novaCategoria):
        existe = False
        x = DaoCategoria.ler()
        for i in x:
            if i.categoria == novaCategoria:
                existe = True

        if not existe:
            DaoCategoria.salvar(novaCategoria)
            print('Categoria cadastrada com sucesso')
        else:
            print('A categoria que deseja cadastrar já existe')

    def removeCategoria(self, categoriaRemover):
        x = DaoCategoria.ler()
        cat = list(filter(lambda x: x.categoria == categoriaRemover, x))

        if len(cat) <= 0:
            print('A categoria que deseja remover não existe.')
        else:
            for i in range(len(x)):
                if x[i].categoria == categoriaRemover:
                    del x[i]
                    break
            print('categoria removida com sucesso.')

            with open('categoria.txt', 'w')as arq:
                for i in x:
                    arq.writelines(i.categoria)
                    arq.writelines('\n')


        estoque = DaoEstoque.ler()
        estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preço, 'Sem categoria'), x.quantidade)
                                    if(x.produto.categoria == categoriaRemover) else(x), estoque))
        
        with open('estoque.txt', 'w')as arq:
            for i in estoque:
                arq.writelines(i.produto.nome +"|"+ i.produto.preço +"|"+
                           i.produto.categoria +"|"+ str(i.quantidade))
                arq.writelines('\n')

    def alteraCategoria(self, categoriaAlterar, categoriaAlterada):
        x = DaoCategoria.ler()

        cat = list(filter(lambda x: x.categoria == categoriaAlterar, x))

        if len(cat) > 0:
            cat1 = list(filter(lambda x: x.categoria == categoriaAlterada, x))
            if len(cat1) == 0:
                x = list(map(lambda x: Categoria(categoriaAlterada) if(x.categoria == categoriaAlterar) else(x), x))
                print('Categoria alterada com sucesso.')
                estoque = DaoEstoque.ler()
                estoque = list(map(lambda x: Estoque(Produtos(x.produto.nome, x.produto.preço, categoriaAlterada), x.quantidade)
                                            if(x.produto.categoria == categoriaAlterar) else(x), estoque))
        
                with open('estoque.txt', 'w')as arq:
                    for i in estoque:
                        arq.writelines(i.produto.nome +"|"+ i.produto.preço +"|"+
                                i.produto.categoria +"|"+ str(i.quantidade))
                        arq.writelines('\n')
            else:
                print('A categoria para qual vc deseja alterar já existe.')

        else:
            print('A categoria que deseja alterar não existe.')

        with open('categoria.txt' , 'w')as arq:
            for i in x:
                arq.writelines(i.categoria)
                arq.writelines('\n')

    def mostrarCategoria(self):
        categoria = DaoCategoria.ler()
        if len(categoria) == 0:
            print('Categoria vazia.')
        else:
            for i in categoria:
                print(f'Categoria: {i.categoria}')

class ControllerEstoque():
    def cadastraProduto(self, nome, preço, categoria, quantidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == categoria, y))
        est = list(filter(lambda x: x.produto.nome == nome, x))

        if len(h) > 0:
            if len(est) == 0:
                produtos = Produtos(nome, preço, categoria)
                DaoEstoque.salvar(produtos, quantidade)
                print('Produto cadastrado com sucesso.')
            else:
                print('Produto ja existe em estoque.')
        else:
            print('Categoria inexistente.')
    #N da para cadastrar se n tiver nd no 'estoque.txt'
    def removerProduto(self, nome):
        x = DaoEstoque.ler()
        est = list(filter(lambda x: x.produto.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].produto.nome == nome:
                    del x[i]
                    break
            print('O produto foi removido com sucesso.')
        else:
            print('O produto q deseja remover não existe.')
        
        with open('estoque.txt', 'w')as arq:
            for i in x:
                arq.writelines(i.produto.nome +"|"+ i.produto.preço +"|"+
                           i.produto.categoria +"|"+ str(i.quantidade))
            arq.writelines('\n')

    def alterarEstoque(self, nomeAlterar, novoNome, novoPreço, novaCategoria, novaQuatidade):
        x = DaoEstoque.ler()
        y = DaoCategoria.ler()
        h = list(filter(lambda x: x.categoria == novaCategoria, y))
        if len(h) > 0:
            est = list(filter(lambda x: x.produto.nome == nomeAlterar, x))
            if len(est) > 0:
                est = list(filter(lambda x: x.produto.nome == novoNome, x))
                if len(est) == 0:
                    x = list(map(lambda x: Estoque(Produtos(novoNome, novoPreço, novaCategoria), novaQuatidade)if (x.produto.nome == nomeAlterar)else(x), x))
                    print('Produto alterado com sucesso.')
                else:
                    print('Produto ja cadastrado')
            else:
                print('O produto que deseja alterar não existe.')
            with open('estoque.txt', 'w')as arq:
                for i in x:
                    arq.writelines(i.produto.nome +"|"+ i.produto.preço +"|"+
                            i.produto.categoria +"|"+ str(i.quantidade))
                    arq.writelines('\n')

        else:
            print('A categoria informada não existe.')

    def mostrarEstoque(self):
        x = DaoEstoque.ler()
        if len(x) == 0:
            print('Estoque vazio.')
        else:
            print('=====-====-==PRODUTOS=====-====-==')
            for i in x:               
                print(f'Nome:{i.produto.nome}')
                print(f'Preço:{i.produto.preço}')
                print(f'Categoria:{i.produto.categoria}')
                print(f'Quantidade:{i.quantidade}')


                print('----------------------')
           
class ControllerVenda():
    def cadastrarVenda(self, nomeProduto, vendedor, comprador, quantidadeVendida):
        x = DaoEstoque.ler()
        temp = []
        existe = False
        quantidade= False

        for i in x:
            if existe == False:
                if i.produto.nome == nomeProduto:
                    existe = True
                    if i.quantidade >= quantidadeVendida:
                        quantidade = True
                        i.quantidade = int(quantidade) - int(quantidadeVendida)
                        
                        vendido = Venda(Produtos(i.produto.nome, i.produto.preço, i.produto.categoria), vendedor, comprador, quantidadeVendida)
                        
                        valorCompra = int(quantidadeVendida) * int(i.produto.preço)
                        
                        DaoVenda.salvar(vendido)

            temp.append(Estoque(Produtos(i.produto.nome, i.produto.preço, i.produto.categoria), i.quantidade))

        arq = open('estoque.txt', 'w')
        arq.write("")

        for i in temp:
            with open('estoque.txt', 'a')as arq:
                arq.writelines(i.produto.nome +'|'+ i.produto.preço +'|'+ i.produto.categoria +'|'+ str(i.quantidade))
                arq.writelines('\n')

        if existe == False:
            print('O produto não existe.')
            return None 
        elif not quantidade:
            print('Quantidade fora do estoque.')
            return None
        else:
            return valorCompra

    def relatorioVendas(self):
        vendas = DaoVenda.ler()
        produtos = []
        
        for i in vendas:
            nome = i.itensVendidos.nome
            quantidade = i.quantidadeVendida
            tamanho = list(filter(lambda x: x['produto'] == nome, produtos))
            if len(tamanho) > 0:
                produtos = list(map(lambda x: {'produto': nome,'quantidade': int(x['quantidade']) + int(quantidade)}
                if x['produto'] == nome else(x), produtos))
            else:
                produtos.append({'produto': nome,'quantidade': int(quantidade)})

        ordenado = sorted(produtos, key=lambda k: k['quantidade'], reverse=True)

        print('Esses são os produtos mais vendidos.')
        a = 1
        for i in ordenado:
            print(f'========== Produto [{a}] ==========')
            print(f"Produto {i['produto']}\n"
                    f"Quantidade {i['quantidade']}\n")
            
            a += 1

    def mostrarVenda(self, dataInicio, dataTermino):
        vendas = DaoVenda.ler()
        dataInicio1 = datetime.strptime(dataInicio, '%d/%m/%Y')
        dataTermino1 = datetime.strptime(dataTermino, '%d/%m/%Y')

        vendasSelecionadas = list(filter(lambda x: datetime.strptime(x.data, '%d/%m/%Y') >= dataInicio1 and 
                                                   datetime.strptime(x.data, '%d/%m/%Y') <= dataTermino1, vendas))

        cont = 1
        total = 0 

        for i in vendasSelecionadas:
            print(f'========== Venda {cont}==========')
            print(f'Nome: {i.itensVendidos.nome}\n'
                  f'Categoria: {i.itensVendidos.categoria}\n'
                  f'data: {i.data}\n'
                  f'QuantidadeVendida: {i.quantidadeVendida}\n'
                  f'Vendedor: {i.vendedor}\n'
                  f'Comprador: {i.comprador}\n')

            total += int(i.itensVendidos.preço) * int(i.quantidadeVendida)
            cont += 1

        print(f'Total vendido: {total}')

class ControllerFornecedor():
    def cadastraFornecedor(self, nome, cnpj, telefone, categoria):
        x = DaoFornecedor.ler()
        listaCnpj = list(filter(lambda x: x.cnpj == cnpj, x))
        listaTelefone = list(filter(lambda x: x.telefone == telefone, x))
        if len(listaCnpj) > 0:
            print('O CNPJ já existe.')
        elif len(listaTelefone) > 0:
            print('O telefone já existe.')
        else:
            if len(cnpj) == 14 and len(telefone) <= 11 and len(telefone) >= 10:
                DaoFornecedor.salvar(Fornecedor(nome, cnpj, telefone, categoria))
            else:
                print('Digite um CNPJ e um telefone vaido.')

    def removerFornecedor(self, nome):
        x = DaoFornecedor.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('O fornecedor que deseja remover não existe')
            return None

        with open('fornecedores.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.cnpj + "|" + i.telefone + "|" + str(i.categoria))
                arq.writelines('\n')
            print('Fornecedor removido com sucesso')

    def mostrarFornecedores(self):
        fornecedores = DaoFornecedor.ler()
        if len(fornecedores) == 0:
            print("Lista de fornecedores vazia")

        for i in fornecedores:
            print("=========Fornecedores==========")
            print(f"Categoria fornecida: {i.categoria}\n"
                  f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Cnpj: {i.cnpj}")

class ControllerCliente:
    def cadastrarCliente(self, nome, telefone, cpf, email, endereco):
        x = DaoPessoa.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        if len(listaCpf) > 0:
            print('CPF já existente')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                DaoPessoa.salvar(Pessoa(nome, telefone, cpf, email, endereco))
                print('Cliente Cadastrado com sucesso')
            else:
                print('digite um cpf ou telefone válido')

    def alterarCliente(self, nomeAlterar, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Pessoa(novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if (
                        x.nome == nomeAlterar) else (x), x))
        else:
            print('O cliente que deseja alterar nao existe')

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('cliente alterado com sucesso')

    def removerCliente(self, nome):
        x = DaoPessoa.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('O cliente que deseja remover não existe')
            return None

        with open('clientes.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('Cliente removido com sucesso')

    def mostrarClientes(self):
        clientes = DaoPessoa.ler()

        if len(clientes) == 0:
            print("Lista de clientes vazia")

        for i in clientes:
            print("=========Cliente=========")
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Endereço: {i.endereco}\n"
                  f"Email: {i.email}\n"
                  f"CPF: {i.cpf}")

class ControllerFuncionario:
    def cadastrarFuncionario(self, clt, nome, telefone, cpf, email, endereco):
        x = DaoFuncionario.ler()

        listaCpf = list(filter(lambda x: x.cpf == cpf, x))
        listaClt = list(filter(lambda x: x.clt == clt, x))
        if len(listaCpf) > 0:
            print('CPF já existente')
        elif len(listaClt) > 0:
            print('Já existe um funcionario com essa clt')
        else:
            if len(cpf) == 11 and len(telefone) >= 10 and len(telefone) <=11:
                DaoFuncionario.salvar(Funcionario(clt, nome, telefone, cpf, email, endereco))
                print('Funcionario Cadastrado com sucesso')
            else:
                print('digite um cpf ou telefone válido')

    def alterarFuncionario(self, nomeAlterar, novoClt, novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nomeAlterar, x))
        if len(est) > 0:
            x = list(map(lambda x: Funcionario(novoClt,novoNome, novoTelefone, novoCpf, novoEmail, novoEndereco) if (
                    x.nome == nomeAlterar) else (x), x))
        else:
            print('O funcionario que deseja alterar nao existe')

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.clt + "|" + i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email
                               + "|" + i.endereco)
                arq.writelines('\n')
            print('funcionario alterado com sucesso')

    def removerFuncionario(self, nome):
        x = DaoFuncionario.ler()

        est = list(filter(lambda x: x.nome == nome, x))
        if len(est) > 0:
            for i in range(len(x)):
                if x[i].nome == nome:
                    del  x[i]
                    break
        else:
            print('O funcionario que deseja remover não existe')
            return None

        with open('funcionarios.txt', 'w') as arq:
            for i in x:
                arq.writelines(i.nome + "|" + i.telefone + "|" + i.cpf + "|" + i.email + "|" + i.endereco)
                arq.writelines('\n')
            print('Funcionarios removido com sucesso')

    def mostrarFuncionarios(self):
        funcionario = DaoFuncionario.ler()

        if len(funcionario) == 0:
            print("Lista de funcionarios vazia")

        for i in funcionario:
            print("========Funcionario==========")
            print(f"Nome: {i.nome}\n"
                  f"Telefone: {i.telefone}\n"
                  f"Email: {i.email}\n"
                  f"Endereço: {i.endereco}\n"
                  f"CPF: {i.cpf}\n"
                  f"CLT: {i.clt}\n")


