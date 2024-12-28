import sys
import time
import os
import shutil


def waktu(detik):
    time.sleep(detik)
    os.system('cls' if os.name == 'nt' else 'clear')

def Simpan_Item_Kategori():
    Kategori_Produk = [
        "Skincare",
        "peralatan_rumah",
        "sparepart",
        "fashion",
        "Komputer_Dan_Aksesoris"
    ]
    return Kategori_Produk

def Tampilan_Kategori():
    Item_Kategori = Simpan_Item_Kategori()
    print("===================================================================")
    print("|-----------------------------------------------------------------|")
    print("|                 SELAMAT DATANG DI MARKOSHOP                     |")
    print("|-----------------------------------------------------------------|")
    print("===================================================================")
    print("|          NO          |           KATEGORI                       |")
    print("-------------------------------------------------------------------")
    for nomor, Item in enumerate(Item_Kategori, start=1):
        print("| \t  {:>2} \t       |      \t   {:<30} |".format(nomor, Item))
        if nomor == len(Item_Kategori) :
            print("-------------------------------------------------------------------")
            print("| \t  {:>2} \t       |      \t   {:<30} |".format(nomor + 1, "Keranjang"))
            print("| \t  {:>2} \t       |      \t   {:<30} |".format(nomor + 2, "Status Pembelanjaan"))
            print("| \t  {:>2} \t       |      \t   {:<30} |".format(nomor - nomor, "Keluar"))
            
    print("-------------------------------------------------------------------")
    return Item_Kategori

def Proses_Kategori():
    Item_Kategori = Simpan_Item_Kategori()
    Tampilan_Kategori()
    while True:
        try:
            input_kategori = input("Masukkan Kode Nomor Pilihan Kategori {0-7} (Ketik '0' Jika Ingin Ke halaman Login) : ")
            input_kategori = int(input_kategori)
            if 1 <= input_kategori <= len(Item_Kategori):
                nama_kategori = Item_Kategori[input_kategori - 1]
                
                Letak_path =   f"Produk_Pakaian/Produk_{nama_kategori}.py"
                if not os.path.exists(Letak_path):
                  shutil.copy("Home/Code_Default_Produk.py",(f"Produk_Pakaian/Produk_{nama_kategori}.py"))
                  waktu(3) 

                  print(f"File untuk kategori '{nama_kategori}' telah dibuat.")
                os.system(f"python Produk_Pakaian/Produk_{nama_kategori}.py")
                return nama_kategori
            elif input_kategori == len(Item_Kategori) + 1 :
                os.system("python Kantong_Belanja_User/Keranjang_user.py")
                
                waktu(3)
            elif input_kategori == len(Item_Kategori) + 2 :
                os.system("python Status_Pembelian_User/Status_Pembelian_User.py")
                
                waktu(3)
            elif input_kategori == 0 :
                print("Anda Dialihkan Ke Halaman Login")
                waktu(3)
                os.system("python Menu_Login/Login.py")
                break
                
                
            else:
                print("Kode Nomor Yang Anda Masukkan Tidak Valid !!!")
        except:
            print("Silakan masukkan angka yang valid.")
    
Proses_Kategori()

