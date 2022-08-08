import datetime
from operator import itemgetter
from tabulate import tabulate

headerCadastro = ['Código', 'Nome', 'Tipo', 'Preço (R$)', 'Disponivel?']
headerNotaFiscal = ['Login', 'Data e hora', 'Valor']
headerValorTotal = ["Valor total"]
cadastro = [[495, "Breaking Bad", "Série", 50, "Sim"], [496, "Better Call Saul", "Série", 50, "Não"],
            [497, "Stranger Things", "Série", 24, "Sim"], [1, "O Ato de Matar", "Documentário", 50, "Não"],
            [25, "Kill Bill", "Filme", 65, "Sim"], [26, "Duna", "Filme", 40, "Sim"]]
dadosCliente = []

def main():
    menuPrincipal()

def menuPrincipal():
    comandoMenuPrincipal = int(input('\nSeja bem vindo ao sistema interno da NerdFlix. O que o usuário deseja fazer?\n'
          + '[1] Cadastrar produtos   [2] Consultar produto\n'
          + '[3] Atualizar produtos   [4] Relatório de produtos\n'
          + '[5] Registrar compra     [6] Relatório de compras\n'))

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
            codigoProduto = int(input("Este código já pertence a outro produto: "))
    except ValueError:
        codigoProduto = int(input("Insira números: "))
        if any(item[0] == codigoProduto for item in cadastro):
            codigoProduto = int(input("Este código já pertence a outro produto: "))

    nomeProduto = input('Insira o nome do produto: ')

    tipoProduto = int(input(
        'Insira o tipo do produto (1 para série, 2 para filme, 3 para documentário): '))
    while tipoProduto not in range(1, 4):
        tipoProduto = (int(input("Insira um tipo válido: ")))

    if tipoProduto == 1:
        tipoProduto = "Série"
    elif tipoProduto == 2:
        tipoProduto = "Filme"
    elif tipoProduto == 3:
        tipoProduto = "Documentário"

    try:
        precoProduto = float(input("Insira o preço (R$) do produto: "))
    except ValueError:
        precoProduto = float(input("Insira um número: "))

    disponivelProduto = input('O produto está disponível? (S/N): ').lower()

    if disponivelProduto == "s":
        disponivelProduto = "Sim"
    elif disponivelProduto == "n":
        disponivelProduto = "Não"
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

def consultarProdutos():
    consultarCodigo = int(
        input('Digite o código do produto que quer consultar: '))
    checkCode = any(consultarCodigo in sublist for sublist in cadastro)
    if checkCode == True:
        for i in cadastro:
            if consultarCodigo == i[0]:
                teste = cadastro.index(i)
                print(tabulate([cadastro[teste]], headers=headerCadastro))
                menuPrincipal()
    else:
        print('Produto não cadastrado')


def atualizarProdutos():
    while True:
        atualizarProdutoCode = int(
            input('Digite o código do produto que quer atualizar: '))
        checkCode = any(atualizarProdutoCode in sublist for sublist in cadastro)
        if checkCode == True:
            for i in cadastro:
                if atualizarProdutoCode == i[0]:
                    codeIndex = cadastro.index(i)

                    atualizarNomeProduto = input('Insira o nome do produto: ')

                    atualizarTipoProduto = int(input(
                        'Insira o tipo do produto (1 para série, 2 para filme, 3 para documentário): '))
                    while atualizarTipoProduto not in [1, 2, 3]:
                        atualizarTipoProduto = (
                            int(input("Insira um tipo válido: ")))

                    if atualizarTipoProduto == 1:
                        atualizarTipoProduto = "Série"
                    elif atualizarTipoProduto == 2:
                        atualizarTipoProduto = "Filme"
                    elif atualizarTipoProduto == 3:
                        atualizarTipoProduto = "Documentário"

                    try:
                        atualizarPrecoProduto = float(
                            input("Insira o preço (R$) do produto: "))
                    except ValueError:
                        atualizarPrecoProduto = float(
                            input("Insira um número: "))

                    atualizarDisponibilidade = input(
                        "O produto está disponível? (S/N): ").lower()

                    if atualizarDisponibilidade == 's':
                        atualizarDisponibilidade = "Sim"

                    elif atualizarDisponibilidade == 'n':
                        atualizarDisponibilidade = "Não"

                    else:
                        atualizarDisponibilidade = input("(S/N): ")

                    cadastro[codeIndex][1:5] = [atualizarNomeProduto, atualizarTipoProduto,
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
            print(tabulate(sorted(cadastro, key=itemgetter(1)), headers=headerCadastro))

        elif comandoRelatorio == 1:
            movieList = []
            for i in cadastro:
                if "Filme" == i[2]:
                    movieIndex = cadastro.index(i)
                    movieList.append(cadastro[movieIndex])
            print(tabulate(sorted(movieList, key=itemgetter(1)), headers=headerCadastro))

        elif comandoRelatorio == 2:
            tvList = []
            for i in cadastro:
                if "Série" == i[2]:
                    tvIndex = cadastro.index(i)
                    tvList.append(cadastro[tvIndex])
            print(tabulate(sorted(tvList, key=itemgetter(1)), headers=headerCadastro))

        elif comandoRelatorio == 3:
            docList = []
            for i in cadastro:
                if "Documentário" == i[2]:
                    docIndex = cadastro.index(i)
                    docList.append(cadastro[docIndex])
            print(tabulate(sorted(docList, key=itemgetter(1)), headers=headerCadastro))

        elif comandoRelatorio == 4:
            availableList = []
            for i in cadastro:
                if "Sim" == i[4]:
                    availableIndex = cadastro.index(i)
                    availableList.append(cadastro[availableIndex])
            print(tabulate(sorted(availableList, key=itemgetter(1)), headers=headerCadastro))

        elif comandoRelatorio == 5:
            unavailableList = []
            for i in cadastro:
                if "Não" == i[4]:
                    unavailableIndex = cadastro.index(i)
                    unavailableList.append(cadastro[unavailableIndex])
            print(tabulate(sorted(unavailableList, key=itemgetter(1)), headers=headerCadastro))

        else:
            menuPrincipal()


def registrarCompra():
    valorTotal = []
    produtoComprado = []
    loginCliente = input('Informe o login do cliente: ')
    data = datetime.datetime.now()
    while True:
        try:
            codigoCliente = int(input('Informe um código válido (produto deve estar disponível!): '))
        except ValueError:
            codigoCliente = int(input('Insira números: '))
        for i in cadastro:
            if codigoCliente == i[0]:
                teste = cadastro.index(i)
                if cadastro[teste][4] == "Sim":
                    valor = cadastro[teste][3]
                    valorTotal.append(valor)
                    produtoComprado.append(cadastro[teste])
                    maisAlgo = input(f"{cadastro[teste][1]} comprado com sucesso! Mais algo? (S/N): ").lower()
                    while True:
                            if maisAlgo == 's':
                                try:
                                    codigoCliente = int(input("Informe um código válido (produto deve estar disponível!): "))
                                except ValueError:
                                    codigoCliente = int(input('Insira números: '))
                            elif maisAlgo == 'n':
                                print(f'\n{tabulate(produtoComprado, headers=headerCadastro)}')
                                valorTotal = sum(valorTotal)
                                print(f'Valor total: {valorTotal}')
                                dadosCliente.append([loginCliente, data.strftime("%x %X"), valorTotal])
                                menuPrincipal()
                            else: 
                                maisAlgo = input("(S/N): ")

def relatorioCompras():
    if len(dadosCliente) == 0:
        print("\nNenhum produto comprado")
        menuPrincipal()
    print(tabulate(dadosCliente, headers=headerNotaFiscal))
    menuPrincipal()

if __name__ == '__main__':
    main()
