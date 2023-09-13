
#1

def e_primo(num):
  for div in range(2,num):
    if num % div==0:
      print(f"o {num} não é primo e é divisivel por {div} ")
    
  else:
    print ( "é primo")



e_primo(20)
#2

def calcular_juros(valor_divida, parcelas):
    if parcelas == 1:
        return 0.0
    if parcelas == 3:
        return valor_divida * 0.10
    if parcelas == 6:
        return valor_divida * 0.15
    if parcelas == 9:
        return valor_divida * 0.20
    if parcelas == 12:
        return valor_divida * 0.25
    else:
        return None


def calcular_valor_total(valor_divida, juros):
    return valor_divida + juros

def mostrar_opcoes_parcelamento(valor_divida):
    print("Opções de Parcelamento:")

    print(f"Parcelas: 1 | Juros: R$ 0 | Total: R${valor_divida:} | Valor da Parcela: R${valor_divida}")
    
    for parcela in range(3,13,3):
      juros = calcular_juros(valor_divida, parcela)
      valor_total = calcular_valor_total(valor_divida, juros)
      valor_parcela = valor_total / parcela
      print(f"Parcelas: {parcela} | Juros: R${juros:} | Total: R${valor_total:} | Valor da Parcela: R${valor_parcela:}")
    
    
    

valor_divida = float(input("Digite o valor da dívida: "))


mostrar_opcoes_parcelamento(valor_divida)



#3

intervalo0_25=0
intervalo26_50=0
intervalo51_75=0
intervalo76_100=0
while True:
  a = int(input(" Digite um valor,caso for negativo o sistema terminará : "))
  if a<0:
    break
  if 0 <= a <= 25 :
    intervalo0_25 +=1
  elif 26 <= a <= 50:
    intervalo26_50 +=1
  elif 51 <= a <= 75:
    intervalo51_75 +=1
  elif 76 <= a <= 100:
    intervalo76_100 +=1
  


print ("[0-25]: ",intervalo0_25)
print ("[26-50]: ",intervalo26_50 )
print ("[51-75]: ",intervalo51_75)
print ("[76-100]: ",intervalo76_100 )



  