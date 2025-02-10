arq = 'imagens/data.txt'
# lendo o arquivo
with open(arq,'r') as f:
  numero = f.read()
  f.close()
numero = int(numero)
numero = numero + 1 
print(numero)
with open(arq,'w') as f:
  print(numero,f)
  f.close()
