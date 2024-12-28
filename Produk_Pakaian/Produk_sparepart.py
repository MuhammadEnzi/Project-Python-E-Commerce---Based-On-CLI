import os
import time
import sys
import json
import random
import string
from datetime import datetime
import threading
def opsi_pengiriman():
    while True:
        print("------Opsi Pengiriman------")
        print("1. J&T Express")
        print("2. JNE Reguler")
        print("3. SICepat Reguler")
        print("4. Ninja Xpress")
        print("5. SPX Standart")
        print("---------------------------")
        opsi_pengiriman_user = input("Silahkan Masukkan Jenis Pengiriman : ")
        opsi_pengiriman_user = int(opsi_pengiriman_user)
        if opsi_pengiriman_user == 1:
            data_pengiriman = "J&T Express"
        elif opsi_pengiriman_user == 2:
            data_pengiriman = "JNE Reguler"
        elif opsi_pengiriman_user ==3 :
            data_pengiriman = "SICepat Reguler"
        elif opsi_pengiriman_user == 4:
            data_pengiriman = "Ninja Xpress"
        elif opsi_pengiriman_user == 5:
            data_pengiriman = "SPX Standart"
        else :
            print("Maaf Nomor Tidak Valid, Silahkan Coba Lagi")
            continue
        return data_pengiriman
    
def alamat_user():
    return input("Silahkan Masukkan Alamat Tujuan Produk ( 'Secara Detail' ) : ")
def update_status_pengiriman(item_belanja):
    time.sleep(5 * 60)  # Tunggu 5 menit
    item_belanja["Status Pengiriman"] = "Produk sedang dalam perjalanan"
    save_status_to_file(item_belanja)

    time.sleep(10 * 60)  # Tunggu 10 menit
    item_belanja["Status Pengiriman"] = "Produk telah sampai di tujuan"
    save_status_to_file(item_belanja)
def save_status_to_file(item_belanja):
    username = baca_user_aktif()
    file_path = f"Status_Pembelian_User/Status_Pembelian_{username}.json"
    
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            kantong_belanja = json.load(file)
            for item in kantong_belanja:
                if item["pembeli"] == username:
                    for menu in item.get("item", []):
                        if menu["Nomor Resi"] == item_belanja["Nomor Resi"]:
                            menu["Status Pengiriman"] = item_belanja["Status Pengiriman"]
                            break
                    else:
                        item["item"].append(item_belanja)
                    break
                       
            else:
                kantong_belanja.append({
                    "pembeli": username,
                    "item": [item_belanja]
                })
    else:
        kantong_belanja = [{
            "pembeli": username,
            "item": [item_belanja]
        }]

    with open(file_path, "w") as file:
        json.dump(kantong_belanja, file, indent=3)
def proses_pembayaran_user(jenis_pembayaran):
            if jenis_pembayaran == 1:
                return "COD"
            if jenis_pembayaran == 2:
                while True:
                    jenis_bank = input("Silahkan Masukkan Jenis Bank ( 'BCA' / 'BNI' / ' BRI' / 'BSI' ) :")
                    if jenis_bank in ["BCA", "BNI", "BRI", "BSI"]:
                        return "Transfer" + " " + jenis_bank
                    else:
                        print("Maaf, Jenis Bank Tidak Valid")
def waktu(detik):
    time.sleep(detik)
    os.system('cls' if os.name == 'nt' else 'clear')
def generate_Nomor_Pesanan(length=14):
    karakter_nomor_Pesanan = string.ascii_uppercase + string.digits
    return ''.join(random.choice(karakter_nomor_Pesanan) for _ in range(length))

def baca_user_aktif():
    if os.path.exists('Menu_Login/user_active.json'):
        with open('Menu_Login/user_active.json', 'r') as file:
            data = json.load(file)
            return data["Username Yang Sedang Aktif"] if data else None
    return None

def simpan_ke_kantong_belanja(produk,jenis_produk, jumlah, harga,total_harga):
    username = baca_user_aktif()

    file_path = f"Kantong_Belanja_User/kantong_belanja_{username}.json"
    
    # Buat data item belanja
    item_belanja = {
        "produk": produk,
        "jenis produk": jenis_produk,
        "jumlah": jumlah,
        "harga": harga,
        "total": total_harga
    }

    # Cek apakah file sudah ada
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            kantong_belanja = json.load(file)  # Membaca data lama
            
            for item in kantong_belanja:
                if item["pembeli"] == username:
                    # Tambahkan item_belanja ke dalam list item yang ada
                    if "item" not in item or not isinstance(item["item"], list):
                        item["item"] = []  # Inisialisasi sebagai list jika belum ada
                    item["item"].append(item_belanja)  # Menambahkan item belanja baru
                    break

            else:
                # Jika username belum ada, buat entri baru
                kantong_belanja.append({
                "pembeli": username,
                "item": item_belanja
            }) 
    else:
        kantong_belanja = [{
        "pembeli": username,
        "item": [item_belanja]  # Buat list baru untuk item belanja
        }]

    # Tambahkan informasi pembeli dan item belanja ke kantong belanja

    # Simpan kembali ke file
    with open(file_path, "w") as file:
        json.dump(kantong_belanja, file, indent=3)
def status_pembelian_user(produk, jenis_produk, jumlah, harga,alamat, pengirima,jenis_pembayaran,status_pembayaran):
    username = baca_user_aktif()
    nomor_resi = generate_Nomor_Pesanan()
    waktu_terbaru = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    file_path = f"Status_Pembelian_User/Status_Pembelian_{username}.json"
    status_pengiriman = "Produk sedang dikemas penjual"
    item_belanja = {
        "Nomor Resi": nomor_resi,
        "Waktu Pembelian": waktu_terbaru,
        "Alamat" :alamat,
        "Jenis Pengiriman" :pengirima,
        "produk": produk,
        "jenis produk": jenis_produk,
        "jumlah": jumlah,
        "harga": harga,
        "total": (jumlah * harga),
        "Jenis Pembayaran": jenis_pembayaran,
        "Status Pembayaran": status_pembayaran,
        "Status Pengiriman" : status_pengiriman
    }
    threading.Thread(target=update_status_pengiriman,args=(item_belanja,)).start()


    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            kantong_belanja = json.load(file)
            for item in kantong_belanja:
                if item["pembeli"] == username:
                    if "item" not in item or not isinstance(item["item"], list):
                        item["item"] = []
                    item["item"].append(item_belanja)
                    break
            else:
                kantong_belanja.append({
                    "pembeli": username,
                    "item": [item_belanja]
                })
    else:
        kantong_belanja = [{
            "pembeli": username,
            "item": [item_belanja]
        }]

    with open(file_path, "w") as file:
        json.dump(kantong_belanja, file, indent=3)


# Jenis Item Pakaian
def Penyimpanan_Item_Produk():
    Item_Produk = {
        # Nama Produk
        "Velg": [
            #              Jenis Item             Harga
            {"Nama_Item": "VND", "Harga": 1800000},
            {"Nama_Item": "Vrossi", "Harga": 1000000},
            {"Nama_Item": "KTC", "Harga": 2200000},
        ],
        "Knalpot": [
            {"Nama_Item": "TZM", "Harga": 600000},
            {"Nama_Item": "WRC", "Harga": 800000},
            {"Nama_Item": "ARM", "Harga": 1000000},
        ],
        "Handle rem" : [
            {"Nama_Item": "RCB", "Harga": 350000},
            {"Nama_Item": "TAD", "Harga": 300000},
            {"Nama_Item": "BREMBO", "Harga": 400000},
        ],
        "Kaliper" : [
            {"Nama_Item": "NISSIN", "Harga": 650000},
            {"Nama_Item": "TZM", "Harga": 600000},
            {"Nama_Item": "TAD", "Harga": 250000},
        ],
        "Shock" : [
            {"Nama_Item": "Ohlins", "Harga": 8000000},
            {"Nama_Item": "DBS", "Harga": 200000},
            {"Nama_Item": "KTC", "Harga": 800000},
        ],
        "Knalpot" : [
            {"Nama_Item": "TZM", "Harga": 600000},
            {"Nama_Item": "WRC", "Harga": 800000},
            {"Nama_Item": "ARM", "Harga": 1000000},
        ],
        "Handle rem" : [
            {"Nama_Item": "RCB", "Harga": 350000},
            {"Nama_Item": "TAD", "Harga": 300000},
            {"Nama_Item": "BREMBO", "Harga": 400000},
        ],
        "Kaliper" : [
            {"Nama_Item": "NISSIN", "Harga": 650000},
            {"Nama_Item": "TZM", "Harga": 600000},
            {"Nama_Item": "TAD", "Harga": 250000},
        ],
        "Shock" : [
            {"Nama_Item": "Ohlins", "Harga": 8000000},
            {"Nama_Item": "DBS", "Harga": 200000},
            {"Nama_Item": "KTC", "Harga": 800000},
        ],
    }
    return Item_Produk

def Tampilan_Kategori():
    Item_Kategori = Penyimpanan_Item_Produk()
    print("========================================================================================================================================")
    print("|--------------------------------------------------------------------------------------------------------------------------------------|")
    print("|                                                         KATEGORI PAKAIAN                                                             |")
    print("|--------------------------------------------------------------------------------------------------------------------------------------|")
    print("========================================================================================================================================")
    print("|          NO          |           PRODUK                         |           JENIS PRODUK                   |          HARGA          |")
    print("----------------------------------------------------------------------------------------------------------------------------------------")
    
    nomor = 1
    for jenis_Produk, detail_item_produk in Item_Kategori.items():
        
        print(f"|    \t   {nomor:<2} \t       | \t   {jenis_Produk:<30} | {' '*40} | {' '*23} |")
        for item in detail_item_produk:
            item["Harga"] = f"{item["Harga"]:,.0f}"
            print(f"|{' ' * 22}|{' ' * 41} |{' ' *10} {item['Nama_Item']:<30} | {' ' *9}Rp.{item['Harga']:<10}  |")
        nomor += 1
        print("----------------------------------------------------------------------------------------------------------------------------------------")


def Pembelian_Produk():
    Item_Kategori = Penyimpanan_Item_Produk()

    
    while True :
        Tampilan_Kategori()
        nomor_kategori = len(Item_Kategori)
        kategori_pilihan = input(f"Masukkan nomor kategori yang ingin dibeli (1-{nomor_kategori}): ")
        kategori_pilihan = int(kategori_pilihan)
        if kategori_pilihan == 0 :
            print("Anda Di Alihkan Halaman Utama")
            os.system("python Home/Home_Page.py")
            sys.exit()
        try:
            kategori_pilihan = int(kategori_pilihan) - 1  # Mengubah ke indeks
            if kategori_pilihan < 0 or kategori_pilihan >= len(Item_Kategori):
                print("Nomor kategori tidak valid.")
                continue
        except ValueError:
            print("Input tidak valid. Harap masukkan nomor yang benar.")
            continue

        jenis_produk = list(Item_Kategori.keys())[kategori_pilihan]

        print(f"\nAnda memilih kategori: {jenis_produk}")
        print("Produk yang tersedia:")

        for urutan, item in enumerate(Item_Kategori[jenis_produk]):
            
            print(f"{urutan + 1}. {item['Nama_Item']} - Rp.{item['Harga']:,.0f}")
        while True :
            produk_pilihan = input("Masukkan nomor produk yang ingin dibeli: ")
            try:
                produk_pilihan = int(produk_pilihan) - 1  # Mengubah ke indeks
                if produk_pilihan < 0 or produk_pilihan >= len(Item_Kategori[jenis_produk]):
                    print("Nomor produk tidak valid.")
                    continue
            except ValueError:
                print("Input tidak valid. Harap masukkan nomor yang benar.")
                continue

            while True:
                jumlah = input("Masukkan jumlah yang ingin dibeli: ")
                try:
                    jumlah = int(jumlah)
                    if jumlah <= 0:
                        print("Jumlah harus lebih dari 0.")
                        continue
                except ValueError:
                    print("Input tidak valid. Harap masukkan jumlah yang benar.")
                    continue

        
                produk_terpilih = Item_Kategori[jenis_produk][produk_pilihan]
                total_harga = produk_terpilih['Harga'] * jumlah

                print(f"\nAnda telah membeli {jumlah} {produk_terpilih['Nama_Item']} dari kategori {jenis_produk}.")
                print(f"Total harga: Rp.{total_harga:,.0f}")
                
                while True:
                    try:
                        keputusan_user = input("Ingin Melakukan Pembayaran Atau Memasukkan Ke Keranjang ( 1.Bayar / 2.Tambah Keranjang ) : ")
                        keputusan_user = int(keputusan_user)
                        if keputusan_user == 1:
                            print(f"Total Pembelian Harga Produk Anda Rp.{total_harga:,.0f}")
                            while True:
                                alamat = alamat_user()
                                pengiriman = opsi_pengiriman()
                                jenis_pembayaran = input("Silahkan Masukkan Metode Pembayaran ( '1. COD' / ' 2. Transfer Bank' ) : ")
                                jenis_pembayaran = int(jenis_pembayaran)
                                status_pengiriman = "Produk sedang dikemas penjual"
                                user_bayar = proses_pembayaran_user(jenis_pembayaran)
                                
                                try: 
                                    if jenis_pembayaran == 1:
                                        status_pembayaran = "Belum Lunas"
                                        status_pengiriman = "Produk sedang dikemas penjual"
                                        
                                    elif jenis_pembayaran == 2:
                                
                                        pembayaran_user = input("Silahkan Masukkan Nominal Pembayaran Sesuai Yang Tertera : Rp.")
                                        pembayaran_user = int(pembayaran_user)
                                        if pembayaran_user < total_harga:
                                            print("Nominal Pembayaran Anda Kurang")
                                            continue
                                        else:
                                            kembalian = pembayaran_user - total_harga
                                            print(f"Uang Kembalian Anda Rp.{kembalian:,.0f}")
                                            waktu(5)
                                            print("Pembelian Berhasil.... ")
                                            print("Terima Kasih.....")
                                            status_pembayaran = "Lunas"

                                        
                                       # Keluar dari fungsi setelah pembayaran berhasil
                                except ValueError:
                                    print("Silahkan Masukkan Nominal Uang Berupa Angka")
                                    continue
                                status_pembelian_user(jenis_produk,produk_terpilih['Nama_Item'], jumlah, total_harga,alamat,pengiriman,user_bayar,status_pembayaran)
                                while True:
                                    try:
                                        kondisi_user = input('Ingin Menambahkan Item Lagi ? Jika Ya Ketik "Ya" Jika Tidak Ketik "No" : ')
                                        if kondisi_user.lower() == "ya" :
                                            waktu(2)
                                            break
                                    
                                        elif kondisi_user.lower() == "no" :
                                            waktu(1)
                                            print("Anda Akan Dialihkan Ke Halaman Utama !!!")
                                            waktu(3)
                                            os.system("python Home/Home_Page.py")
                                            waktu(2)
                                            break
                                        else:
                                            print("Maaf, Kode Yang Anda Masukkan Tidak Sesuai")
                                    except:
                                        print("Maaf, Kode Yang Anda Masukkan Tidak Sesuai")
                                break
                            break
                                
                                
                            

                        elif keputusan_user == 2:
                            simpan_ke_kantong_belanja(jenis_produk,produk_terpilih['Nama_Item'], jumlah,produk_terpilih['Harga'], total_harga)
                            waktu(2)
                            print(f"{jumlah} {produk_terpilih['Nama_Item']} telah ditambahkan ke kantong belanja.")
                            waktu(2)
                            while True:
                                try:
                                    kondisi_user = input('Ingin Menambahkan Item Lagi ? Jika Ya Ketik "Ya" Jika Tidak Ketik "No" : ')
                                    if kondisi_user.lower() == "ya" :
                                        waktu(2)
                                        break
                                
                                    elif kondisi_user.lower() == "no" :
                                        waktu(1)
                                        print("Anda Akan Dialihkan Ke Halaman Utama !!!")
                                        waktu(3)
                                        os.system("python Home/Home_Page.py")
                                        waktu(2)
                                        break
                                    else:
                                        print("Maaf, Kode Yang Anda Masukkan Tidak Sesuai")
                                except:
                                    print("Maaf, Kode Yang Anda Masukkan Tidak Sesuai")
                            break


                            

                        else:
                            print("Maaf Nomor Yang Anda Masukkan Tidak Valid, Silahkan Coba Lagi....")
                            continue
                            
                    except ValueError:
                        print("Input tidak valid. Harap masukkan nomor yang benar.")
                break
            break
            
Pembelian_Produk()             