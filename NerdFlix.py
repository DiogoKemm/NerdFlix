import datetime
from tabulate import tabulate

headers = ['Código', 'Produto', 'Tipo', 'Preço (R$)', 'Disponibilidade']
headerNotaFiscal = ['Login', 'Data', 'Valor']
cadastro = [[495, "Breaking Bad", 2, 50, True], [496, "Better Call Saul", 3, 50, False],
            [497, "Stranger Things", 3, 24, True]]
dadosCliente = []


def main():
    menuPrincipal()


def menuPrincipal():
    print('\nSeja bem vindo ao sistema interno da NerdFlix. O que o usuário deseja fazer?\n'
          + '[1] Cadastrar produtos   [2] Consultar produto\n'
          + '[3] Atualizar produtos   [4] Relatório de produtos\n'
          + '[5] Registrar compra     [6] Relatório de compras\n')

    comandoMenuPrincipal = int(input())

    if comandoMenuPrincipal == 1:
        cadastrarProdutos()
    elif comandoMenuPrincipal == 2:
        consultarProdutos()
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
        menuPrincipal()


def cadastrarProdutos():

    try:
        codigoProduto = int(input("Insira o código do produto: "))
        if any(item[0] == codigoProduto for item in cadastro):
            print("Este código já pertence a outro produto!")
    except ValueError:
        codigoProduto = int(input("Insira números: "))

    nomeProduto = input('Insira o nome do produto: ')

    tipoProduto = int(input(
        'Insira o tipo do produto (1 para série, 2 para filme, 3 para documentário): '))
    while tipoProduto not in range(1, 4):
        tipoProduto = (int(input("Insira um tipo válido: ")))

    try:
        precoProduto = float(input("Insira o preço (R$) do produto: "))
    except ValueError:
        precoProduto = float(input("Insira um número: "))

    disponivelProduto = input('O produto está disponível? (S/N): ').lower()

    if disponivelProduto == "s":
        disponivelProduto == True
    elif disponivelProduto == "n":
        disponivelProduto == False
    else:
        disponivelProduto = input("(S/N): ").lower()

    cadastro.append([codigoProduto, nomeProduto, tipoProduto,
                    precoProduto, disponivelProduto])

    escolhaUsuario = input(
        (f'{nomeProduto} cadastrado com sucesso! Deseja voltar ao menu principal? (S/N): ')).lower()

    while escolhaUsuario != "s" or "n":
        if escolhaUsuario == "s":
            menuPrincipal()
        if escolhaUsuario == "n":
            cadastrarProdutos()
        else:
            escolhaUsuario = input("(S/N): ").lower()

    return disponivelProduto, codigoProduto, nomeProduto, tipoProduto


def consultarProdutos():
    consultarCodigo = int(
        input('Digite o código do produto que quer consultar: '))
    res1 = any(consultarCodigo in sublist for sublist in cadastro)
    if res1 == True:
        for i in cadastro:
            if consultarCodigo in i:
                teste = cadastro.index(i)
                print(tabulate([cadastro[teste]], headers=headers))
                menuPrincipal()
    else:
        print('Produto não cadastrado')


def atualizarProdutos():
    while True:
        atualizarProdutoCode = int(
            input('Digite o código do produto que quer atualizar: '))
        teste2 = any(atualizarProdutoCode in sublist for sublist in cadastro)
        if teste2 == True:
            for i in cadastro:
                if atualizarProdutoCode in i:
                    teste = cadastro.index(i)

                    atualizarNomeProduto = input('Insira o nome do produto: ')

                    atualizarTipoProduto = int(input(
                        'Insira o tipo do produto (1 para série, 2 para filme, 3 para documentário): '))
                    while atualizarTipoProduto not in [1, 2, 3]:
                        atualizarTipoProduto = (
                            int(input("Insira um tipo válido: ")))

                    try:
                        atualizarPrecoProduto = float(
                            input("Insira o preço (R$) do produto: "))
                    except ValueError:
                        atualizarPrecoProduto = float(
                            input("Insira um número: "))

                    atualizarDisponibilidade = input(
                        "O produto está disponível? (S/N): ").lower()

                    if atualizarDisponibilidade == 's':
                        atualizarDisponibilidade = True

                    elif atualizarDisponibilidade == 'n':
                        atualizarDisponibilidade = False

                    else:
                        atualizarDisponibilidade = input("(S/N): ")

                    cadastro[teste][1:5] = [atualizarNomeProduto, atualizarTipoProduto,
                                            atualizarPrecoProduto, atualizarDisponibilidade]

                    menuPrincipal()

        else:
            print("Produto não cadastrado")
            menuPrincipal()


def relatorioProdutos():
    while True:
        print("\nQue produtos você deseja visualizar?"
              + "\n[0] Todos os produtos          [1] Somente filmes"
              + "\n[2] Séries                     [3] Documentários"
              + "\n[4] Disponíveis para venda     [5] Indisponíveis"
              + "\nPressione qualquer outra tecla para sair")

        try:
            comandoRelatorio = int(input())
        except ValueError:
            menuPrincipal()

        if comandoRelatorio == 0:
            if len(cadastro) == 0:
                print('Nenhum produto cadastrado')
                menuPrincipal()
            sortByName(cadastro)
            print(tabulate(cadastro, headers=headers))

        elif comandoRelatorio == 1:
            teste2 = []
            sortByName(cadastro)
            for i in cadastro:
                if 2 == i[2]:
                    teste = cadastro.index(i)
                    teste2.append(cadastro[teste])
            print(tabulate(teste2, headers=headers))

        elif comandoRelatorio == 2:
            teste2 = []
            sortByName(cadastro)
            for i in cadastro:
                if 1 == i[2]:
                    teste = cadastro.index(i)
                    teste2.append(cadastro[teste])
            print(tabulate(teste2, headers=headers))

        elif comandoRelatorio == 3:
            teste2 = []
            sortByName(cadastro)
            for i in cadastro:
                if 3 == i[2]:
                    teste = cadastro.index(i)
                    teste2.append(cadastro[teste])
            print(tabulate(teste2, headers=headers))

        elif comandoRelatorio == 4:
            teste2 = []
            sortByName(cadastro)
            for i in cadastro:
                if True == i[4]:
                    teste = cadastro.index(i)
                    teste2.append(cadastro[teste])
            print(tabulate(teste2, headers=headers))

        elif comandoRelatorio == 5:
            teste2 = []
            sortByName(cadastro)
            for i in cadastro:
                if False == i[4]:
                    teste = cadastro.index(i)
                    teste2.append(cadastro[teste])
            print(tabulate(teste2, headers=headers))

        else:
            menuPrincipal()


def registrarCompra():
    loginCliente = input('Informe o login do cliente: ')
    data = datetime.datetime.now()
    codigoCliente = int(input('Informe o código do produto: '))
    for i in cadastro:
        if codigoCliente == i[0]:
            teste = cadastro.index(i)
            if cadastro[teste][4] == True:
                print("Produto comprado com sucesso!")
                valor = cadastro[teste][3]
                dadosCliente.append([loginCliente, data, valor])
                menuPrincipal()
    else:
        voltar = input(
            "Produto não encontrado ou indisponível. Voltar ao menu principal? (S/N): ").lower()
        if voltar == "s":
            menuPrincipal()
        elif voltar == "n":
            registrarCompra()


def relatorioCompras():
    if len(dadosCliente) == 0:
        print("\nNenhum produto comprado")
        menuPrincipal()
    print(tabulate(dadosCliente, headers=headerNotaFiscal))
    menuPrincipal()

# função que retorna a lista em ordem baseado pelo nome


def sortByName(sublist):
    l = len(sublist)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sublist[j][1] > sublist[j + 1][1]):
                tempo = sublist[j]
                sublist[j] = sublist[j + 1]
                sublist[j + 1] = tempo
    return sublist


if __name__ == '__main__':
    main()
