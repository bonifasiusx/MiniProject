# Mini Project: KALKULATOR RUNGKAD

from time import sleep

def kalkulator():
    menu_utama = ['Tambah  (+)', 'Kurang  (-)', 'Bagi    (/)', 'Kali    (*)']

    while True:
        title = '== KALKULATOR RUNGKAD =='
        symbol = '=' * (len(title))
        print(f'\n{symbol}\n{title}\n{symbol}\n')

        for i in range(len(menu_utama)):
            print(str(i+1) + '. ' + menu_utama[i])

        print('0. Exit   (END)')
        user_input_str = input('\nPilih Menu: ')

        if (not user_input_str.isdigit()) or (int(user_input_str) > 4):
            print('\nPilihan tidak ditemukan!\nCoba lagi ya bro.\n')
            continue
        
        user_input = int(user_input_str)
        
        if user_input == 0:
            exit_text = 'PROGRAM ENDING IN'
            exit_symbol = '=' * (len(exit_text))
            print(f'\n{exit_symbol}')
            print(exit_text)
            sleep(0.5)
            print('3...')
            sleep(0.5)
            print('2...')
            sleep(0.5)
            print('1...')
            sleep(0.5)
            print(exit_symbol)
            print('\nSEE YOU BRO!\n')
            break
        
        angka1_str = input("Masukkan angka pertama: ")
        angka2_str = input("Masukkan angka kedua: ")

        if not angka1_str.isdigit() or not angka2_str.isdigit():
            print('\nPake angka lah der...')
            continue

        angka1 = int(angka1_str)
        angka2 = int(angka2_str)

        if user_input == 1:
            print('\nHasil: ' + str(angka1 + angka2))

        elif user_input == 2:
            print('\nHasil: ' + str(angka1 - angka2))

        elif user_input == 3:
            if angka2 == 0:
                print('\nWah ini pelanggaran ini...')
                print('Coba lagi yak!')
            else:
                print('\nHasil: ' + str(angka1 / angka2))

        elif user_input == 4:
            if angka1 == 0 or angka2 == 0:
                print('\nBerapa yak kira-kira🤡')
            else:
                print('\nHasil: ' + str(angka1 * angka2))

        else:
            print('\nInvalid Input Brader')
            print('Pilih menu yang bener lah kocak\n')
            
kalkulator()