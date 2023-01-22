print('''\033[31mAqui você irá conseguir calcular quantas ações e, 
qual o valor investido para receber sua renda mensal desejada\033[m''')
c = 0
while c != 5:
    rendamensal = float(input('Qual o valor da renda mensal? R$'))
    dividendyeld = float(input('Qual o Dividend Yeld dos últimos 12 meses? (xx.x) '))
    
