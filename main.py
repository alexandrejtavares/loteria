import random

n1 = int(input('Digite a primeira dezena: '))
n2 = int(input('Digite a segunda dezena: '))
n3 = int(input('Digite a terceira dezena: '))
n4 = int(input('Digite a quarta dezena: '))
n5 = int(input('Digite a quinta dezena: '))
n6 = int(input('Digite a sexta dezena: '))

dezenas = set([n1, n2, n3, n4, n5, n6])

contador = 0

while True:
    # Incrementa o contador do sorteio
    contador += 1
    # Sorteia os 6 números e coloca no list sorteio
    sorteio = []
    while len(sorteio) < 6:
        # variável que vai receber o número sorteado
        num = random.randint(1, 60)
        # Se o número já existir no list sorteio, repete o sorteio até que o
        # número seja único
        while num in sorteio:
            num = random.randint(1, 60)
        # Armazena o número no list sorteio na posição correspondente
        sorteio.append(num)

    print(f"Sorteio nº: {contador}: {[x for x in sorteio]}")
    # Verifica se os números escolhidos são os sorteados.
    if dezenas == set(sorteio):
        break

print(f"Os números ganhadores foram {sorteio[0]}, {sorteio[1]}, {sorteio[2]}, {sorteio[3]}, {sorteio[4]}, {sorteio[5]}, que saíram no sorteio nº {contador}.")
