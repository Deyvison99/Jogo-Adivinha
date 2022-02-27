from random import randint  # comando aleatorio
from time import sleep  # Da um atraso
print('*' * 20)
print('* JOGO DE ADIVINHA *')
print('*' * 20)
print()
while True:
    computador = randint(0, 5)  # Faz o computador 'Pensar'
    print('\033[1;32m-=-' * 20)
    print('\033[1;32mVou penssar em um número entre 0 e 5. Tenta adivinhar...')
    print('\033[1;32m-=-' * 20)
    print()
    jogador = int(input('\033[1;33mEm que número eu pensei?'))  # Jogador tenta adivinhar
    print()
    print('\033[1;32mPROCESSANDO...')

    sleep(2)

    print()
    if jogador == computador:
        print('\033[1;32mPARABÉNS! Você conseguiu me vencer!')
        break
    else:
        print(f'\033[1;31mGANHEI! Eu pensei no número {computador} e não {jogador}')
