def calculadora(num1, num2, op):
  if(op == 1):
    result = num1 + num2
  elif(op == 2):
    result = num1 - num2
  elif(op == 3):
    result = num1 * num2
  elif(op == 4):
    if(num2 == 0):
      print("O denominador não pode ser 0")
      return
    result = num1 / num2
  else:
    result = 0
  print("O resultado é:", result)
  return result


def printMenu():
  print("1 - Soma \n 2 - Subtração \n 3 - Multiplicação \n 4 - Divisão \n 0 - Sair")
  op = int(input())
  return op

def menu(op):
  while(op != 0):
    if(op != 0 and op != 1 and op != 2 and op != 3 and op != 4):
      print("Essa opção não existe")
      op = printMenu()
    else:
      print("Quais os valores a serem calculados?")
      num1 = int(input())
      num2 = int(input())
      calculadora(num1, num2, op)
      op = printMenu()

def init():
  op = printMenu()
  menu(op)

init()