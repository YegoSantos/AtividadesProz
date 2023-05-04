qtdRodas = int(input("Quantidade de Rodas? \n"))
peso= float(input("Quantidade de Quilogramas? \n"))
qtdPessoas= int(input("Quantidade de Pessoas no Veiculo? \n"))

if qtdRodas == 2 or qtdRodas == 3:
  print("A: Veiculos com duas ou três rodas")
elif qtdRodas == 4  and qtdPessoas <= 8 and peso <= 3500:
  print("B: Veículos com quatro rodas, que acomodam até oito pessoas e seu peso é de até 3500 kg;")
elif qtdRodas >= 4 and peso >= 3500 and peso <= 6000:
  print("C: Veículos com quatro rodas ou mais e com peso entre 3500 e 6000 kg;")
elif qtdRodas >= 4 and qtdPessoas > 8:
  print("D: Veículos com quatro rodas ou mais e que acomodam mais de oito pessoas")
else:
  print("E: Veículos com quatro rodas ou mais e com mais de 6000 kg.")