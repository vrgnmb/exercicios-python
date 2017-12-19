def  imc (peso, altura):
	return  (peso / (altura ** 2) )	

nomes = input ('Digite os nomes: ')
pessoas = nomes.split (',')
print (pessoas)
lista_imc_nome = []
lista_nome_imc = []
for nome in pessoas:
	peso =  float (input ('Digite o peso de{}: ' .format(nome)))
	altura =  float (input ('Digite a altura de {}: ' .format(nome)))
	valorimc = imc (peso, altura) 
	lista_imc_nome .append ((valorimc, nome))
	lista_nome_imc .append ((nome, valorimc))

print (sorted(lista_imc_nome)[1])
print (sorted(lista_imc_nome)[-2])

#terminar fazendo o {:.2f} e deixando mais organico