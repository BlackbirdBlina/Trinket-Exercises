salario_inicial = float(input(' Qual é o salário mensal inicial?'))
salario_com_aumento = salario_inicial * (5 / 100) + salario_inicial
valor_poupado = salario_com_aumento / 2
preco_automovel = float(input('Qual é o preço do automóvel a ser adquirido?'))
quantidade_meses = 0

valor_acumulado = 0
while valor_acumulado <= preco_automovel:
  quantidade_meses = quantidade_meses + 1
  valor_acumulado = valor_acumulado + valor_poupado
print(f'O funcionário terá que esperar {quantidade_meses} meses')
