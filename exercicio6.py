import csv
def leitura ():
	nomes = input ('Digite vários nomes separados por vírgula: ')
	pessoas = nomes.split(',')
	print (pessoas)
	lista = []

	for nome in pessoas: 
		peso =  float (input ('Digite o peso de {}: ' .format(nome)))
		altura =  float (input ('Digite a altura de {}: ' .format(nome)))
		print ('nome {}, peso {} kg, altura {} m' .format(nome, peso, altura))
		lista.append ((nome, peso, altura))
	return lista

def escrever (nome_arquivo, pessoas):
	coluna = ['Nome', 'Peso', 'Altura']
	with open (nome_arquivo, 'w', newline='') as cvsfile:
		writer = csv.DicWriter(csvfile, fieldnames=colunas)
		writer.writeheader()
		for nome, peso, altura in pessoas:
			pessoa = {}
			pessoa['Nome'] = nome
			pessoa['Peso'] = peso
			pessoa['altura'] = altura
			writer.writerow(pessoa)

pessoas = leitura ()
escrever ('nome_arquivo.csv')