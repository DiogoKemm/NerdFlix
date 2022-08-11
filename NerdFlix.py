#Módulos necessários
import datetime
from operator import itemgetter
from tabulate import tabulate

#Cabeçalhos para as tabelas
headerCadastro   = ['Código', 'Nome', 'Tipo', 'Preço (R$)', 'Disponivel?']
headerNotaFiscal = ['Login', 'Data e hora', 'Valor (R$)'] 

#Listas para armazenamento de informações
cadastro     = [[34, "Teste", "Filme", 50, "Sim"]] 
dadosCliente = [] 

#Função que define o menu principal
def menuPrincipal():
    while True:
        try:
            while True:
                comandoMenuPrincipal = int(input(
                    '\nSeja bem vindo ao sistema interno da NerdFlix. O que o usuário deseja fazer?\n'
                    + '[1] Cadastrar produtos   [2] Consultar produto\n'
                    + '[3] Atualizar produtos   [4] Relatório de produtos\n'
                    + '[5] Registrar compra     [6] Relatório de compras\n'))

                #Opções de seleção para outras funções
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
                    print("\nDigite um número válido!")
        except ValueError:
            print("\nInsira um número!")

#Função de cadastro de produtos
def cadastrarProdutos():
    while True:
        try:
            codigoProduto = int(input("Insira o código do produto: "))
            while any(item[0] == codigoProduto for item in cadastro):
                codigoProduto = int(input("Este código já pertence a outro produto: "))  
        except ValueError:
            print("Insira números!")
        else:
            break

    nomeProduto = input('Insira o nome do produto: ')

    while True:
        try:
            tipoProduto = int(input(
                'Insira o tipo do produto (1 para série, 2 para filme, 3 para documentário): '))
            while tipoProduto not in range(1, 4):
                tipoProduto = (int(input("Insira um tipo válido: ")))
        except ValueError:
            print("Insira um número!")
        else:
            break

    if tipoProduto == 1:
        tipoProduto = "Série"
    elif tipoProduto == 2:
        tipoProduto = "Filme"
    elif tipoProduto == 3:
        tipoProduto = "Documentário"

    while True:
        try:
            precoProduto = float(input("Insira o preço (R$) do produto: "))
        except ValueError:
            print("Insira um número!")
        else: 
            break

    while True:
        disponivelProduto = input('O produto está disponível? (S/N): ').lower()
        if disponivelProduto == "s":
            disponibilidade = "Sim"
            break

        elif disponivelProduto == "n":
            disponibilidade = "Não"
            break

    cadastro.append([codigoProduto, nomeProduto, tipoProduto,
                    precoProduto, disponibilidade])

    while True:
        escolhaUsuario = input(
        (f'{nomeProduto} cadastrado com sucesso! Deseja voltar ao menu principal? (S/N): ')).lower()
        if escolhaUsuario == "s":
            menuPrincipal()
        elif escolhaUsuario == "n":
            cadastrarProdutos()

#Consultoria dos produto baseado em seu código
def consultarProdutos():
    while True:
        try:
            consultarCodigo = int(
                input('Digite o código do produto que quer consultar: '))
            checkCode = any(consultarCodigo in sublist for sublist in cadastro)
            if checkCode == True:
                for i in cadastro:
                    if consultarCodigo == i[0]:
                        teste = cadastro.index(i)
                        print("\n" + tabulate([cadastro[teste]], headers=headerCadastro))
                        menuPrincipal()
            else:
                while True:
                    voltar = input('Produto não cadastrado. Deseja voltar ao menu principal? (S/N): ').lower()
                    if voltar == 's':
                        menuPrincipal()
                    elif voltar == 'n':
                        consultarProdutos()
        except ValueError:
            print("Digite um número!")
        else:
            break
                    
#Atualiza o produto baseado em seu código
def atualizarProdutos():
    while True:
        try:
            atualizarProdutoCode = int(
                input('Digite o código do produto que quer atualizar: '))
            checkCode = any(atualizarProdutoCode in sublist for sublist in cadastro)
            if checkCode == True:
                for i in cadastro:
                    if atualizarProdutoCode == i[0]:
                        codeIndex = cadastro.index(i)

                        atualizarNomeProduto = input('Insira o nome do produto: ')

                        while True:
                            try:
                                atualizarTipoProduto = int(input(
                                    'Insira o tipo do produto (1 para série, 2 para filme, 3 para documentário): '))
                                while atualizarTipoProduto not in [1, 2, 3]:
                                    atualizarTipoProduto = (
                                        int(input("Insira um tipo válido: ")))
                            except ValueError:
                                print("Insira um número!")
                            else:
                                break

                        if atualizarTipoProduto == 1:
                            atualizarTipoProduto = "Série"
                        elif atualizarTipoProduto == 2:
                            atualizarTipoProduto = "Filme"
                        elif atualizarTipoProduto == 3:
                            atualizarTipoProduto = "Documentário"

                        while True:
                            try:
                                atualizarPrecoProduto = float(
                                    input("Insira o preço (R$) do produto: "))
                            except ValueError:
                                print("Insira um número!")
                            else:
                                break
                        
                        while True:
                            atualizarDisponibilidade = input(
                                "O produto está disponível? (S/N): ").lower()

                            if atualizarDisponibilidade == 's':
                                disponibilidade = "Sim"
                                break

                            elif atualizarDisponibilidade == 'n':
                                disponibilidade = "Não"
                                break
                        
                        print('Produto cadastrado com sucesso!')

                        cadastro[codeIndex][1:5] = [atualizarNomeProduto, atualizarTipoProduto,
                                                atualizarPrecoProduto, disponibilidade]

                        menuPrincipal()
            else:
                print("\nProduto não cadastrado")
                menuPrincipal()

        except ValueError:
            print("Insira um número!")
        else: 
            break

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
            print('\n'+ tabulate(sorted(cadastro, key=itemgetter(1)), headers=headerCadastro))

        elif comandoRelatorio == 1:
            movieList = []
            for i in cadastro:
                if "Filme" == i[2]:
                    movieIndex = cadastro.index(i)
                    movieList.append(cadastro[movieIndex])
            print('\n'+ tabulate(sorted(movieList, key=itemgetter(1)), headers=headerCadastro))

        elif comandoRelatorio == 2:
            tvList = []
            for i in cadastro:
                if "Série" == i[2]:
                    tvIndex = cadastro.index(i)
                    tvList.append(cadastro[tvIndex])
            print('\n'+ tabulate(sorted(tvList, key=itemgetter(1)), headers=headerCadastro))

        elif comandoRelatorio == 3:
            docList = []
            for i in cadastro:
                if "Documentário" == i[2]:
                    docIndex = cadastro.index(i)
                    docList.append(cadastro[docIndex])
            print('\n'+ tabulate(sorted(docList, key=itemgetter(1)), headers=headerCadastro))

        elif comandoRelatorio == 4:
            availableList = []
            for i in cadastro:
                if "Sim" == i[4]:
                    availableIndex = cadastro.index(i)
                    availableList.append(cadastro[availableIndex])
            print('\n'+ tabulate(sorted(availableList, key=itemgetter(1)), headers=headerCadastro))

        elif comandoRelatorio == 5:
            unavailableList = []
            for i in cadastro:
                if "Não" == i[4]:
                    unavailableIndex = cadastro.index(i)
                    unavailableList.append(cadastro[unavailableIndex])
            print('\n'+ tabulate(sorted(unavailableList, key=itemgetter(1)), headers=headerCadastro))

        else:
            menuPrincipal()

#Função que pede o login do cliente, define a data e hora da compra, e compra o produto 
def registrarCompra():
    valorTotal      = []
    produtoComprado = []
    loginCliente    = input('Informe o login do cliente: ')
    data            = f"{datetime.datetime.now():%d/%m/%Y %X}"
    while True:
        try:
            codigoCliente = int(input('Informe um código válido (produto deve estar disponível!): '))
            if any(item[0] != codigoCliente for item in cadastro):
                print("\nProduto não encontrado!")
                menuPrincipal()
            for i in cadastro:
                if codigoCliente == i[0]:
                    codeIndex = cadastro.index(i)
                    if cadastro[codeIndex][4] == "Sim":
                        valor = cadastro[codeIndex][3]
                        valorTotal.append(valor)
                        produtoComprado.append(cadastro[codeIndex])
                        while True:
                            maisAlgo = input(f"{cadastro[codeIndex][1]} comprado com sucesso! Mais algo? (S/N): ").lower()
                            if maisAlgo == 's':
                                break
                            elif maisAlgo == 'n':
                                print('\n' + tabulate(produtoComprado, headers=headerCadastro))
                                valorTotal = sum(valorTotal)
                                print(f'\nValor total: R$ {valorTotal}')
                                dadosCliente.append([loginCliente, data, valorTotal])
                                menuPrincipal()
        except ValueError:
            print("Insira um número!")
        else:
            pass
                
#Relatório de todos os produtos comprados e seus respectivos clientes
def relatorioCompras():
    if len(dadosCliente) == 0:
        print("\nNenhum produto comprado")
        menuPrincipal()
    print('\n'+ tabulate(dadosCliente, headers=headerNotaFiscal))
    menuPrincipal()

menuPrincipal()