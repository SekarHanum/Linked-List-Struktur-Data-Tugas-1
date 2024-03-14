'''
This program was made by kelompok 1 Struktur Data UNESA to fulfill project from our teacher Mr. I Gde Agung Sri Sidhimantra S.Kom M.Kom

our member :
1. Sekar Hanum (148)
2. Regha Rahmadian Bintang (156)
3. Adip Setiaputra (158)

See more on our github
https://github.com/SekarHanum/Linked-List-Struktur-Data-Tugas-1

'''
#Data dari sebuah menu makanan (nama menu dan harganya)
class Node:
    def __init__(self,nama_menu,harga_menu,next=None):
        self.nama = nama_menu
        self.harga = harga_menu
        self.next = next
#Linked list yang digunakan untuk sebuah pesanan
class LinkedList:
    def __init__(self):
        self.head = None
    #Menambahkan menu
    def tambah_pesanan(self,nama_menu,harga_menu):
        add_pesanan = Node(nama_menu,harga_menu)
        if self.head is None:
            self.head = add_pesanan
            return
        
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = add_pesanan
    #Print data dalam list
    def print_menu(self):
        if self.head == None:
            print("Kosong")
        menu_makanan = self.head
        index = 1
        while menu_makanan:
            print(f"{index}.{menu_makanan.nama}\t\tRp{menu_makanan.harga}")
            menu_makanan = menu_makanan.next
            index += 1
    #Menghitung harga makanan dalam list
    def harga_total(self):
        menu_makanan = self.head
        harga = 0
        while menu_makanan:
            harga += menu_makanan.harga
            menu_makanan = menu_makanan.next
        # print(harga)
        return harga
#List dari menu yang ditawarkan
List_Menu = [["Miexue Ice Cream",5_000],["Boba Shake    ",16_000],["Mi Sundae     ",14_000],["Mi Ganas       ",11_000],["Creamy Mango Boba",22_000]]
System = LinkedList()

#Tampilan daftar menu yang tersedia beserta harganya
def daftar_menu():
    print("""
Berikut adalah menu andalan kami
Menu                    Harga
1. Miexue Ice Cream     Rp5000
2. Boba Shake           Rp16000
3. Mi Sundae            Rp14000
4. Mi Ganas             Rp11000
5. Creamy Manggo Boba   Rp22000

9.Tampilkan pesanan
0.Keluar
""")

#Fungsi yang digunkan untuk mengubah input user menjadi list pesanan
def pesan(input):
    System.tambah_pesanan(List_Menu[input-1][0],List_Menu[input-1][1])
#jumlah total pesanan yang di pesan (mulai dari 0)
jumlah_pesanan = 0
#variabel yang digunakan untuk menghentikan while setelah opsi checkout di jalankan
pengguna = True
#ucapan selamat datang kepada pengguna aplikasi Miexue
print("Selamat datang di Aplikasi Miexue")
#serangkaian program yang digunakan saat pengguna melakukan pemesanan
while pengguna:
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
