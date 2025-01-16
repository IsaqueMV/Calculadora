operadores = ('-', '+', '/', '//', '%', '**')
linha = '~'*60


print('=' * 60)
print('CALCULADORA'.center(60))
print('=' * 60)


ligado = True
while ligado:
    operacao = ''
    
    print('Qual operação deseja fazer?'.center(60))
    print(linha)
    print('Soma: +, Subtração: -, Divisão: /, Divisão Inteira: //')
    print('Resto da Divisão: % e potênciação: **')
    print(linha)

    ligado_2 = True
    while ligado_2:
        operacao = input('Digite o operador: ')
        print(linha)
        
        if operacao in operadores:
            ligado_2 = False
            break
            
        else:
            print('Operador inválido!'.center(60))
            print('Digite o operador disponível!'.center(60))
            print(linha)


    print('Agora digite os números que serão usados na operação!'.center(60))
    print(linha)
    
    while True:
        entrada_1 = input('Digite um número: ')
        entrada_2 = input('Digite outro número: ')
        print(linha)

        if entrada_1.isnumeric() and entrada_2.isnumeric():
            break
            
        else:
            print('Digite apenas números!'.center(60))
            print(linha)
            continue

    num_entrada1 = int(entrada_1)
    num_entrada2 = int(entrada_2)

    if operacao == '+':
        resultado = num_entrada1 + num_entrada2
        print(f'A soma entre {entrada_1} e {entrada_2} = {resultado}'.center(60))
        print(linha)

    if operacao == '-':
        resultado = num_entrada1 - num_entrada2
        print(f'A subtração de {entrada_1} por {entrada_2} = {resultado}'.center(60))
        print(linha)

    if operacao == '/':
        resultado = num_entrada1 / num_entrada2
        print(f'A divisão de {entrada_1} por {entrada_2} = {resultado}'.center(60))
        print(linha)

    if operacao == '//':
        resultado = num_entrada1 // num_entrada2
        print(f'A Divisão inteira de {entrada_1} por {entrada_2} = {resultado}'.center(60))
        print(linha)

    if operacao == '%':
        resultado = num_entrada1 % num_entrada2
        print(f'O Resto da divisão de {entrada_1} por {entrada_2} = {resultado}'.center(60))
        print(linha)

    if operacao == '**':
        resultado = num_entrada1 ** num_entrada2
        print(f'O número {entrada_1} elevado a {entrada_2} = {resultado}'.center(60))
        print(linha)


    opcoes2 = ['1', '2']
    sair = ''
    while sair not in opcoes2:
        sair = input('Digite [1] para fazer outras operaçoes, ou [2] para Sair: ')
        
        if sair == '1':
            print('Reiniciando...')
            continue
            
        elif sair == '2':
            print('Programa Finalizado!'.center(60))
            ligado = False
            break
            
        else:
            print(linha)
            print('Digite apenas [1] ou [2]!'.center(60))
            print(linha)
            
    print(linha)
