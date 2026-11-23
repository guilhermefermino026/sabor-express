import subprocess
import os

def exibir_menu():
    print(""" 
𝕊𝕒𝕓𝕠𝕣 𝔼𝕩𝕡𝕣𝕖𝕤𝕤
""")

def exibir_opcoes():
    print('1. Cadastrar restaurante')
    print('2. Listar restaurante')
    print('3. Ativar restaurante')
    print('4. Sair\n')

def finalizar_app():
    subprocess.run('clear', check=False)
    # os.system('clear') is deprecated, the recommendation is to use the subprocess
    print('Finalizando o app')

def escolher_opcao():
    opcao_escolhida = int(input('Escolha uma opção: '))
    if opcao_escolhida == 1:
        print('Cadastrar restaurante')
    elif opcao_escolhida == 2:
        print('Listar restaurante')
    elif opcao_escolhida == 3:
        print('Ativar restaurante')
    else:
        finalizar_app()


#if 25 <= tempo <= 45:
# TEMPO ESTÁ CERCADO POR 25 E 45, LOGO DEVE ESTAR NESSE RANGE


def main():
    exibir_menu()
    exibir_opcoes()
    escolher_opcao()

if __name__ == '__main__':
    main()