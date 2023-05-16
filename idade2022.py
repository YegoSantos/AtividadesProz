def calcIdade(nome):    
  try:
    anoNasc = int(input("Em qual ano você nasceu? Entre 1922 e 2021. \n"))
    if(anoNasc >= 1922 and anoNasc <= 2021):
      idade = 2022 - anoNasc
      print(nome, "sua idade é/será", idade)
  except:
    print("Ano de nascimento tem que ser entre 1922 e 2021")
    calcIdade(nome)

nome = input("Informe seu nome completo \n")
calcIdade(nome)    