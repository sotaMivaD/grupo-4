import os

def logo():
    mensagem = ("BEM VINDO AO PALAVRAS CRUZADAS!")
    print("-" * len(mensagem))
    print(mensagem)
    print("-" * len(mensagem))

def menu():
    mensagem = ("           MENU           ")
    print("-" * len(mensagem))
    print(mensagem)
    print("-" * len(mensagem))
    escolha = input("Digite 1 para INICIAR e 2 para SAIR: ")
    while escolha != "1" and escolha != "2":
        escolha = input("Escolha inválida. Digite 1 para INICIAR e 2 para SAIR: ")
    if escolha == "1":
        print("Jogo iniciado")
        cenario = int(input("Digite o tema ((1)animais, (2)país ou (3)frutas): "))
        return cenario
    else:
        print("Fim do jogo!")
        exit()
    
class Tabuleiro:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.tabuleiro = [[' ']*tamanho for _ in range(tamanho)]

    def preencher_palavra(self, palavra, linha, coluna, direcao):
        if direcao == 'horizontal':
            for i, letra in enumerate(palavra):
                self.tabuleiro[linha][coluna+i] = letra
        elif direcao == 'vertical':
            for i, letra in enumerate(palavra):
                self.tabuleiro[linha+i][coluna] = letra

    def mostrar_tabuleiro(self):
        for linha in self.tabuleiro:
            print(' '.join(linha))

tabuleiro = Tabuleiro(15)

logo()

def jogo1():
    tabuleiro.preencher_palavra('caranguejo', 5, 0, 'horizontal')
    tabuleiro.preencher_palavra('***g***', 2, 5, 'vertical')
    tabuleiro.preencher_palavra('c****', 5, 0, 'vertical')
    tabuleiro.preencher_palavra('*r***', 4, 2, 'vertical')
    tabuleiro.preencher_palavra('***o', 2, 9, 'vertical')
    tabuleiro.preencher_palavra('**e***', 3, 7, 'vertical')
    tabuleiro.preencher_palavra('1↓', 3, 0, 'vertical')
    tabuleiro.preencher_palavra('2↓', 2, 2, 'vertical')
    tabuleiro.preencher_palavra('3↓', 0, 5, 'vertical')
    tabuleiro.preencher_palavra('4↓', 1, 7, 'vertical')
    tabuleiro.preencher_palavra('5↓', 0, 9, 'vertical')

    animais = {1:"cobra", 2:"arara", 3:"canguru", 4:"coelho", 5:"leao"}

    palavras_acertadas = 0
    while palavras_acertadas < 5:
        tabuleiro.mostrar_tabuleiro()

        print("\033[1;35m DICAS: \033[m\n")
        print(''' 
            1- São conhecidas por seu corpo longo e sem membros.
            2- São conhecidas por suas penas coloridas e seu bico forte e curvado.
            3- São conhecidos por suas pernas traseiras grandes e fortes, que são usadas para saltar a grandes distâncias.
            4- São pequenos mamíferos conhecidos por suas orelhas longas e cauda fofa.
            5- São carnívoros e conhecidos por sua juba distinta nos machos.\n''')

        escolha = int(input("Escolha um número correspondente a uma dica: "))
        while escolha not in animais:
            escolha = int(input("Escolha uma dica válida(1 a 5):"))
        if escolha in animais:
            chute = input(f"Digite a palavra da dica {escolha}: ").lower()
            os.system('cls' if os.name == 'nt' else 'clear')
            if chute == animais[escolha]:
                print(f"VOCÊ ACERTOU!!!!")
                del(animais[escolha]) 
                palavras_acertadas+=1
            else:
                print("Infelizmente, isso não está correto. Tente novamente!")

        if palavras_acertadas == 5:
            print("Parabéns, você acertou todas as palavras!")
            break

def jogo2():
    tabuleiro.preencher_palavra("madagascar", 5, 0, 'horizontal')
    tabuleiro.preencher_palavra("m*****",5, 0, 'vertical')
    tabuleiro.preencher_palavra("****d**",1, 2, 'vertical')
    tabuleiro.preencher_palavra("g*****",5, 4, 'vertical')
    tabuleiro.preencher_palavra("*s****",4,6, 'vertical')
    tabuleiro.preencher_palavra("*****a***",0,8, 'vertical')


    pais = {1: "mexico", 2: "equador", 3: "grecia", 4: "israel", 5: "australia"}

    palavras_acertadas = 0
    while palavras_acertadas < 5:
        tabuleiro.mostrar_tabuleiro()
        print("\033[1;33m DICAS: \033[m\n")
        print('''
            1- Pais onde é comemorado o dia da morte.
            2- Divide o hemisferio norte e sul.
            3- Os grandes filosofos sairam de lá.
            4- Berço das religioes monoteistas.  
            5- Possui grande quantidade de animais exoticos.''')

        escolha = int(input("Escolha um número correspondente a uma dica: "))
        while escolha not in pais:
            escolha = int(input("Escolha uma dica válida(1 a 5):"))
        if escolha in pais:
            chute = input(f"Digite a palavra da dica {escolha}: ").lower()
            os.system('cls' if os.name == 'nt' else 'clear')
            if chute == pais[escolha]:
                print(f"VOCÊ ACERTOU!!!!")
                del(pais[escolha]) 
                palavras_acertadas+=1
            else:
                print("Infelizmente, isso não está correto. Tente novamente!")

        if palavras_acertadas == 5:
            print("Parabéns, você acertou todas as palavras!")
        
        
def jogo3():
        tabuleiro.preencher_palavra("framboesas", 0, 5, 'vertical')
        tabuleiro.preencher_palavra("f***",0, 5, 'horizontal')
        tabuleiro.preencher_palavra("*a****",2, 4, 'horizontal')
        tabuleiro.preencher_palavra("m*******",3, 5, 'horizontal')
        tabuleiro.preencher_palavra("s********",7,5, 'horizontal')
        tabuleiro.preencher_palavra("****a",8,1, 'horizontal')


        frutas = {1: "figo", 2: "banana", 3: "maracuja", 4: "siriguela", 5: "manga"}

        palavras_acertadas = 0
        while palavras_acertadas < 5:
            tabuleiro.mostrar_tabuleiro()
            print("\033[1;34m DICAS: \033[m\n")
            print('''  
                1- Simboliza sorte e fartura .
                2- A fruta favorita do macaco.
                3- Fruta que acalma.
                4- Fruto pequena e amarela.  
                5- Tem na camisa.''')

            escolha = int(input("Escolha um número correspondente a uma dica: "))
            while escolha not in frutas:
                escolha = int(input("Escolha uma dica válida(1 a 5):"))
            if escolha in frutas:
                chute = input(f"Digite a palavra da dica {escolha}: ").lower()
                os.system('cls' if os.name == 'nt' else 'clear')
                if chute == frutas[escolha]:
                    print(f"VOCÊ ACERTOU!!!!")
                    del(frutas[escolha]) 
                    palavras_acertadas+=1
                else:
                    print("Infelizmente, isso não está correto. Tente novamente!")

            if palavras_acertadas == 5:
                print("Parabéns, você acertou todas as palavras!")

cenario = menu()
os.system('cls' if os.name == 'nt' else 'clear')
if cenario == 1:
    jogo1()
elif cenario == 2:
    jogo2()
else:
    jogo3()
