# -*- coding: utf-8 -*-
from random import shuffle

class Tabuleiro:

    def __init__(self, DL, TL, DP, TP):
        self.index = [["   " for i in range(15)] for j in range(15)]
        self.preenchido = [] # Armazena os campos que ja foram preenchidos (para IA)
        self.setBonus(DL, TL, DP, TP)
        self.preenchido.append((7, 7))

    def getTabuleiro(self):
        return self.index

    # Devolve para IA um campo do tabuleiro aleatoriamente que ja foi preenchido
    def getPreenchido(self):
        shuffle(self.preenchido)
        return self.preenchido

    def getElemento(self, i, j):
        return self.index[i][j]

    def setBonus(self, DL, TL, DP, TP):
        for posicao in DL:
            self.index[posicao[0]][posicao[1]] = "DL."
        for posicao in TL:
            self.index[posicao[0]][posicao[1]] = "TL."
        for posicao in DP:
            self.index[posicao[0]][posicao[1]] = "DP."
        for posicao in TP:
            self.index[posicao[0]][posicao[1]] = "TP."
        self.index[7][7] = " * "

    def setPalavra(self, palavra, posicao, direcao, jogador):
        direcao.upper()
        palavra = palavra.palavra.upper()

        # HORIZONTAL
        if ((direcao.upper() == "H") or (direcao.upper() == "HORIZONTAL")):
            direcao = "H"
            for i in range(len(palavra)):
                self.index[posicao[0]][posicao[1]+i] = " " + palavra[i] + " "
                self.preenchido.append((posicao[0], posicao[1]+i))

        # VERTICAL
        elif ((direcao.upper() == "V") or (direcao.upper() == "VERTICAL")):
            direcao = "V"
            for i in range(len(palavra)):
                self.index[posicao[0]+i][posicao[1]] = " " + palavra[i] + " " 
                self.preenchido.append((posicao[0]+i, posicao[1]))

    def printTabuleiro(self):
        string = "   | " + " | ".join(str(cabecalho) for cabecalho in range(10)) + " |" + " |".join(str(cabecalho) for cabecalho in range(10, 15)) + " |\n"
        tabuleiro = list(self.index)
        for i in range(len(tabuleiro)):
            # IFs NECESSARIO PARA IDENTAÇÃO DO TABULEIRO
            if i < 10:
                string += str(i) + "  |" + "|".join(str(letra) for letra in tabuleiro[i]) + "|\n"
            if i >= 10:
                string += str(i) + " |" + "|".join(str(letra) for letra in tabuleiro[i]) + "|\n"
        print(string)