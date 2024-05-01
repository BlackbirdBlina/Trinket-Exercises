area_total = 0
for i in range(1, 5):
  largura_do_lote = float(input(str('Qual é a largura do lote ') + str(str(i) + str('?'))))
  comprimento_do_lote = float(input(str('Qual é o comprimento do lote ') + str(str(i) + str('?'))))
  area_cada_lote = largura_do_lote * comprimento_do_lote
  area_total = area_total + area_cada_lote
print(f'A área total do terreno é {area_total} m2')
