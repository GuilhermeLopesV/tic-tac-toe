from features_package.game import game


def main():
    print('=== JOGO DA VELHA ===')

    while True:
        option = input('(I)niciar ou (S)air: ').strip().upper()

        if option == 'I':
            game()
        elif option == 'S':
            print('Saindo...')
            break
        else:
            print('Opção inválida!')


if __name__ == "__main__":
    main()