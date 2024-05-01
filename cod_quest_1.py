distancia = float(input('Qual é a distância da viagem de ida e volta em quilômetros?'))
quilometro_por_litro = float(input('Quantos quilômetros o carro percorre com cada litro de combustível?'))
preco_por_litro = float(input('Qual é o preço em reais por litro de combustível?'))
preco_total = (distancia / quilometro_por_litro) * preco_por_litro
print(f'O valor em reais para realizar a viagem pretendida é {preco_total}')
