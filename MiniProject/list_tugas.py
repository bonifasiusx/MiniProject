# Mini-Project: To-Do List CLI (Command Line Interface)

from time import sleep

def list_tugas():
# BACA FILE SAAT PROGRAM DIMULAI
    try:
        with open('tugas.txt', 'r') as file:
            tugas = [baris.strip() for baris in file.readlines()]
    except FileNotFoundError:
        tugas = []

    print('\nSELAMAT DATANG DI LIST TUGAS RUNGKAD!\n')
    print('[1] Lihat Tugas Terkini')
    print('[2] Tambah Tugas Baru')
    print('[3] Tandai Tugas Selesai')
    print('[0] Keluar')

    while True:
        user_input_str = input('\nSilahkan Pilih Menu: ')
        
        if not user_input_str.isdigit():
            print('\nMohon pilih menu yang tersedia.')
            continue
        
        user_input = int(user_input_str)

        if user_input == 1:
            if not tugas:
                print('Belum ada tugas. Yuk tambah dulu!\n')
            else:
                for i in range(len(tugas)):
                    print(str(i+1) + '. ' + tugas[i])

        elif user_input == 2:
            tugas_baru = input("Masukkan tugas baru: ")
            tugas.append(tugas_baru)
            with open('tugas.txt', 'w') as file:
                for t in tugas:
                    file.write(t + '\n')
            print(f"\nTugas '{tugas_baru}' telah ditambahkan!")

        elif user_input == 3:
            if not tugas:
                print('Belum ada tugas. Yuk tambah dulu!\n')
            else:
                print('Tugas Tersedia: ')
                for i in range(len(tugas)):
                    print(str(i+1) + '. ' + tugas[i])

                nomor = input('\nPilih nomor tugas yang selesai: ')
                if nomor.isdigit():
                    nomor = int(nomor)
                    if 1 <= nomor <= len(tugas):
                        nama_tugas = tugas[nomor - 1]
                        del tugas[nomor - 1]
                        with open('tugas.txt', 'w') as file:
                            for t in tugas:
                                file.write(t + '\n')
                        print(f"\nTugas '{nama_tugas}' sudah diselesaikan!")
                    else:
                        print('Tugas tidak ditemukan!')
                else:
                    print('Input harus angka ya, bro!')

        elif user_input == 0:
            print('\nExiting List Tugas in')
            sleep(0.5)
            print('3...')
            sleep(0.5)
            print('2...')
            sleep(0.5)
            print('1...')
            sleep(0.5)
            print('\nSee you bro!\n')
            break

        else:
            print('\nPilihan tidak dikenali! Mohon pilih menu yang tersedia.')
            continue