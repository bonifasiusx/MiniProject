# ==================  MAIN PROGRAM  ================== # 

from head import welcome
from game_gacha import game
from kalkulator import kalkulator
from list_tugas import list_tugas
from exit import exit_program


# FUNCTION MENU UTAMA #
def main_menu():
    menu = ['GAME GACHA', 'KALKULATOR', 'TUGAS']
    while True:
        for i in range(len(menu)):
            print(str(i + 1) + '. ' + menu[i])
        
        # EXIT MENU
        print('0. EXIT PROGRAM')
            
        user_input_str = input('\nSilahkan Pilih Menu: ')

        if not user_input_str.isdigit():
            print('\nPilihan tidak dikenali, silahkan ulangi.\n')

        user_input = int(user_input_str)
        if user_input == 1:
            game()
            return main_menu()
        elif user_input == 2:
            kalkulator()
            return main_menu()
        elif user_input == 3:
            list_tugas()
            return main_menu()
        elif user_input == 0:
            exit_program()
            break
        else:
            input('\nPilihan tidak dikenali, silahkan pilih menu yang tersedia: ')
            return main_menu()
    
        
def app():        
    welcome()
    main_menu()
app()