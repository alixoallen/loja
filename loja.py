print('--------------'*5)
print('         loja barata                ')
total=0
mil=0
menor=0
nome=0
while True:
    produto=str(input('nome do produto : '))
    preço=int(input('preço: R$'))
    resp=str(input('quer continuar ? [S/N] ')).strip().upper()[0]
    total+=preço
    if preço>=1000:
        mil+=1
    if menor == 0:
        menor = preço
        nome = produto
    elif preço < menor:
        menor = preço
        nome = produto
    while resp not in 'SN':
      resp=str(input('quer continuar ? [S/N] ')).strip().upper()[0] 
    if resp=='N':
        print('-----------------fim do programa----------------------------')
        print(f'o total da compra foi de R${total}')
        print(f'temos {mil} produtos custando mais de R$1000.00')
        print(f'o produto mais barato foi {nome} que custa {menor}')
        break
