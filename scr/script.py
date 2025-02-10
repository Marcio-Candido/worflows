arq = 'imagens/data.txt'
# lendo o arquivo
with open(arq,'r') as f
  numero = f.read()
numero = int(numero)
with open(arq,'w') as f
  print(numero+1,f)
