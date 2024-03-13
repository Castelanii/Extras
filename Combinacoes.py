#Esse codigo propõe verificar o maior numero de uma lista e falar se existe alguma combinação de elementos da própia lista que a soma resulte no maior elemento
def combinacoes(array, x):
  # Função para gerar combinações de tamanho r a partir da sequência
  def helper(inicio, elementos):
      if len(elementos) == x:
          result.append(elementos.copy())
          #volta para o for i in range assim que a lista elementos atinge o tamanho necessário
          return


      for i in range(inicio, len(array)):
        #note que toda vez que voltarmos para cá após o return acima, a lista elementos volta 
        #sem o ultimo valor atribuido anteriormente, porém o indice i continua subindo, ou seja
        #ele vai mudar o ultimo valor da lista elementos, toda vez que voltarmos com return, 
        #até chegar ao ultimo elemento de array
          helper(i + 1, elementos + [array[i]])

  result = []
  helper(0, [])
  return result

def ArrayChallenge(arr):
arr.sort()
maior = arr.pop()
#for para gerar todos os tamnhanhos de combinaçoes possiveis, exemplo se len(arr) é 4, 
#vai gerar as combinaçoes 2x2 e 3x3 e 4x4
for i in range(2, len(arr) + 1):
  comb = combinacoes(arr, i)
  #for para verificar cada combinação para ver se a soma de seus elementos resulta no maior numero
  for i in comb:     
    if sum(i) == maior:
      return "true"


# code goes here
return "false"
