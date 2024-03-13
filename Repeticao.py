#Esse codigo propõe achar a palavra com mais letras repetidas dentro de uma string, caso ajam palavras com mesmo numero de letras repetidas, a saida será a primeira delas
def SearchingChallenge(strParam):
  palavras = strParam.split()

  palavra = ""
  maior = 0
  for i in palavras:
    contagem={}
    for letras in i:
      contagem[letras]= contagem.get(letras,0)+1
      if contagem[letras] > maior:
        maior = contagem[letras]
        palavra = i

  if maior == 1:
    return "-1"

  # code goes here
  return palavra

# keep this function call here 
print(SearchingChallenge(input()))
