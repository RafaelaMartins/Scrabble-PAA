# -*- coding: utf-8 -*-
from tabuleiro import Tabuleiro
from jogador import Jogador
from pacote import Pacote
from palavra import Palavra
from ia import *
import os
import pickle
import cProfile
import pstats
p= cProfile.Profile()
p.enable()




# VALOR DE PONTUAÇÃO DE CADA LETRA
VALOR_LETRA = {"A": 1,
               "B": 3,
               "C": 2,
               "D": 2,
               "E": 1,
               "F": 4,
               "G": 4,
               "H": 4,
               "I": 1,
               "J": 5,
               "L": 2,
               "M": 1,
               "N": 3,
               "O": 1,
               "P": 2,
               "Q": 6,
               "R": 1,
               "S": 1,
               "T": 1,
               "U": 1,
               "V": 4,
               "X": 8,
               "Z": 8,
               "Ç": 3,
               "#": 0}

# POSIÇÕES DAS CASAS BONUS NO TABULEIRO
DL = ((0, 3), (0,11), (2,6), (2,8), (3,0), (3,7), (3,14), (6,2), (6,6), (6,8), (6,12), (7,3), (7,11), (8,2), (8,6), (8,8), (8, 12), (11,0), (11,7), (11,14), (12,6), (12,8), (14, 3), (14, 11))
TL = ((1,5), (1, 9), (5,1), (5,5), (5,9), (5,13), (9,1), (9,5), (9,9), (9,13), (13,5), (13,9))
DP = ((1,1), (2,2), (3,3), (4,4), (1,13), (2,12), (3,11), (4,10), (13,1), (12,2), (11,3), (10,4), (13,13), (12, 12), (11,11), (10,10))
TP = ((0,0), (7,0), (14,0), (0,7), (14,7), (0,14), (7,14), (14,14))



def turno(jogador_atual, tabuleiro, pacote):
#É passado o nome do jogador que está realizando a jogada, o tabuleiro atual,pacote de letras sorteados
    global jogador, passar_turno, turno_atual, dicionario, modo_jogo
    #Turno atual é variavel global de ia.py assim como, turno atual e dicionario.
    # Final da partida — A partida terminará quando não houver mais pedras no saquinho e: um jogador ficar sem letras ou os dois jogadores passarem duas vezes.
    if ((pacote.tamanho()) == 0 and ((jogador_atual.tamanhoMao() == 0) or (passar_turno >= 4))):
    #Se o tamanho pacote é igual a  0 e as letras na mão do jogador atual são 0 ou o jogador atual passou a vez mais de 4 vezes finaliZA
    #Pq acabou as letras do pacote e não tem letra pra por na mão, ou já estou os passa a vez 
        finalizar()
    else:
        
        os.system('cls' if os.name == 'nt' else 'clear')
        #limpa o terminal
        tabuleiro.printTabuleiro()
        #mostra tabuleiro
        print("Pontuação: | Jogador " + jogador[0].getNome() + " - " + str(jogador[0].getPontuacao()) + " | Jogador " + jogador[1].getNome() + " - " + str(jogador[1].getPontuacao()) + " | ")
        #mostra a pontuação e os respectivos nomes de cada jogador
        print("\n#### Turno do jogador: " + jogador_atual.getNome()+ " ####")
        #mostra de quem é o turno atual
        print("Letras Disponiveis: " + jogador_atual.getMaoStr())
        #exibe as letras disponiveis para o jogador atual

        # REPETE ATÉ QUE O JOGADOR ESCOLHA UMA OPÇÃO VALIDA
        while True:
            while True:
                print("1 - Selecionar palavra / 2 - Trocar Mão / 3 - Passar Turno")
                opcao = input("Selecione uma opção: ")
                if (opcao == '1') or (opcao == '2') or (opcao == '3') or (opcao == '4'):
                    break
            opcao = int(opcao)        
            if ((opcao >= 1) and (opcao <= 4)):
                if (opcao == 1):

                    # REPETE ATÉ QUE O JOGADOR COLOQUE UMA PALAVRA VALIDA
                    while True:
                        palavra = input("Palavra: ")
                        posicao = []
                        linha = input("Linha: ")
                        coluna = input("Coluna: ")
                        #Se linha ou coluna são vazios ou a linha é um valor <0 ou >15 e coluna valor <0 ou >15
                        if ((linha == "") or (coluna == "")) or ( (linha ) not in [str(x) for x in range(15)] or coluna not in [str(x) for x in range(15)]):
                            posicao = [-1, -1] #Posicao invalida
                        else:
                            posicao = [int(linha), int(coluna)] #posicao recebe a linha e a coluna digitada
                        direcao = input("Direção (H - Horizontal / V - Vertical): ") #direção armazena v ou h
                        coringa = ""
                        if "#" in palavra:#se contem um coringa
                            while len(coringa) != 1:#enquanto ogador nãoe scolher valor de #
                                coringa = input("Coloque a letra que representa o Coringa: ")
                                #recebe valor coringa
                        palavra = Palavra(palavra, posicao, jogador_atual, direcao, tabuleiro, dicionario, coringa)
                        #Chama a classe palavra, passando a palavra escrita pelo jogador,posição que ele deseja colocar,quem é o jogador atual
                        #Qual a direção, qual o tabuleiro atual,dicionario original setado, valor coringa
                        #Palavra é um objeto que verifica o tabuleiro pra adicionar a palavra
                        boolean = palavra.checaPalavra(turno_atual)
                        #se possivel adicionar boolean recebe true

                        if (boolean == True):
                        	#verifica a potuação e seta o novo ponto no jogador atual
                            jogador_atual.aumentarPontuacao(palavra.pontuacaoPalavra(VALOR_LETRA, DL, TL, DP, TP))
                            tabuleiro.setPalavra(palavra, posicao, direcao, jogador_atual)
                            #verifica horizontal e vertical

                            passar_turno = 0
                            break;
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                            tabuleiro.printTabuleiro()
                            print("Pontuação: | Jogador " + jogador[0].getNome() + " - " + str(jogador[0].getPontuacao()) + " | Jogador " + jogador[1].getNome() + " - " + str(jogador[1].getPontuacao()) + " | ")
                            print("\n#### Turno do jogador: " + jogador_atual.getNome()+ " ####")
                            print("Letras Disponiveis: " + jogador_atual.getMaoStr())
                            print("!!!!! " + boolean + " !!!!!")

                    
                if (opcao == 2):
                    letras = input("Quais letras deseja trocar: ").upper()
                    for i in range(len(letras)):
                        jogador_atual.trocarMao(letras[i])
                    if (turno_atual == 1):
                        turno_atual -= 1

                if (opcao == 3):
                    print("Turno passado")
                    if (turno_atual == 1):
                        turno_atual -= 1
                    passar_turno += 1

                # DEBUG
                if (opcao == 4):
                    print("FINALIZANDO")
                    finalizar()

                # SE TODOS OS DADOS ESTIVEREM CORRETOS, NÃO REPETE
                break;
            os.system('cls' if os.name == 'nt' else 'clear')
            tabuleiro.printTabuleiro()
            print("Pontuação: | Jogador " + jogador[0].getNome() + " - " + str(jogador[0].getPontuacao()) + " | Jogador " + jogador[1].getNome() + " - " + str(jogador[1].getPontuacao()) + " | ")
            print("\n#### Turno do jogador: " + jogador_atual.getNome()+ " ####")
            print("Letras Disponiveis: " + jogador_atual.getMaoStr())

        
        turno_atual += 1
        # CHAMA O PROXIMO JOGADOR
        if jogador[0].getNome() == jogador_atual.getNome():
            if (modo_jogo == 2):#se o o modo for jogador vs ia então chama turno ia
                turno_ia(jogador[1], tabuleiro, pacote)
            else:
                turno(jogador[1], tabuleiro, pacote)
        else:
            turno(jogador[0], tabuleiro, pacote)


def turno_ia(jogador_atual, tabuleiro, pacote):
    global jogador, passar_turno, turno_atual, dicionario, dicionario_ordenado, modo_jogo

    print("\nComputador: Pensando...")

    # Final da partida — A partida terminará quando não houver mais pedras no saquinho e: um jogador ficar sem letras ou os dois jogadores passarem duas vezes.
    if ((pacote.tamanho()) == 0 and ((jogador_atual.tamanhoMao() == 0) or (passar_turno >= 4))): 
        finalizar()
    else:    
        jogada = jogada_ia(jogador_atual, tabuleiro, pacote, turno_atual, dicionario, dicionario_ordenado)

        """
            jogada: tupla de (opção, palavra, posicao, direção, coringa)
            Opção: 1: jogada normal
            Opção: 2: Trocar mão
            Opção: 3: Passar turno
        """
        
        if (jogada[0] == 1):
            palavra = Palavra(jogada[1], jogada[2], jogador_atual, jogada[3], tabuleiro, dicionario, jogada[4])
            jogador_atual.aumentarPontuacao(palavra.pontuacaoPalavra(VALOR_LETRA, DL, TL, DP, TP))
            tabuleiro.setPalavra(palavra, jogada[2], jogada[3], jogador_atual)
            passar_turno = 0

        if (jogada[0] == 2):
            letras = trocar_mao_ia()
            for i in range(len(letras)):
                jogador_atual.trocarMao(letras[i])
            if (turno_atual == 1):
                turno_atual -= 1
            if pacote.tamanho() < 10:
                passar_turno += 1
                if passar_turno >= 4:
                    finalizar()

        if (jogada[0] == 3):
            if (turno_atual == 1):
                turno_atual -= 1
            passar_turno += 1
            if passar_turno >= 4:
                finalizar()
        
        turno_atual += 1
        # CHAMA O PROXIMO JOGADOR
        if jogador[0].getNome() == jogador_atual.getNome():
            if (modo_jogo == 2):
                print("TURNO DA IA")
            else:
                turno(jogador[1], tabuleiro, pacote)
        else:
            turno(jogador[0], tabuleiro, pacote)


# INICIA O JOGO
def iniciar():
    global jogador, passar_turno, turno_atual, dicionario, dicionario_ordenado, modo_jogo
    
    tabuleiro = Tabuleiro(DL, TL, DP, TP)
    pacote = Pacote()
    jogador = []
    passar_turno = 0
    turno_atual = 1

    dicionario = set()
    dicionario_ordenado = {}
    
    pkl_file = open('dicionario.pkl', 'rb')
    dicionario = pickle.load(pkl_file)
    pkl_file.close()

    pkl_file = open('dicionario_ordenado.pkl', 'rb')
    dicionario_ordenado = pickle.load(pkl_file)
    pkl_file.close()


    if dicionario == "":
        print("ERRO - Dicionario não foi carregado corretamente")

    # MENU DE INICIO
    os.system('cls' if os.name == 'nt' else 'clear')
    print("#-----------------------------------------------#")
    print("|  SCRABBLE - PROJETO E ANÁLISE DE ALGORITIMOS  |")
    print("|                     TeamR                     |")
    print("|         Luiz Eduardo Pereira - 0021619        |")
    print("|        Rafaela Martins Vieira - 0002852       |")
    print("#-----------------------------------------------#")
    print("\n\n\n")
    print("Modos de Jogo:")
    print("    1 - Jogador vs Jogador")
    print("    2 - Jogador vs Computador")
    modo_jogo = int(input("Escolha uma opção: "))
    while ((modo_jogo < 1) or (modo_jogo > 2)):
        modo_jogo = int(input("Escolha uma opção válida (1 / 2): "))

    # ESCOLHA DE NOMES DOS JOGADORES
    jogador.append(Jogador(pacote))
    jogador[0].setNome(input("Nome do Jogador 1: "))
    jogador.append(Jogador(pacote))
    if (modo_jogo == 1):    
        jogador[1].setNome(input("Nome do Jogador 2: "))
    else:
        jogador[1].setNome("Computador")

    jogador_atual = jogador[0]
    turno(jogador_atual, tabuleiro, pacote)


# FINALIZA O JOGO
def finalizar():
    global jogador

    os.system('cls' if os.name == 'nt' else 'clear')
    if (jogador[0].getPontuacao() == jogador[1].getPontuacao()):
        print("FIM DE JOGO!")
        print("EMPATE")
        print("PONTUAÇÃO: " + str(jogador[0].getPontuacao()))    
    elif (jogador[0].getPontuacao() > jogador[1].getPontuacao()):
        print("FIM DE JOGO!")
        print("VENCEDOR: " + jogador[0].getNome())
        print("PONTUAÇÃO: " + str(jogador[0].getPontuacao()))
    else:
        print("FIM DE JOGO!")
        print("VENCEDOR: " + jogador[1].getNome())
        print("PONTUAÇÃO: " + str(jogador[1].getPontuacao()))
    pstats.Stats(p).sort_stats('cumulative').print_stats(30)    
    exit()

# INICIA TODOS OS COMPONENTES NECESSARIO PARA O JOGO COMEÇAR


iniciar()