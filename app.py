import os

saldo = 1000.00

def exibir_nome_do_programa():
    print('''
██████╗░░█████╗░███╗░░██╗░█████╗░░█████╗░
██╔══██╗██╔══██╗████╗░██║██╔══██╗██╔══██╗
██████╦╝███████║██╔██╗██║██║░░╚═╝██║░░██║
██╔══██╗██╔══██║██║╚████║██║░░██╗██║░░██║
██████╦╝██║░░██║██║░╚███║╚█████╔╝╚█████╔╝
╚═════╝░╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░░╚════╝░
''')
    
def lista_opcoes():
    print('1. Verificar Saldo')
    print('2. Depositar Dinheiro')
    print('3. Sacar Dinheiro')
    print('4. Sair\n')
    
def verificar_saldo():
    subtitulo('Verificar Saldo')
    print(f'Seu saldo atual é: {saldo:.2f}')
    voltar_menu()

def depositar_dinheiro():
    subtitulo('Depositar Dinheiro')
    deposito = float(input('Insira o valor que deseja depositar em R$: '))

    if deposito > 0:
        global saldo
        saldo += deposito
        print(f'Você depositou o valor de R$ {deposito:.2f} com sucesso!')
    else:
        print(f'Ocorreu um erro ao depositar. Tente novamente.') 
           
    voltar_menu()

def sacar_dinheiro():
    subtitulo('Sacar Dinheiro')
    saque = float(input('Insira o valor que deseja sacar em R$: '))

    if saque > 0:
        global saldo
        saldo -= saque
        print(f'Você sacou o valor de R$ {saque:.2f} com sucesso')
    else:
        print(f'Ocorreu um erro ao sacar. Tente novamente.')
    voltar_menu()

def sair_app():
    subtitulo('A aplicação foi finalizada!')
    os._exit(0)

def opcao_invalida():
    print('Opção invalida')
    voltar_menu()

def escolher_opcoes():
    try:
        opcao_escolhida = int(input('\nEscolha uma opção: '))

        if opcao_escolhida == 1:
            verificar_saldo()
        elif opcao_escolhida == 2:
            depositar_dinheiro()
        elif opcao_escolhida == 3:
            sacar_dinheiro()
        elif opcao_escolhida == 4:
            sair_app()
        else:
           opcao_invalida()
    except:
        opcao_invalida()

def voltar_menu():
    input('\nPreciso qualquer tecla para retornar ao menu principal.')
    main()

def subtitulo(texto):
    os.system('cls')
    linha = '*' * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()
    
def main():
    os.system('cls')
    exibir_nome_do_programa()
    lista_opcoes()
    escolher_opcoes()
    
if __name__ == '__main__':
    while True:    
        main()