gatos = {'inglês': 'cat', 'espanhol': 'gato', 'francês': 'chat', 'alemão': 'katze', 'italiano': 'gatto'}

for item in sorted(gatos.items()):
	print (item)

for valor in sorted(gatos.value(), reverse=True):
	print (valor)

for item in sorted(gatos.keys()):
	if not item.endswith('ês'):
		print (gatos[item])

