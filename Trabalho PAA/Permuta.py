tam = 0
A = ""
R = []
def permutation(list, start, end,root):
    '''This prints all the permutations of a given list
       it takes the list,the starting and ending indices as input'''
    if (start == end):
    	#print(list)
    	i = 6
    	print(list)
    	A = list[0]+list[1]+list[2]+list[3]+list[4]+list[5]+list[6]
    	teste = find_prefix(root, A)
    	if teste[0]:
    		print(n)
    		break; 
    else:
        for i in range(start, end + 1):
            list[start], list[i] = list[i], list[start]  # The swapping
            permutation(list, start + 1, end)
            list[start], list[i] = list[i], list[start]  # Backtracking 
    	

    	
    	
            


entrada = input('Entre com um conjunto de palavras: ')
w = list(entrada)
permutation(w, 0, 6)

