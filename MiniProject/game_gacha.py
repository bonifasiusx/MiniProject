# GAME GACHA ANGKA ACAK 1-10 (USER VS KOMPUTER)

import random
from time import sleep

def game():
    while True:
        angka_user = input('\nSilahkan pilih nomer acak dari 1-10! \n')
        
        if (not angka_user.isdigit()) or not (1 <= int(angka_user) <= 10):
            print('Invalid input bro! \nPilih nomer 1-10 ya.')
            continue

        angka_user = int(angka_user)
        nomer_gacha = random.randint(1, 10)
        
        if angka_user == nomer_gacha:
            print(f'\nSELAMAT KAMU MENANG 🏆\nKomputer juga gacha di nomer {nomer_gacha}!')
        else:
            print(f'\nYAH KAMU KALAH 😔 \n\nKamu pilih nomer {angka_user}. \nSedangkan GACHA RUNGKAD adalah {nomer_gacha}.')
        
        coba_lagi = input('\nMau coba lagi? [Y/N]: ')
        if coba_lagi == 'y' or coba_lagi == 'Y':
            continue
        else:
            print('\nNICE TRY BRO! \nTerimakasih telah bertanding di GACHA RUNGKAD.\n')
            sleep(0.5)
            print('CLOSING GACHA RUNGKAD')
            sleep(0.5)
            print('...')
            sleep(0.5)
            print('...')
            sleep(0.5)
            print('...\n')
            sleep(0.5)
            print('ADIOS BRADER\n')
            sleep(0.5)
            break