import os

jogo = [
        [' ','|', ' ', '|', ' '],
        [' ', '|', ' ', '|', ' '],
        [' ', '|', ' ', '|', ' '],
]
tipos_de_jogos_1 = ['X','|', 'X', '|', 'X']
tipos_de_jogos_2 = ['O','|', 'O', '|', 'O']
tipos_1 = [
        ['X','|', ' ', '|', ' '],
        ['X', '|', ' ', '|', ' '],
        ['X', '|', ' ', '|', ' '],
]

def verificado_de_vitorias(res='X'):
    tipos_2 = ((res, '|', ' ', '|', ' ', res, '|', ' ', '|', ' ', res, '|', ' ', '|', ' '),
               (' ', '|', res, '|', ' ', ' ', '|', res, '|', ' ', ' ', '|', res, '|', ' '),
               (' ', '|', ' ', '|', res, ' ', '|', ' ', '|', res, ' ', '|', ' ', '|', res),
               (res, '|', ' ', '|', ' ', ' ', '|', res, '|', ' ', ' ', '|', ' ', '|', res),
               (' ', '|', ' ', '|', res, ' ', '|', res, '|', ' ', res, '|', ' ', '|', ' '),
               (res, '|', ' ', '|', ' ', res, '|', ' ', '|', ' ', res, '|', ' ', '|', res),
               (res, '|', ' ', '|', ' ', ' ', '|', ' ', '|', ' ', res, '|', res, '|', res),
               (' ', '|', ' ', '|', res, ' ', '|', res, '|', ' ', res, '|', ' ', '|', res),
               (res, '|', res, '|', ' ', res, '|', ' ', '|', ' ', res, '|', ' ', '|', ' '), #Horizontal primeira fileira
               (res, '|', ' ', '|', res, res, '|', ' ', '|', ' ', res, '|', ' ', '|', ' '),
               (res, '|', ' ', '|', ' ', res, '|', res, '|', ' ', res, '|', ' ', '|', ' '),
               (res, '|', ' ', '|', ' ', res, '|', ' ', '|', res, res, '|', ' ', '|', ' '),
               (res, '|', ' ', '|', ' ', res, '|', ' ', '|', ' ', res, '|', res, '|', ' '),
               (res, '|', ' ', '|', ' ', res, '|', ' ', '|', ' ', res, '|', ' ', '|', res),
               (res, '|', res, '|', ' ', ' ', '|', res, '|', ' ', ' ', '|', res, '|', ' '), # Horizontal segunda fileira
               (' ', '|', res, '|', res, ' ', '|', res, '|', ' ', ' ', '|', res, '|', ' '),
               (' ', '|', res, '|', ' ', res, '|', res, '|', ' ', ' ', '|', res, '|', ' '),
               (' ', '|', res, '|', ' ', ' ', '|', res, '|', res, ' ', '|', res, '|', ' '),
               (' ', '|', res, '|', ' ', ' ', '|', res, '|', ' ', res, '|', res, '|', ' '),
               (' ', '|', res, '|', ' ', ' ', '|', res, '|', ' ', ' ', '|', res, '|', res),
               (res, '|', ' ', '|', res, ' ', '|', ' ', '|', res, ' ', '|', ' ', '|', res), # Horizontal terceira fileira
               (' ', '|', res, '|', res, ' ', '|', ' ', '|', res, ' ', '|', ' ', '|', res),
               (' ', '|', ' ', '|', res, res, '|', ' ', '|', res, ' ', '|', ' ', '|', res),
               (' ', '|', ' ', '|', res, ' ', '|', res, '|', res, ' ', '|', ' ', '|', res),
               (' ', '|', ' ', '|', res, ' ', '|', ' ', '|', res, res, '|', ' ', '|', res),
               (' ', '|', ' ', '|', res, ' ', '|', ' ', '|', res, ' ', '|', res, '|', res),
               (res, '|', res, '|', ' ', ' ', '|', res, '|', ' ', ' ', '|', ' ', '|', res), # Diagonal esquerda
               (res, '|', ' ', '|', res, ' ', '|', res, '|', ' ', ' ', '|', ' ', '|', res),
               (res, '|', ' ', '|', ' ', res, '|', res, '|', ' ', ' ', '|', ' ', '|', res),
               (res, '|', ' ', '|', ' ', ' ', '|', res, '|', res, ' ', '|', ' ', '|', res),
               (res, '|', ' ', '|', ' ', ' ', '|', res, '|', ' ', res, '|', ' ', '|', res),
               (res, '|', ' ', '|', ' ', ' ', '|', res, '|', ' ', ' ', '|', res, '|', res),
               (res, '|', ' ', '|', res, ' ', '|', res, '|', ' ', res, '|', ' ', '|', ' '), # Diagonal direita
               (' ', '|', res, '|', res, ' ', '|', res, '|', ' ', res, '|', ' ', '|', ' '),
               (' ', '|', ' ', '|', res, res, '|', res, '|', ' ', res, '|', ' ', '|', ' '),
               (' ', '|', ' ', '|', res, ' ', '|', res, '|', res, res, '|', ' ', '|', ' '),
               (' ', '|', ' ', '|', res, ' ', '|', res, '|', ' ', res, '|', res, '|', ' '),
               (' ', '|', ' ', '|', res, ' ', '|', res, '|', ' ', res, '|', ' ', '|', res),
               )
    return tipos_2

def verificar_escolha(jogador):
    def aplicar(resposta):
        if resposta == '1':
            jogo[0].pop(0)
            jogo[0].insert(0,jogador )
        elif resposta == '2':
            jogo[0].pop(2)
            jogo[0].insert(2,jogador )
        elif resposta == '3':
            jogo[0].pop(4)
            jogo[0].insert(4,jogador )
        elif resposta == '4':
            jogo[1].pop(0)
            jogo[1].insert(0,jogador )
        elif resposta == '5':
            jogo[1].pop(2)
            jogo[1].insert(2,jogador )
        elif resposta == '6':
            jogo[1].pop(4)
            jogo[1].insert(4,jogador )
        elif resposta == '7':
            jogo[2].pop(0)
            jogo[2].insert(0,jogador )
        elif resposta == '8':
            jogo[2].pop(2)
            jogo[2].insert(2,jogador )
        elif resposta == '9':
            jogo[2].pop(4)
            jogo[2].insert(4,jogador )
    return aplicar

vitorias_do_jogador_1 = 0
vitorias_do_jogador_2 = 0
empates = 0
resposta_ja_utilizada = set()

jogador_resposta_1 = (verificar_escolha('X'))
jogador_resposta_2 = (verificar_escolha('O'))

print('Bem vindo ao jogo da velha')

while True:
    try:
        opcoes_de_inicio = input('Digite (I) para iniciar ou (S) para sair: ').upper()
    except ValueError:
        print('Opção escolhida não é valida')
        os.system('cls')

    if opcoes_de_inicio not in ('I', 'S'):
        print('Opção escolhida não é valida')
        os.system('cls')
        continue

    if opcoes_de_inicio == 'S':
        print('Saindo do jogo, Obrigado por utilizar o jogo da velha')
        break

    if opcoes_de_inicio == 'I':
        os.system('cls')
        while True:
            def perguntar_1():
                print('Opções de espaços: 1,2,3,4,5,6,7,8,9 ')
                jogador_1 = input('Jogador 1 digite onde quer colocar o (x): ').upper()

                if jogador_1 not in ('1','2','3','4','5','6','7','8','9','E','S'):
                    print('resposta invalida')
                    return perguntar_1()  # chama a função de novo (volta pra mesma linha)
                elif jogador_1 in resposta_ja_utilizada:
                    print('Espaço já ocupado')
                    return perguntar_1()

                return jogador_1

            resposta = perguntar_1()
            jogador_resposta_1(resposta)
            resposta_ja_utilizada.add(resposta)

            for tabela in jogo:
                print("".join(str(n) for n in tabela))

            juntar = sum(jogo, [])
            jogo_tupla = tuple(juntar)
            valor_antigo = 'O'    # valor a ser retirado
            novo_valor = ' '
            lista = list(jogo_tupla)

            for i in range(len(lista)):
                if lista[i] == valor_antigo:
                    lista[i] = novo_valor

            lista = tuple(lista)
            vitorias_x = verificado_de_vitorias('X')
            for vitoria in vitorias_x:
                if vitoria == lista:
                    print('Jogador 1 venceu!')
                    print('Iniciando proximo jogo')
                    jogo = [
                        [' ', '|', ' ', '|', ' '],
                        [' ', '|', ' ', '|', ' '],
                        [' ', '|', ' ', '|', ' '],
                    ]
                    vitorias_do_jogador_1 += 1
                    print(f'Vitorias do jogador 1: {vitorias_do_jogador_1}')
                    print(f'Vitorias do jogador 2: {vitorias_do_jogador_2}')
                    print(f'Empates: {empates}')
                    resposta_ja_utilizada.clear()
                    continue

            for jogos in jogo:
                if jogos == tipos_de_jogos_1:
                    print('Jogador 1 venceu!')
                    print('Iniciando proximo jogo')
                    jogo = [
                        [' ', '|', ' ', '|', ' '],
                        [' ', '|', ' ', '|', ' '],
                        [' ', '|', ' ', '|', ' '],
                    ]
                    vitorias_do_jogador_1 += 1
                    print(f'Vitorias do jogador 1: {vitorias_do_jogador_1}')
                    print(f'Vitorias do jogador 2: {vitorias_do_jogador_2}')
                    print(f'Empates: {empates}')
                    resposta_ja_utilizada.clear()
                    continue

            if resposta == 'E':
                print('Iniciando proximo jogo')
                jogo = [
                    [' ', '|', ' ', '|', ' '],
                    [' ', '|', ' ', '|', ' '],
                    [' ', '|', ' ', '|', ' '],
                ]
                empates += 1
                resposta_ja_utilizada.clear()
                continue

            if resposta == 'S':
                if vitorias_do_jogador_1 > vitorias_do_jogador_2:
                    print('Jogador 1 venceu!')
                elif vitorias_do_jogador_2 > vitorias_do_jogador_1:
                    print('Jogador 2 venceu!')
                elif vitorias_do_jogador_2 == vitorias_do_jogador_1:
                    print('Empate!')
                print('Fim do jogo')
                print(f'Vitorias do jogador 1: {vitorias_do_jogador_1}')
                print(f'Vitorias do jogador 2: {vitorias_do_jogador_2}')
                print(f'Empates: {empates}')
                resposta_ja_utilizada.clear()
                break

            def perguntar_2():
                print('Opções de espaços: 1,2,3,4,5,6,7,8,9 ')
                jogador_2 = input('Jogador 2 digite onde quer colocar o (O): ').upper()

                if jogador_2 not in ('1','2','3','4','5','6','7','8','9','E','S'):
                    print('resposta invalida')
                    return perguntar_2()  # chama a função de novo (volta pra mesma linha)
                elif jogador_2 in resposta_ja_utilizada:
                    print('Espaço já ocupado')
                    return perguntar_2()

                return jogador_2

            resposta_2 = perguntar_2()
            jogador_resposta_2(resposta_2)
            resposta_ja_utilizada.add(resposta_2)

            for tabela in jogo:
                print("".join(str(n) for n in tabela))

            juntar_2 = sum(jogo, [])
            jogo_tupla_2 = tuple(juntar_2)
            valor_antigo_2 = 'X'
            novo_valor_2 = ' '
            lista_2 = list(jogo_tupla_2)

            for i in range(len(lista_2)):
                if lista_2[i] == valor_antigo_2:
                    lista_2[i] = novo_valor_2

            lista_2 = tuple(lista_2)
            vitorias_o = verificado_de_vitorias('O')

            for vitoria in vitorias_o:
                if vitoria == lista_2:
                    print('Jogador 2 venceu!')
                    print('Iniciando proximo jogo')
                    jogo = [
                            [' ', '|', ' ', '|', ' '],
                            [' ', '|', ' ', '|', ' '],
                            [' ', '|', ' ', '|', ' '],
                        ]
                    vitorias_do_jogador_2 += 1
                    print(f'Vitorias do jogador 1: {vitorias_do_jogador_1}')
                    print(f'Vitorias do jogador 2: {vitorias_do_jogador_2}')
                    print(f'Empates: {empates}')
                    resposta_ja_utilizada.clear()
                    continue

            for jogos in jogo:
                if jogos == tipos_de_jogos_2:
                    print('Jogador 2 venceu a partida!')
                    print('Iniciando proximo jogo, Se quiser sair digite ("s")')
                    jogo = [
                        [' ', '|', ' ', '|', ' '],
                        [' ', '|', ' ', '|', ' '],
                        [' ', '|', ' ', '|', ' '],
                    ]
                    vitorias_do_jogador_2 += 1
                    print(f'Vitorias do jogador 1: {vitorias_do_jogador_1}')
                    print(f'Vitorias do jogador 2: {vitorias_do_jogador_2}')
                    print(f'Empates: {empates}')
                    resposta_ja_utilizada.clear()
                    continue

            if resposta_2 == 'E':
                print('Iniciando proximo jogo')
                jogo = [
                    [' ', '|', ' ', '|', ' '],
                    [' ', '|', ' ', '|', ' '],
                    [' ', '|', ' ', '|', ' '],
                ]
                empates += 1
                resposta_ja_utilizada.clear()
                continue

            if resposta_2 == 'S':
                if vitorias_do_jogador_1 > vitorias_do_jogador_2:
                    print('Jogador 1 venceu!')
                elif vitorias_do_jogador_2 > vitorias_do_jogador_1:
                    print('Jogador 2 venceu!')
                elif vitorias_do_jogador_2 == vitorias_do_jogador_1:
                    print('Empate!')
                print('Fim do jogo')
                print(f'Vitorias do jogador 1: {vitorias_do_jogador_1}')
                print(f'Vitorias do jogador 2: {vitorias_do_jogador_2}')
                print(f'Empates: {empates}')
                resposta_ja_utilizada.clear()
                break