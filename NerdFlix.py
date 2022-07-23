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

def cadastrarProdutos():

    codigoProduto = int(input("Insira o código do produto: "))

    nomeProduto = input('Insira o nome do produto: ')

    tipoProduto = int(input('Insira o tipo do produto (1 para série, 2 para filme, 3 para documentário): '))

    precoProduto = float(input("Insira o preço (R$) do produto: "))

    disponivelProduto = bool(input("O produto está disponível? (S/N): "))
    if disponivelProduto == 'S':
        disponivelProduto = True
    elif disponivelProduto == 'N':
        disponivelProduto = False

    escolhaUsuario = input((f'{nomeProduto} cadastrado com sucesso! Deseja voltar ao menu principal? (S/N): '))
    cadastro.append([codigoProduto, nomeProduto, tipoProduto, precoProduto])

    if escolhaUsuario == 'S':
        menuPrincipal()
    elif escolhaUsuario == 'N':
        while escolhaUsuario == 'N':
            cadastrarProdutos()

def consultarProdutos():
    consultarCodigo = int(input('Digite o código do produto que quer consultar: '))
    res1 = any(consultarCodigo in sublist for sublist in cadastro)
    if res1 == True:
        for i in cadastro:
            if consultarCodigo in i:
                teste = cadastro.index(i)
                print(cadastro[teste])


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