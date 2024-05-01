valor_das_multas = float(input('Qual é o valor original cobrado por cada multa?')) * 2
juros_cobrado_detran = float(input('Qual é a porcentagem de juros cobrada pelo Detran?'))
quantidade_amigos_contribuem = float(input('Quantos amigos irão contribuir com as despesas?'))
valor_com_juros = valor_das_multas * (juros_cobrado_detran / 100) + valor_das_multas
valor_que_cada_amigo_paga = valor_com_juros / quantidade_amigos_contribuem
print(f'O valor em reais que cada amigo deverá pagar ao Detran é {valor_que_cada_amigo_paga}')
