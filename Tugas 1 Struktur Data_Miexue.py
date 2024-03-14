'''
This program was made by kelompok 1 Struktur Data UNESA to fulfill project from our teacher Mr. I Gde Agung Sri Sidhimantra S.Kom M.Kom

our member :
1. Sekar Hanum ()
2. Adip Setyaputra ()
3. Regha Rahmadian Bintang (156)

See more on our github
[githublink]

    NOTE IKI ISIEN REK!!!
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
