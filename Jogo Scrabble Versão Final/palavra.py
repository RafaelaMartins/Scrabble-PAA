 # -*- coding: utf-8 -*-
class Palavra:

    def __init__(self, palavra, posicao, jogador, direcao, tabuleiro, dicionario, coringa):
        self.palavra = palavra.upper()
        self.palavracoringa = ""
        self.coringa = coringa
        self.posicao = posicao
        self.jogador = jogador
        self.direcao = direcao.upper()
        self.tabuleiro = tabuleiro
        self.dicionario = dicionario

    def setPalavra(self, palavra):
        self.palavra = palavra

    def setPosicao(self, posicao):
        self.posicao = posicao

    def setDirecao(self, direcao):
        self.direcao = direcao

    def getPalavra(self):
        return self.palavra

    def checaPalavra(self, turno_atual):

        pontuacaoPalavra = 0

        # Armazena as letras que ja estão em campo
        letra_campo = ""
        # Armazena as letras que ainda não estão no campo, ou seja, estão na mao 
        letra_mao = ""

        if self.palavra == "":
            return "ERRO: Palavra Vazia"
        # Checa Palavra
        else:
            # Guarda a palavra com coringa para pontuação
            self.palavracoringa = self.palavra
            if "#" in self.palavra:
                # ":" = Fatiamento de Sequências - http://www.devfuria.com.br/python/sequencias-fatiamento/ 
                self.palavra = self.palavra[:self.palavra.index("#")] + self.coringa.upper() + self.palavra[(self.palavra.index("#")+1):]

            if self.palavra not in self.dicionario:
                return "ERRO: Palavra inexistente no dicionario."

            # Confere se alguma letra não excederá as casas do tabuleiro
            if (self.posicao[0] < 0 or self.posicao[1] < 0) or (self.posicao[0] > 14 or self.posicao[1] > 14) or (self.direcao == "V" and (self.posicao[0] + len(self.palavra)-1) > 14) or (self.direcao == "H" and (self.posicao[1] + len(self.palavra)-1) > 14):
                return "ERRO - Palavra excede o tabuleiro.\n"

            # Confere se a direção está correta e quais letras ja estavam em campo
            if self.direcao == "H":
                for i in range(len(self.palavra)):
                    if self.tabuleiro.index[self.posicao[0]][self.posicao[1]+i][1] == " " or self.tabuleiro.index[self.posicao[0]][self.posicao[1]+i] == "DL." or self.tabuleiro.index[self.posicao[0]][self.posicao[1]+i] == "TL." or self.tabuleiro.index[self.posicao[0]][self.posicao[1]+i] == "DP." or self.tabuleiro.index[self.posicao[0]][self.posicao[1]+i] == "TP." or self.tabuleiro.index[self.posicao[0]][self.posicao[1]+i][1] == "*":
                        letra_campo += " "
                    else:
                        letra_campo += self.tabuleiro.index[self.posicao[0]][self.posicao[1]+i][1]
            elif self.direcao == "V":
                for i in range(len(self.palavra)):
                    if self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]][1] == " " or self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]] == "DL." or self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]] == "TL." or self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]] == "DP." or self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]] == "TP." or self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]][1] == "*":
                        letra_campo += " "
                    else:
                        letra_campo += self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]][1]
            else:
                return "ERRO: Direção invalida."

            # Confere se existe letras adjacentes a esta
            if self.direcao == "H":
                if (self.posicao[1]-1 >= 0): # Para não dar erro de index
                    if (self.tabuleiro.index[self.posicao[0]][self.posicao[1]-1][1] != ' ' and self.tabuleiro.index[self.posicao[0]][self.posicao[1]-1][2] != '.'): # Verifica se posição anterior tem letra
                        return "aERRO: Já existe palavras formadas adjacentes a essa"
                if (self.posicao[1] + len(self.palavra) <= 14):
                    if (self.tabuleiro.index[self.posicao[0]][self.posicao[1]+len(self.palavra)][1] != ' ' and self.tabuleiro.index[self.posicao[0]][self.posicao[1]+len(self.palavra)][2] != '.'): # Verifica se a proxima posição tem letra
                        return "bERRO: Já existe palavras formadas adjacentes a essa"
                if (self.posicao[0] != 0):
                    verificador = False
                    for i in range(len(self.palavra)):
                        verificador_anterior = verificador
                        if (self.tabuleiro.index[self.posicao[0]-1][self.posicao[1]+i][1] != ' ' and self.tabuleiro.index[self.posicao[0]-1][self.posicao[1]+i][2] != '.'):
                            verificador = True
                            if (self.tabuleiro.index[self.posicao[0]][self.posicao[1]+i][1] == ' ' or self.tabuleiro.index[self.posicao[0]][self.posicao[1]+i][2] == '.'):
                                return "cERRO: Já existe palavras formadas adjacentes a essa"
                        else:
                            verificador = False
                        if verificador_anterior == verificador and verificador == True:
                            return "dERRO: Já existe palavras formadas adjacentes a essa"
                if (self.posicao[0] != 14):
                    verificador = False
                    for i in range(len(self.palavra)):
                        verificador_anterior = verificador
                        if (self.tabuleiro.index[self.posicao[0]+1][self.posicao[1]+i][1] != ' ' and self.tabuleiro.index[self.posicao[0]+1][self.posicao[1]+i][2] != '.'):
                            verificador = True
                            if (self.tabuleiro.index[self.posicao[0]][self.posicao[1]+i][1] == ' ' or self.tabuleiro.index[self.posicao[0]][self.posicao[1]+i][2] == '.'):
                                return "eERRO: Já existe palavras formadas adjacentes a essa"
                        else:
                            verificador = False
                        if verificador_anterior == verificador and verificador == True:
                            return "fERRO: Já existe palavras formadas adjacentes a essa"
            elif self.direcao == "V":
                if (self.posicao[0]-1 >= 0): # Para não dar erro de index
                    if (self.tabuleiro.index[self.posicao[0]-1][self.posicao[1]][1] != ' ' and self.tabuleiro.index[self.posicao[0]-1][self.posicao[1]][2] != '.'): # Verifica se posição anterior tem letra
                        return "gERRO: Já existe palavras formadas adjacentes a essa"
                if (self.posicao[0] + len(self.palavra) <= 14):
                    if (self.tabuleiro.index[self.posicao[0]+len(self.palavra)][self.posicao[1]][1] != ' ' and self.tabuleiro.index[self.posicao[0]+len(self.palavra)][self.posicao[1]][2] != '.'): # Verifica se a proxima posição tem letra
                        return "hERRO: Já existe palavras formadas adjacentes a essa"
                if (self.posicao[1] != 0):
                    verificador = False
                    for i in range(len(self.palavra)):
                        verificador_anterior = verificador
                        if (self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]-1][1] != ' ' and self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]-1][2] != '.'):
                            verificador = True
                            if (self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]][1] == ' ' or self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]][2] == '.'):
                                return "iERRO: Já existe palavras formadas adjacentes a essa"
                        else:
                            verificador = False
                        if verificador_anterior == verificador and verificador == True:
                            return "jERRO: Já existe palavras formadas adjacentes a essa"
                if (self.posicao[1] != 14):
                    verificador = False
                    for i in range(len(self.palavra)):
                        verificador_anterior = verificador
                        if (self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]+1][1] != ' ' and self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]+1][2] != '.'):
                            verificador = True
                            if (self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]][1] == ' ' or self.tabuleiro.index[self.posicao[0]+i][self.posicao[1]][2] == '.'):
                                return "kERRO: Já existe palavras formadas adjacentes a essa"
                        else:
                            verificador = False
                        if verificador_anterior == verificador and verificador == True:
                            return "lERRO: Já existe palavras formadas adjacentes a essa"

            # Confere se as letras da mão não farão uma sobreposição sobre as do campo
            if (turno_atual != 1):
                for i in range(len(self.palavracoringa)):
                    if letra_campo[i] == " ":
                        letra_mao += self.palavracoringa[i]
                    elif letra_campo[i] != self.palavracoringa[i]:
                        return "ERRO: A palavra não pode sobrepor as letras em campo"
            else:
                letra_mao = self.palavracoringa

            # Confere se a palavra esta conectada com pelo menos uma letra em campo
            if (turno_atual != 1) and (letra_campo == " " * len(self.palavra)):
                return "ERRO: A palavra deve estar conectado a pelo menos uma letra do campo"

            # Confere se o jogador possui letras suficientes para formar a palavra
            if len(letra_mao) == 0:
                return "ERRO - É necessario colocar pelo menos uma letra da mão em campo"
            for letra in letra_mao:
                if letra not in self.jogador.getMao() or self.jogador.getMao().count(letra) < letra_mao.count(letra):
                    return "ERRO - Letras insuficientes"

            # Confere se no primeiro turno foi colocado a palavra no '*'
            if (turno_atual == 1): 
                testador = False
                if self.direcao == "H":
                    for i in range(len(self.palavra)):
                        if [self.posicao[0], self.posicao[1]+i] == [7,7]:
                            testador = True
                else:
                    for i in range(len(self.palavra)):
                        if [self.posicao[0]+i, self.posicao[1]] == [7,7]:
                            testador = True
                if (testador == False):                
                    return "ERRO - Primeiro turno deve conter a palavra no '*' (Posição [7, 7])."

            # RETIRA LETRAS USADAS E REPOEM POR NOVAS DO PACOTE
            for letra in letra_mao:
                self.jogador.removerMao(letra)    
                self.jogador.adicionarMao()   

            return True

    def pontuacaoPalavra(self, VALOR_LETRA, DL, TL, DP, TP):
        pontuacao = 0
        
        if (self.palavracoringa == ''):
            self.palavracoringa = self.palavra

        if (self.direcao == "H"):
            for i in range(len(self.palavracoringa)):
                if ((self.posicao[0], self.posicao[1]+i) in DL) and (self.palavracoringa != '#'):
                    pontuacao += VALOR_LETRA[self.palavracoringa[i]] * 2
                elif ((self.posicao[0], self.posicao[1]+i) in TL) and (self.palavracoringa != '#'):
                    pontuacao += VALOR_LETRA[self.palavracoringa[i]] * 3
                elif (self.palavracoringa != '#'):
                    pontuacao += VALOR_LETRA[self.palavracoringa[i]]
            for i in range(len(self.palavracoringa)):
                if ((self.posicao[0], self.posicao[1]+i) in DP):
                    pontuacao *= 2
                if ((self.posicao[0], self.posicao[1]+i) in TP):
                    pontuacao *= 3
        else:
            for i in range(len(self.palavracoringa)):
                if ((self.posicao[0]+i, self.posicao[1]) in DL) and (self.palavracoringa != '#'):
                    pontuacao += VALOR_LETRA[self.palavracoringa[i]] * 2
                elif ((self.posicao[0]+i, self.posicao[1]) in TL) and (self.palavracoringa != '#'):
                    pontuacao += VALOR_LETRA[self.palavracoringa[i]] * 3
                elif (self.palavracoringa != '#'):
                    pontuacao += VALOR_LETRA[self.palavracoringa[i]]
            for i in range(len(self.palavracoringa)):
                if ((self.posicao[0]+i, self.posicao[1]) in DP):
                    pontuacao *= 2
                if ((self.posicao[0]+i, self.posicao[1]) in TP):
                    pontuacao *= 3
        return pontuacao