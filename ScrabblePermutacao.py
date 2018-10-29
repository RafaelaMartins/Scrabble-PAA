# -*- coding: utf-8 -*-
from typing import Tuple
from multiprocessing.pool import ThreadPool
import time
result = []


A = ""
R = []
C = False
def permutation(list, start, end,root):
    '''This prints all the permutations of a given list
       it takes the list,the starting and ending indices as input'''
    if (start == end ):
    	#print(list)
    	#print(list)
    	
    	teste = find_prefix(root,''.join(list))
    	if teste[0]:
            #print("ENTROU")
            #print(''.join(list))
            global R 
            R = (''.join(list))
            global C
            C = True 
            

    else:
        for i in range(start, end + 1):
            list[start], list[i] = list[i], list[start]  # The swapping
            permutation(list, start + 1, end,root)
            list[start], list[i] = list[i], list[start]  # Backtracking 
            
    	


class TrieNode(object):

    def __init__(self, char: str):
        self.char = char
        self.children = []
        #É o ultimo caractere da palavra
        self.wordfinished = False;
        #Quantas vezes o caractere aparece
        self.counter = 1
        #função adiciona palavra 
        
def add(root,word):
    node = root
    for char in word:
        found_in_child=False
        #Busca pelo caractere no node
        for child in node.children:
            if child.char == char:
             # Nos encontramos isso, aumenta o contador por 1 para manter-lo na hora buscar outro
                child.counter+=1 #E aponte o nó para o filho que contém este caractere
                node = child
                found_in_child = True
                break # Nós não achamos isso, então adicione um novo filho
     
        if not found_in_child:
            new_node = TrieNode(char)
            node.children.append(new_node) 
            # E, em seguida, apontar o nó para o novo filho
            node = new_node # Tudo terminou. Marque-o como o fim de uma palavra.    
    node.wordfinished = True 

def find_prefix(root, prefix: str) -> Tuple[bool, int]:
    """
    Valida e  retorna 
    1. Se o prefixo existe em qualquer palavra nós adicionamos
    2. Se sim então quantas palavras atualmente tem o prefixo
    """
    node = root
    # Se o nó raiz não tem filho, então retorna falso.
    # Porque isso significa que nós estamos tentando procurar em uma arvore vazia
    if not root.children:
        return False, 0
    for char in prefix:
        char_not_found = True
        # Procura através de todos os filhos do nó presente
        for child in node.children:
            if child.char == char:
                # Nós encontramos o char existindo no filho
                char_not_found = False
                # Associe o nó com o filho que contém o char e quebre
                node = child
                break
        # Retorna False de qualquer maneira quando não encotramos o char.` 
        if char_not_found:
            return False, 0
    # Well, we are here means we have found the prefix. Return true to indicate that
    # And also the counter of the last node. This indicates how many words have this
    # prefix
    return True, node.counter

if __name__ == "__main__":
    root = TrieNode('*')
    arquivo = open('wordlist.txt', 'r')
    i=0
    for linha in arquivo:
    	add(root, linha)
    	#print(linha)
    	i+=1
    	#print(i)

    arquivo.close()
    entrada = input('Entre com um conjunto de palavras: ')
    w = list(entrada)
    #print(type(w))
    tam = len(w)
    tam=tam-1
    #print(w)
    #print(tam)

    #print(permute(tam, w))
    permutation(w,0,tam,root)
    print(C)
    print(R)
    #print(type(comb))
    #aux = []
    #aux=tuple(comb)
    #print(aux)
    #print(type(aux))
    #n = 0
    #for n in aux:
    	
    #	teste = find_prefix(root, n)
    #	if teste[0]:
    #		print(n)
    #		break; 

    #teste = find_prefix(root, 'abacate')
    #print(find_prefix(root, 'abacate'))
    #print(teste[0])	
    	

    #add(root, "hackathon")
    #add(root, 'hack')
    #print(find_prefix(root, 'hac'))
    #print(find_prefix(root, 'hack'))
    #print(find_prefix(root, 'hackathon'))  
    #print(find_prefix(root, 'ha'))
    #print(find_prefix(root, 'hammer'))

