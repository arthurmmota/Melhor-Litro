
def converteparaLitro(preco, ml):
    precoLitro = round(preco*1000/ml, 2)
    return precoLitro

listaCervejas = []

while True:
    entrada = input()
    if (entrada == 'z'):
        break
    entrada = entrada.split()
    print(entrada)

    dictPreco_ml = dict(cerveja = entrada[0], preco = float(entrada[1]), ml = float(entrada[2]), precoLitro = 0 )
    dictPreco_ml['precoLitro'] = converteparaLitro(dictPreco_ml['preco'],dictPreco_ml['ml'])

    listaCervejas.append(dictPreco_ml)
    listaCervejas = sorted(listaCervejas, key=lambda x: x['precoLitro']).copy()

    #listaCervejas2 = sorted(listaCervejas, key=lambda x: x['precoLitro'])

    for dicio in listaCervejas:

        print('*** CERVEJA ', dicio['cerveja'], ' ------ R$%.2f' % dicio['precoLitro'], ' / L ***' )


for item in listaCervejas:
    print(item)