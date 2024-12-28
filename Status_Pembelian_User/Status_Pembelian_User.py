import os
import time
import json

def waktu(detik):
    time.sleep(detik)
    os.system('cls' if os.name == 'nt' else 'clear')

def baca_user_aktif():
    if os.path.exists('Menu_Login/user_active.json'):
        with open('Menu_Login/user_active.json', 'r') as file:
            try:
                data = json.load(file)
                return data["Username Yang Sedang Aktif"] if data else None
            except json.JSONDecodeError:
                print("Error: Format file user_active.json tidak valid.")
                return None
    return None
def tampilkan_informasi():
    username = baca_user_aktif()
    file_name = f"Status_Pembelian_User/Status_Pembelian_{username}.json"
    with open(file_name, 'r') as file :
        data = json.load(file)

    # Menampilkan informasi pembelian
    for pembeli in data:
        nomor = 0
        print("--------------------------------------------------------")
        print(f"            Status Pembelian Produk {pembeli['pembeli'].upper()}")
        print("--------------------------------------------------------")
        for item in pembeli['item']:
            print(f"  Nomor Resi          : {item['Nomor Resi']}")
            print(f"  Alamat              : {item['Alamat']}")
            print(f"  Jenis Pengiriman    : {item['Jenis Pengiriman']}")
            print(f"  Waktu Pembelian     : {item['Waktu Pembelian']}")
            print(f"  Produk              : {item['produk']}")
            print(f"  Jenis Produk        : {item['jenis produk']}")
            print(f"  Jumlah              : {item['jumlah']}")
            print(f"  Harga               : {item['harga']:,.0f}")
            print(f"  Total               : {item['total']:,.0f}")
            print(f"  Jenis Pembayaran    : {item['Jenis Pembayaran']}")
            print(f"  Status Pembayaran   : {item['Status Pembayaran']}")
            print(f"  Status Pengiriman   : {item.get('Status Pengiriman', 'Belum Diperbarui')}")  # Menampilkan status pengiriman
            print("--------------------------------------------------------")
def verifikasi_user():
    while True:
        try:
            keputusan_user = int(input("Silahkan Ketik '0' Jika Ingin Keluar : "))
            if keputusan_user == 0 :
                print("Anda Di Alihkan Halaman Utama")
                waktu(3)
                os.system("python Home/Home_Page.py")
            else :
                print("Maaf Nomor Tidak Valid")
                waktu(2)
                continue
        except ValueError:
            print("Silahkan Masukkan Nomor Sesuai Instruksi")
            waktu(2)
            continue
            
# Contoh penggunaan


  # Delay 2 detik sebelum menampilkan informasi
tampilkan_informasi()
verifikasi_user()
waktu(3)
