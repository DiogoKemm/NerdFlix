cadastro = []

def main():
    menuPrincipal()

def menuPrincipal():
    print('\nSeja bem vindo ao sistema interno da NerdFlix. O que o usuário deseja fazer?\n'
    + '[1] Cadastrar produtos   [2] Consultar produto\n'
    + '[3] Atualizar produtos   [4] Relatório de produtos\n'
    + '[5] Registrar compra     [6] Relatório de compras')

    comandoMenuPrincipal = int(input())

    if comandoMenuPrincipal == 1:
        cadastrarProdutos()
    elif comandoMenuPrincipal == 2:
        organizarDados()
    elif comandoMenuPrincipal == 3:
        atualizarProdutos()
    elif comandoMenuPrincipal == 4:
        relatorioProdutos()
    elif comandoMenuPrincipal == 5:
        registrarCompra()
    elif comandoMenuPrincipal == 6:
        relatorioCompras()
    else: 
        print("Digite um número válido\n")

def cadastrarProdutos():

    listaProduto = []

    codigoProduto = int(input("Insira o código do produto: "))
    listaProduto.append(codigoProduto)

    nomeProduto = input('Insira o nome do produto: ')
    listaProduto.append(nomeProduto)

    tipoProduto = int(input('Insira o tipo do produto (1 para série, 2 para filme, 3 para documentário): '))
    listaProduto.append(tipoProduto)

    precoProduto = float(input("Insira o preço (R$) do produto: "))
    listaProduto.append(precoProduto)

    disponivelProduto = bool(input("O produto está disponível? (S/N): "))
    if disponivelProduto == 'S':
        disponivelProduto = True
    elif disponivelProduto == 'N':
        disponivelProduto = False
    listaProduto.append(disponivelProduto)

    escolhaUsuario = input((f'{listaProduto[1]} cadastrado com sucesso! Deseja voltar ao menu principal? (S/N): '))
    cadastro.extend(listaProduto)

    if escolhaUsuario == 'S':
        menuPrincipal()
    elif escolhaUsuario == 'N':
        while escolhaUsuario == 'N':
            cadastrarProdutos()

def organizarDados():
    i = 0
    if len(cadastro) == 0:
        print("Insira um produto primeiro")
        menuPrincipal()
    while len(cadastro) != 0:
        codigo_produto = [cadastro[0]]
        nome_produto = [cadastro[1]]
        tipo_produto = [cadastro[2]]
        preco_produto = [cadastro[3]]
        disponivel_produto = [cadastro[4]]

        #código para gerar multiplos vetores
        produto.extend(codigo_produto, nome_produto, tipo_produto, preco_produto, disponivel_produto)

        del cadastro[0:5]

def consultarProdutos():
    organizarDados()

  

def atualizarProdutos():
    print('Em construção')
    menuPrincipal()

def relatorioProdutos():
    print("Em construção")
    menuPrincipal()

def registrarCompra():
    print("Em construção")
    menuPrincipal()

def relatorioCompras():
    print("Em construção")
    menuPrincipal()
    


if __name__ == '__main__':
    main()
