daftar_menu()
    user_input = int(input("Silahkan Pesan :"))
    if user_input == 0:
        print("Terimakasih telah menggunakan Aplikasi Miexue")
        break
    elif  user_input in range(0,len(List_Menu)+1):
        while True:
            konfirmasi = int(input(f'Ingin menambahkan "{List_Menu[user_input-1][0]}" ke dalam pesanan?\n1. Ya\n0. Tidak\nSilahkan pilih :'))
            if konfirmasi == 1:
                pesan(user_input)
                print(f'Sukses Menambahkan "{(List_Menu[user_input-1][0])}" Kedalam pesanan')
                jumlah_pesanan += 1
                break
            elif konfirmasi == 0:
                break
            else:
                print("Error\nInput tidak valid")
    elif user_input == 9:
        if jumlah_pesanan < 1:
            while True:
                list_pesanan = int(input("Anda belum memiliki pesanan\n\n0. Kembali\nSilahkan pilih :"))
                if list_pesanan == 0:
                    break
                else:
                    print("Error\nInput tidak valid")
        else:
            while True:
                print("Pesanan Anda :\nMenu\t\t\t\tHarga")
                System.print_menu()
                print(f"Total Harga\t\t\t:Rp{System.harga_total()}")
                struk = int(input("\n1. Checkout pesanan\n0. Kembali\nSilahkan pilih :"))
                if struk == 0:
                    break
                elif struk == 1:
                    print("Pesanan anda sedang diproses\nTerimakasih telah menggunakan Aplikasi Miexue")
                    pengguna = False
                    break
                else:
                    print("Error\nInput tidak valid")
    else:
        print("Error\nInput tidak valid")
