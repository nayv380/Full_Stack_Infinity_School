import db

produtos = db.importar_csv()

def listar_produtos():
    if len(produtos) == 0:
        print('Não há produtos cadastrados')
        return False

    print(' Produtos '.center(30, '='))
    for index, produto in enumerate(produtos, start=1):
        print(f'[{index}] - {produto["nome"]}')
        preco_formatado = f'R$ {produto["preco"]:.2f}'.replace('.', ',')
        print(f'Preço: {preco_formatado}')
        print(f'Quantidade: {produto["quantidade"]}')
        
        if index != len(produtos):
            print('-' * 30)
    
    return True

def cadastrar_produto():
    while True:
        nome = input('Digite o nome do produto: ')
        preco_str = input('Digite o preço do produto (use vírgula): ')
        try:
            preco = float(preco_str.replace('.', '').replace(',', '.'))
        except ValueError:
            print('Preço inválido. Por favor, insira um valor numérico válido (exemplo: 1.234,56).')
            return
        quantidade = int(input('Digite a quantidade: '))

        produto = {
            'nome': nome,
            'preco': preco,
            'quantidade': quantidade
        }
        produtos.append(produto)

        print('Produto cadastrado com sucesso.')

        resp = input('Deseja cadastrar outro produto? [Sim/Não] -> ')
        if resp.upper() == 'NÃO':
            break

def editar_produto():
    while True:
        tem_produtos = listar_produtos()

        if not tem_produtos:
            return
        
        print('=' * 30)
        produto_index = int(input('Selecione o produto a ser editado: '))
        
        produto = produtos[produto_index - 1]

        produto['nome'] = input('Digite o novo nome do produto: ')
        preco_str = input('Digite o novo preço do produto (use vírgula): ')
        try:
            produto['preco'] = float(preco_str.replace('.', '').replace(',', '.'))
        except ValueError:
            print('Preço inválido. Por favor, insira um valor numérico válido (exemplo: 1.234,56).')
            return
        produto['quantidade'] = int(input('Digite a nova quantidade do produto: '))

        print('Produto editado com sucesso.')

        resp = input('Deseja editar outro produto? [Sim/Não] -> ')
        if resp.upper() == 'NÃO':
            break

def excluir_produto():
    while True:
        tem_produtos = listar_produtos()

        if not tem_produtos:
            return
        
        print('=' * 30)
        produto_index = int(input('Selecione o produto a ser excluido: '))

        if produto_index < 1 or produto_index > len(produtos):
            print('Não há produto com esse indice.')
            return

        produtos.pop(produto_index - 1)
        
        print('Produto excluido com sucesso!')
        
        resp = input('Deseja excluir outro produto? [Sim/Não] -> ')
        if resp.upper() == 'NÃO':
            break
