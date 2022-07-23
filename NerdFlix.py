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
        menuPrincipal()

def cadastrarProdutos():

    codigoProduto = int(input("Insira o código do produto: "))

    nomeProduto = input('Insira o nome do produto: ')

    tipoProduto = int(input('Insira o tipo do produto (1 para série, 2 para filme, 3 para documentário): '))

    precoProduto = float(input("Insira o preço (R$) do produto: "))

    disponivelProduto = (input("O produto está disponível? (S/N): "))
    if disponivelProduto == 'S':
        disponivelProduto = True
    elif disponivelProduto == 'N':
        disponivelProduto = False
    
    cadastro.append([codigoProduto, nomeProduto, tipoProduto, precoProduto, disponivelProduto])

    escolhaUsuario = input((f'{nomeProduto} cadastrado com sucesso! Deseja voltar ao menu principal? (S/N): '))

    while escolhaUsuario != 'S' or 'N':
        if escolhaUsuario == 'S':
            menuPrincipal()
        elif escolhaUsuario == 'N':
            cadastrarProdutos()
    
def consultarProdutos():
    consultarCodigo = int(input('Digite o código do produto que quer consultar: '))
    res1 = any(consultarCodigo in sublist for sublist in cadastro)
    if res1 == True:
        for i in cadastro:
            if consultarCodigo in i:
                teste = cadastro.index(i)
                print(cadastro[teste])
    else: 
        print('Produto não cadastrado')



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

def relatorioProdutos():
    print("\nQue produtos você deseja visualizar?"
    + "\n[0] Todos os produtos          [1] Somente filmes"
    + "\n[2] Séries                     [3] Documentários"
    + "\n[4] Disponíveis para venda     [5] Indisponíveis")
    
    comandoRelatorio = int(input())

    if comandoRelatorio == 0:
        sortfun(cadastro)
        teste5 = (f'Código: {[item[0] for item in cadastro]}\n'
        + f'Nome: {[item[1] for item in cadastro]}\n'
        + f'Tipo: {[item[2] for item in cadastro]}\n'
        + f'Preço (R$): {[item[3] for item in cadastro]}\n')
        print(teste5)

    elif comandoRelatorio == 1:
        sortfun(cadastro)
        if any(sub[2]== 2 for sub in cadastro):
            for i in cadastro:
                if 2 in i:
                    teste69 = cadastro.index(i)
                    print(cadastro[teste69])

    elif comandoRelatorio == 2:
        sortfun(cadastro)
        if any(sub[2]== 1 for sub in cadastro):
            for i in cadastro:
                if 1 in i:
                    teste69 = cadastro.index(i)
                    print(cadastro[teste69])
    
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
        print('perish')


#função que retorna a lista em ordem baseado pelo nome
def sortfun(sub_li):
    l = len(sub_li)
    for i in range(0, l):
        for j in range(0, l-i-1):
            if (sub_li[j][1] > sub_li[j + 1][1]):
                tempo = sub_li[j]
                sub_li[j]= sub_li[j + 1]
                sub_li[j + 1]= tempo
    return sub_li

#função que extrai valor de uma sublista (ainda não usado)
def Extract(lst):
    return [item[0] for item in lst]

def registrarCompra():
    print("Em construção")
    menuPrincipal()

def relatorioCompras():
    print("Em construção")
    menuPrincipal()
    
if __name__ == '__main__':
    main()