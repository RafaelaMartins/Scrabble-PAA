# -*- coding: utf-8 -*-
from random import shuffle

class Pacote:

    def __init__(self):
        # Inicializa o pacote com 100 letras.
        self.pacote = []
        self.add("A", 14)
        self.add("B", 3)
        self.add("C", 4)
        self.add("D", 5)
        self.add("E", 11)
        self.add("F", 2)
        self.add("G", 2)
        self.add("H", 2)
        self.add("I", 10)
        self.add("J", 2)
        self.add("L", 5)
        self.add("M", 6)
        self.add("N", 4)
        self.add("O", 10)
        self.add("P", 4)
        self.add("Q", 1)
        self.add("R", 6)
        self.add("S", 8)
        self.add("T", 5)
        self.add("U", 7)
        self.add("V", 2)
        self.add("X", 1)
        self.add("Z", 1)
        self.add("Ç", 2)
        self.add("#", 3) # "#" representa uma peça em branco.
        shuffle(self.pacote) # Embaralha o pacote.

    def add(self, letra, quantidade):
        for i in range(quantidade):
            self.pacote.append(letra)

    def adicionar(self, letra):
        self.pacote.append(letra)
        shuffle(self.pacote)

    def retirar(self):
        if (len(self.pacote)) > 0:
            return self.pacote.pop()
        return "0"

    def tamanho(self):
        return len(self.pacote)
