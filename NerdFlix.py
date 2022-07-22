cadastro = []

def main():
    menuPrincipal()

def menuPrincipal():
    print('Seja bem vindo ao sistema interno da NerdFlix. O que o usuário deseja fazer?\n'
    + '[1] Cadastrar produtos   [2] Consultar produto\n'
    + '[3] Atualizar produtos   [4] Relatório de produtos\n'
    + '[5] Registrar compra     [6] Relatório de compras')

    comandoMenuPrincipal = int(input())

    if comandoMenuPrincipal == 1:
        cadastrarProdutos()
    elif comandoMenuPrincipal == 2:
        consultarProdutos()

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

def consultarProdutos():
    print(cadastro)

if __name__ == '__main__':
    main()
