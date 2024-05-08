import os

while True:
    def logo_do_jogo():
     print("\n\033[1;31;40mX----------\033[m#_JOGO_DA_VELHA_#\033[1;34;40m----------O\033[m\n\n")

    # Menu de seleção de jogador
    jogadores = ["\033[1;31mX\033[m","\033[1;34mO\033[m"]
    turno = 0
    menu = int(input('''MENU\n\n[1] INICIAR O JOGO\n[2]SAIR DO PROGRAMA\nO que você deseja?  '''))
    while menu != 1 and menu != 2:
        menu = int(input("Digite uma opção válida: "))
    if menu == 1:
        primeiro_jogador = str(input("Escolha 'X' ou 'O' para iniciar o jogo: ")).upper()
        while primeiro_jogador != "X" and primeiro_jogador != "O":  
            primeiro_jogador = str(input("Digite uma escolha válida: ")).upper()
        if primeiro_jogador == "O":
            turno = 1
        else:
            turno = 0   
    else:
        print("JOGO ENCERRADO!")
        exit()

    # Matriz preenchida para ilustrar as jogadas
    demonstração = [[7,8,9],[4,5,6],[1,2,3]]

    # Imprime a matriz Demonstração
    def demonstrar():
        print("\n\033[1;35;44mDEMONSTRAÇÃO:\033[m\n-------------")
        for i in range(3):
            print("\033[1;33;40m|\033[m", end="")
            for j in range(3):
                print(f"\033[1;33;40m {demonstração[i][j]} |\033[m", end="")
            print("\n-------------")

    # Dicionario Mapa de números para posições na matriz
    mapa = {7: (0, 0), 8: (0, 1), 9: (0, 2),
            4: (1, 0), 5: (1, 1), 6: (1, 2),
            1: (2, 0), 2: (2, 1), 3: (2, 2)}

    # Inicializa a matriz que recebe as jogadas
    matriz = [[" " for i in range(3)] for i in range(3)]

    # Função para imprimir a matriz do jogo
    def imprimir_matriz():
        for i in range(3):
            print("\033[1;33;40m|\033[m", end="")
            for j in range(3):
                print(f"\033[1;33;40m {matriz[i][j]} |\033[m", end="")
            print("\n\033[1;34;40m-------------\033[m")

    # Função para verificar se há um vencedor
    def checar_vencedor():
        # Checa linhas
        for i in range(3):
            if matriz[i][0] == matriz[i][1] == matriz[i][2] != " ":
                return matriz[i][0]
        # Checa colunas
        for i in range(3):
            if matriz[0][i] == matriz[1][i] == matriz[2][i] != " ":
                return matriz[0][i]
        # Checa diagonais
        if matriz[0][0] == matriz[1][1] == matriz[2][2] != " ":
            return matriz[0][0]
        if matriz[0][2] == matriz[1][1] == matriz[2][0] != " ":
            return matriz[0][2]
        return None

    # Loop do jogo
    while True:
        # Limpa a tela
        os.system('cls' if os.name == 'nt' else 'clear')
        
        jogada_valida = False

        while not jogada_valida:
            logo_do_jogo()
            demonstrar()
            print(f"\nJOGADOR \033[1m{jogadores[turno]}:\033[m ")
            imprimir_matriz()
            jogada = int(input(f"Digite um número de 1 a 9 para jogar no local correspondente: "))
            if jogada in mapa:
                i, j = mapa[jogada]
                if matriz[i][j] == " ":
                    matriz[i][j] = jogadores[turno]
                    jogada_valida = True
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                    print("Posição já preenchida! Escolha outra.")
                    continue
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
                print("Por favor digite um número de 1 a 9 !!!")
                continue
            turno = (turno + 1) % 2
        vencedor = checar_vencedor()
        if vencedor is not None:
            os.system('cls' if os.name == 'nt' else 'clear')
            imprimir_matriz()
            print(f"O jogador {vencedor} venceu!")
            break
        elif " " not in [matriz[i][j] for i in range(3) for j in range(3)]:
            os.system('cls' if os.name == 'nt' else 'clear')
            imprimir_matriz()
            print("Deu Velha !!!")
            break
        
    #Pergunta ao usuário se ainda quer continuar jogando
    continuar = input("Deseja continuar jogando? (s/n): ").lower()
    while continuar != "s" and continuar != "n":
        continuar = input("Digite uma opção válida(s/n): ").lower()
    if continuar == "n":
        print("FIM DO JOGO!")
        break
