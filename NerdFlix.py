import datetime
from tabulate import tabulate

cadastro = [[495, "Breaking Bad", 2, 50, True]]
headers = ['Código', 'Produto', 'Tipo', 'Preço (R$)', 'Disponibilidade']
headerNotaFiscal = ['Login', 'Data', 'Valor total (R$)']
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

    while True:
        codigoProduto = int(input("Insira o código do produto: "))
        if any(item[0]==codigoProduto for item in cadastro):
            print("Este código já pertence a outro produto!")
            break

        nomeProduto = input('Insira o nome do produto: ')

        tipoProduto = int(input('Insira o tipo do produto (1 para série, 2 para filme, 3 para documentário): '))
        while tipoProduto not in [1, 2, 3]:
            tipoProduto = (int(input("Insira um tipo válido: ")))

        try:
            precoProduto = float(input("Insira o preço (R$) do produto: "))
        except ValueError:
            precoProduto = float(input("Insira um número: "))


        disponivelProduto = (input("O produto está disponível? (S/N): "))
        if disponivelProduto == "s" or "S":
            disponivelProduto = True
        if disponivelProduto == "n" or "N":
            disponivelProduto = False
        
        cadastro.append([codigoProduto, nomeProduto, tipoProduto, precoProduto, disponivelProduto])

        escolhaUsuario = input((f'{nomeProduto} cadastrado com sucesso! Deseja voltar ao menu principal? (S/N): '))

        while escolhaUsuario != "s" or "S" and "n" or "N":
            if escolhaUsuario == 's' and "S":
                menuPrincipal()
            if escolhaUsuario == "n" and "N":
                cadastrarProdutos()
            else:
                escolhaUsuario = input("(S/N): ")

        return disponivelProduto
    
def consultarProdutos():
    consultarCodigo = int(input('Digite o código do produto que quer consultar: '))
    res1 = any(consultarCodigo in sublist for sublist in cadastro)
    if res1 == True:
        for i in cadastro:
            if consultarCodigo in i:
                teste = cadastro.index(i)
                print(tabulate([cadastro[teste]], headers=headers))
                menuPrincipal()
    else: 
        print('Produto não cadastrado')
        menuPrincipal()


def atualizarProdutos():
    atualizarProdutoCode = int(input('Digite o código do produto que quer atualizar: '))
    teste2 = any(atualizarProdutoCode in sublist for sublist in cadastro)
    if teste2 == True:
        for i in cadastro:
            if atualizarProdutoCode in i:
                teste = cadastro.index(i)

                atualizarNomeProduto = input('Insira o nome do produto: ')

                atualizarTipoProduto = int(input('Insira o tipo do produto (1 para série, 2 para filme, 3 para documentário): '))

                atualizarPrecoProduto = float(input("Insira o preço (R$) do produto: "))

                atualizarDisponibilidade = bool(input("O produto está disponível? (S/N): "))
                if atualizarDisponibilidade == 'S':
                    disponivelProduto = True
                elif atualizarDisponibilidade == 'N':
                    disponivelProduto = False

                #código-espaguete
                cadastro[teste][1] = atualizarNomeProduto
                cadastro[teste][2] = atualizarTipoProduto
                cadastro[teste][3] = atualizarPrecoProduto
                cadastro[teste][4] = atualizarDisponibilidade
                
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
        
        comandoRelatorio = int(input())

        if comandoRelatorio == 0:
            if len(cadastro) == 0:
                print('Nenhum produto cadastrado')
                menuPrincipal()
            sortfun(cadastro)
            print(tabulate(cadastro, headers=headers))

        elif comandoRelatorio == 1:
            sortfun(cadastro)
            if any(sub[2]== 2 for sub in cadastro):
                for i in cadastro:
                    if 2 in i:
                        teste69 = cadastro.index(i)
                        print(tabulate(cadastro, headers=headers))

        elif comandoRelatorio == 2:
            sortfun(cadastro)
            if any(sub[2]== 1 for sub in cadastro):
                for i in cadastro:
                    if 1 in i:
                        teste69 = cadastro.index(i)
                        print(tabulate(cadastro, headers=headers))
            
        elif comandoRelatorio == 3:
            sortfun(cadastro)
            if any(sub[2]== 3 for sub in cadastro):
                for i in cadastro:
                    if 3 in i:
                        teste69 = cadastro.index(i)
                        print(cadastro[teste69])

        elif comandoRelatorio == 4:
            sortfun(cadastro)
            if any(sub[4] == True for sub in cadastro):
                for i in cadastro:
                    if True in i:
                        teste69 = cadastro.index(i)
                        print(cadastro[teste69])
        
        elif comandoRelatorio == 5:
            sortfun(cadastro)
            if any(sub[4] == False for sub in cadastro):
                for i in cadastro:
                    if False in i:
                        teste69 = cadastro.index(i)
                        print(cadastro[teste69])

        else:
            menuPrincipal()

    

def registrarCompra():
            loginCliente = input('Informe o login do cliente: ')
            data = datetime.datetime.now()
            codigoCliente = int(input('Informe o código do produto: '))
            if any(sub[0] == codigoCliente for sub in cadastro) and any(sub[4] == True for sub in cadastro):
                print('Produto adicionado ao carrinho') 
                valor = [sub[3] for sub in cadastro]
                maisAlgo = input("Mais alguma compra? (S/N): ").lower()
                if maisAlgo == "s":
                    registrarCompra()
                elif maisAlgo == "n":
                    print((f'Nota fiscal\nCódigo: {[item[0] for item in cadastro]}\n'
                    + f'Nome: {[item[1] for item in cadastro]}\n'
                    + f'Tipo: {[item[2] for item in cadastro]}\n'
                    + f'Preço (R$): {[item[3] for item in cadastro]}\n'))
                    dadosCliente.append([loginCliente, data, valor])
                    menuPrincipal()    
            else:
                voltar = input("Produto não encontrado ou indisponível. Voltar ao menu principal? (S/N): ").lower()
                if voltar == "s":
                    menuPrincipal()
                elif voltar == "n":
                    registrarCompra()
    
def relatorioCompras():
    if len(dadosCliente) == 0:
        print("\nNenhum produto comprado")
        menuPrincipal()
    print(tabulate(dadosCliente))
    menuPrincipal()

#função que retorna a lista em ordem baseado pelo nome (index(2))
def sortfun(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

def irOuFicar():
    comandoIrOuFicar = input('Deseja consultar mais algum produto? (S/N): ')
    if comandoIrOuFicar == "n" and "N":
        menuPrincipal()
    if comandoIrOuFicar == "S" and "s":
        relatorioProdutos()
    
if __name__ == '__main__':
    main()