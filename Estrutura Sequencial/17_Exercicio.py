"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser
pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em
latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:

a) comprar apenas latas de 18 litros;
b) comprar apenas galões de 3,6 litros;
c) misturar latas e galões, de forma que o desperdício de tinta seja menor.
Acrescente 10% de folga e sempre arredonde os valores para cima,
isto é, considere latas cheias.

"""

tamanho_da_area = int(input('tamanho da área em metros:'))
litros = tamanho_da_area / 6
latas = litros / 18
preco_lata = 80
galoes = litros / 3.6
preco_galoes = 25
latas_e_galoes = ((litros / 18) + (latas / 3.6))
rendimento_lata = 6*18
rendimento_galao = 6*3.6

if latas < 1:
    print('Quantidade de latas a serem compradas:', round(latas + 0.5))
    print('Preço total:', 'R$', preco_lata)
else:
    if latas > 1:
        print('Quantidade de latas a serem compradas:', round(latas + 0.5))
        print('Preço total:', 'R$', round(latas + 0.5) * preco_lata)

if galoes < 1:
    print('Quantidade de galões a serem comprados:', round(galoes))
    print('Preço total:', 'R$', preco_galoes)
else:
    if galoes > 1:
        print('Quantidade de galoes a serem comprados:', round(galoes + 0.5))
        print('Preço total:', 'R$', round(galoes + 0.5) * preco_galoes)

if tamanho_da_area <= 100:
    print('Será mais viável escolher um dos valores acima')

else:
    if tamanho_da_area > 100:
        folga = tamanho_da_area * 1.1
        excedente = folga % rendimento_lata
        resultado_lata = round(folga/rendimento_lata - 0.5)
        resultado_galao = excedente / rendimento_galao
        print('quantidade de latas:', resultado_lata)
        if excedente > 0:
            print('quantidade de galões:', round(resultado_galao + 0.5))
        print('Preço total para latas e galões:', (resultado_lata*preco_lata)+(resultado_galao*preco_galoes))
