# -*- coding: utf-8 -*-
class Jogador:
    
    def __init__(self, pacote):
        self.nome = ""
        self.pontuacao = 0
        self.pacote = pacote
        self.mao = []
        # Adiciona as 7 letras iniciais na mão do jogador.
        for i in range(7):
            self.adicionarMao()
        
    def setNome(self, nome):
        self.nome = nome

    def getNome(self):
        return self.nome

    def aumentarPontuacao(self, aumento):
        self.pontuacao += aumento

    def getPontuacao(self):
        return self.pontuacao   

    def adicionarMao(self):
        # Retira do pacote e coloca na mão uma letra.
        letra = self.pacote.retirar()
        if letra != "0":
            self.mao.append(letra)

    def getMao(self):
        return self.mao

    def getMaoStr(self):
        string = ""
        for i in range(self.tamanhoMao()):
            string += self.mao[i]
        return string

    def removerMao(self, letra):
        self.mao.remove(letra)

    def tamanhoMao(self):
        return len(self.mao)

    def trocarMao(self, letra):
        self.removerMao(letra)
        self.pacote.adicionar(letra)
        self.mao.append(self.pacote.retirar())
        