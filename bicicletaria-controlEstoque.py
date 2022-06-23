listaPecas = []
linha = '-' * 20

def cadastrarPeca(codigoProduto):
   print('Você Selecionou a Opção de Cadastro de Peças')
   print('Código da peça: {}'.format(codigoProduto))
   nome = input('Entre com o NOME da peça: ')
   fabric = input('Entre com o FABRICANTE da peça: ')
   preco = float(input('Entre com o VALOR(R$) da peça: '))
   dicionarioPeca = {'codigo': codigoProduto,
                 'nome': nome,
                 'fabricante': fabric,
                 'valor R$': preco}
   listaPecas.append(dicionarioPeca.copy())

def consultarPeca():
   while True:
       try:
           print('Você selecionou a opção de Consulta de Peças')
           opcaoConsulta = int(input('Escolha a opção desejada: \n'
                                     '1- Consultar Todas as Peças \n'
                                     '2- Consultar Peças por Código \n'
                                     '3- Consultar Peças por Fabricante \n'
                                     '4- Retornar \n'
                                     '>> '))
           print(linha)
           if opcaoConsulta == 1:
               for peca in listaPecas:
                   for key, value in peca.items():
                       print('{} : {} '.format(key, value))
           elif opcaoConsulta == 2:
               entrada = int(input('Digite o código desejado: '))
               for peca in listaPecas:
                   if (peca['codigo'] == entrada):
                       for key, value in peca.items():
                           print('{} : {} '.format(key, value))
           elif opcaoConsulta == 3:
               print('Pecas por fabricante')
               entrada = (input('Digite o fabricante desejado: '))
               for peca in listaPecas:
                   if (peca['fabricante'] == entrada):
                       for key, value in peca.items():
                           print('{} : {} '.format(key, value))
           elif opcaoConsulta == 4:
               print('Programa encerrado')
               break
           else:
               print('O número digitado e inválido!')
               continue
       except ValueError:
           print('Digite apenas valores numéricos!')
           continue
print(linha)

def removerPeca():
   print('Você Selecionou a Opção de Remover Peças')
   entrada = int(input('Digite o código desejado para remover: '))
   for peca in listaPecas:
       if (peca['codigo'] == entrada):
           listaPecas.remove(peca)

print('Bem Vindo ao Controle de Estoque da Bicicletaria do Ghabriel Machado Rodrigues')
codigoProduto = 0
while True:
   try:
       opcao = int(input('Escolha a opção desejada: \n'
                         '1- Cadastrar \n'
                         '2- Consultar Peças  \n'
                         '3- Remover Peças \n'
                         '4- Sair \n'
                         '>> '))
       if opcao == 1:
           codigoProduto = codigoProduto + 1
           cadastrarPeca(codigoProduto)
       elif opcao == 2:
           consultarPeca()
       elif opcao == 3:
           removerPeca()
       elif opcao == 4:
           print('Programa encerrado')
           break
       else:
           print('O número digitado e inválido!')
           continue
   except ValueError:
       print('Digite apenas valores numéricos!')
       continue




