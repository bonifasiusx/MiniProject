# MENU UTAMA

def welcome():
    print('\nINITIATING PROGRAM...\n')
    nama_user = input('PLEASE ENTER YOUR NAME: ')
    
    title = (f'== HAI {nama_user.upper()} SELAMAT DATANG DI LAPAK RUNGKAD ==')
    symbol = '=' * len(title)
    
    print(f'\n{symbol}')
    print(title)
    print(f'{symbol}\n')
    
        