def  imc (peso, altura):
	return  (peso / (altura ** 2) )	

peso =  float (input ('Digite seu peso: '))
altura =  float (input ('Digite sua altura: '))
valorimc = (imc(peso, altura))

print ('Seu imc é: {:.2f}' .format(valorimc))

