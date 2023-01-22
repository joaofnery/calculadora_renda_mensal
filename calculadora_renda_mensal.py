print('''\033[32mAqui você irá conseguir calcular quantas ações e, 
qual o valor investido para receber sua renda mensal desejada\033[m''')
c = 0
while c != 3:
    rendamensal = float(input('Qual o valor da renda mensal? R$'))
    dividendyeld = float(input('Qual o Dividend Yeld dos últimos 12 meses? (xx.x) '))
    yeldm = (1 + (dividendyeld / 100)) ** (1 / 12) - 1
    valorinvest = rendamensal / yeldm

    print('Deseja informar o preço de alguma ação/FII para saber a quantidade de cotas necessárias?')
    c = int(input('''   
                        [1] SIM
                        [2] NÃO
                        [3] Finalizar programa
                        [1][2][3]: '''))
    if c == 1:
        preco = float(input('Qual o preço do ativo? R$'))
        cotas = valorinvest // preco
    elif c == 2 or c == 3:
        preco = 0
        cotas = 0

    print('x-'*20)
    print('''
        RENDA MENSAL    = R${:.2f}
        DY              = {}
        VALOR INVESTIDO = R${:.2f}
        PREÇO/COTA      = R${:.2f}
        QTD COTAS       = {}'''.format(rendamensal, dividendyeld, valorinvest, preco, cotas))
    print('x-' * 20)
print('Muito Obrigado! Programa finalizado. ')

