from features_package.game import jogo


def main():
    print('=== JOGO DA VELHA ===')

    while True:
        opcao = input('(I)niciar ou (S)air: ').upper()

        if opcao == 'I':
            jogo()
        elif opcao == 'S':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')


if __name__ == "__main__":
    main()