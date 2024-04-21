# Código de exemplo para condições if
x = 10
if x > 5:
  print("x é maior que 5")
elif x == 5:
  print("x é igual a 5")
else:
  print("x é menor que 5")


# Código de exemplo para "switch case" usando dicionário
def case_one():
  return "Executando caso um"


def case_two():
  return "Executando caso dois"


def case_three():
  return "Executando caso três"


switch_case = {1: case_one(), 2: case_two(), 3: case_three()}

case_number = 2
print(switch_case.get(case_number, "Caso padrão, nenhum caso correspondente"))
