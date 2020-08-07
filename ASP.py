#  CAIO VICTOR DO AMARAL CUNHA SARMENTO
#  UFPB - CENTRO DE INFORMATICA -  2020
#       ENGENHARIA DE COMPUTACAO

file = open("entrada.txt", "r")							#Abre o arquivo de entrada

linhas = file.readlines()								#Pega as linhas
i = 1
array = []												#Cria o array dos numeros
quadros = int(linhas[0])								#Adiciona o numero de quadros a variavel quadros

for linha in linhas[1:]:								#Armazena no array os numeros do arquivo
	array.insert(i, int(linha.strip()))
	i += 1

def FIFO(lista):										#Funcao FirstIn, First Out
	memoria = []										#Cria o array para a memória
	faltas = 0											#Faltas de memoria
	index = 0											#Indice para adicionar a memoria

	for x in range (len(lista)):										#Laco principal
		if lista[x] not in memoria and len(memoria) < quadros:			#Caso o elemento atual nao esteja na memoria e a memoria nao esteja cheia
			memoria.insert(x, lista[x])									#Insere o elemento atual e incrementa as faltas
			faltas += 1
		elif lista[x] not in memoria and len(memoria) >= quadros:		#Caso o elemento atual nao esteja na memoria e a memoria esteja cheia
			memoria[index] = lista[x]									#Substitui na memoria no indice baseado no FIFO
			faltas += 1													#Incrementa as faltas e o indice
			index += 1
		if index == quadros:											#Caso o indice chegue ao tamanho do quadro, reinicia
			index = 0
		#print(lista[x],memoria, faltas)
	print("FIFO", faltas)												#Printa as faltas do FIFO

def OTM(lista):											#Funcao Otima
	memoria = []										#Cria o array para a memória
	exist = [0] * quadros 								#Cria um array para verificar se o elemento esta na memoria
	faltas = 0											#Faltas na memoria											

	for x in range (len(lista)):										#Laco principal
		if lista[x] not in memoria and len(memoria) < quadros:			#Caso o elemento atual nao esteja na memoria e a memoria nao esteja cheia
			memoria.insert(x, lista[x])									#Insere o elemento atual e incrementa as faltas
			faltas += 1
		elif lista[x] not in memoria and len(memoria) >= quadros:		#Caso o elemento atual nao esteja na memoria e a memoria esteja cheia
			for y in range (x, len(lista)):								#Percorre os elementos futuros da lista
				if lista[y] in memoria and sum(exist) < quadros:		#Caso o elemento que esta verificando esteja na memoria e a soma do exist seja menor que os quadros
					exist[memoria.index(lista[y])] =  1					#Significa que ainda nao preencheu todo o exist, setando o indice do elemento na memoria pra 1

				if sum(exist) == quadros:								#Caso o exist esteja cheio
					memoria[memoria.index(lista[y])] = lista[x]			#O ultimo elemento que foi adicionado no exist é o que vai ser trocado na memoria
					faltas += 1											#Incrementa as faltas
					exist = [0] * quadros								#Zera o exist
					break												#Sai do laço

				elif sum(exist) < quadros and y == len(lista) - 1:		#Caso a soma dos itens de exist seja menor que o tamanho do quadro e a lista estiver terminado
					for z in range (0, quadros):						#O metodo de substituir se torna FIFO, indo para o primeiro elemento que nao "exist" no for
						if exist[z] != 1:								#Se o elemento do exist for diferente de 1, substitui pelo elemento atual
							memoria[z] =  lista[x]						
							faltas += 1									#Incrementa as faltas
							exist = [0] * quadros						#Zera o exist
							break										#Sai do laco
		#print(lista[x],memoria, faltas)	
	print("OTM", faltas)												#Printa as faltas do OTM

def LRU (lista):									#Funcao Least Recently Used 
	memoria = []									#Cria o array para a memoria
	lista_aux = []									#Cria o array auxiliar para a lista
	exist = [0] * quadros 							#Cria um array para verificar se o elemento esta na memoria
	faltas = 0										#Faltas na memoria

	for x in range (len(lista)):										#Laco principal
		if lista[x] not in memoria and len(memoria) < quadros:			#Caso o elemento atual nao esteja na memoria e a memoria nao esteja cheia
			memoria.insert(x, lista[x])									#Insere o elemento atual e incrementa as faltas
			faltas += 1
		elif lista[x] not in memoria and len(memoria) >= quadros:		#Caso o elemento atual nao esteja na memoria e a memoria esteja cheia
			lista_aux = lista.copy()									#Copia a lista para uma lista auxiliar
			lista_aux.reverse()											#Reverte a lista
			
			for y in range (len(lista_aux) - x, len(lista_aux)):		#Percorre os elementos passados da lista
				if lista_aux[y] in memoria and sum(exist) < quadros:	#Caso o elemento que esta verificando esteja na memoria e a soma do exist seja menor que os quadros
					exist[memoria.index(lista_aux[y])] =  1				#Significa que ainda nao preencheu todo o exist, setando o indice do elemento na memoria pra 1

				if sum(exist) == quadros:								#Caso o exist esteja cheio
					memoria[memoria.index(lista_aux[y])] = lista[x]		#O ultimo elemento que foi adicionado no exist é o que vai ser trocado na memoria
					faltas += 1											#Incrementa as faltas
					exist = [0] * quadros								#Zera o exist
					break												#Sai do laço

				elif sum(exist) < quadros and y == len(lista) - 1:		#Caso a soma dos itens de exist seja menor que o tamanho do quadro e a lista estiver terminado
					for z in range (0, quadros):						#O metodo de substituir se torna FIFO, indo para o primeiro elemento que nao "exist" no for
						if exist[z] != 1:								#Se o elemento do exist for diferente de 1, substitui pelo elemento atual
							memoria[z] =  lista[x]
							faltas += 1									#Incrementa as faltas
							exist = [0] * quadros						#Zera o exist
							break										#Sai do laco
		#print(lista[x],memoria, faltas)
	print("LRU", faltas)												#Printa as faltas do LRU

if quadros <= 0:								#Caso o numero de quadros seja 0, todas as faltas sao 0
	print("FIFO 0\nOTM 0\nLRU 0")
else:											#Caso contrario, chama as funcoes
	FIFO(array)
	OTM(array)
	LRU(array)