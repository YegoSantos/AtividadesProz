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
  print(result)
  return result

calculadora(2, 1, 4)

