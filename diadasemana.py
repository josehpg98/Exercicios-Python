import calendar
ano = 2022
mes = 12
dia = 13
dia_semana = calendar.weekday(ano, mes, dia)
if dia_semana == 1:
    print('Segunda-feira')
elif dia_semana == 2:
    print('Terça-feira')
elif dia_semana == 3:
    print('Quarta-feira')
elif dia_semana == 4:
    print('Quinta-feira')
elif dia_semana == 5:
    print('Sexta-feira')
elif dia_semana == 6:
    print('Sabado')
else:
    print('Domingo')