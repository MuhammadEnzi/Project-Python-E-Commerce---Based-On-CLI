import os
import time
import json
import string
import random
from datetime import datetime
import threading
import os
import json
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
                    if jenis_bank.upper() in ["BCA", "BNI", "BRI", "BSI"]:
                        return "Transfer" + " " + jenis_bank.upper()
                    else:
                        print("Maaf, Jenis Bank Tidak Valid")

def generate_Nomor_Pesanan(length=14):
    karakter_nomor_Pesanan = string.ascii_uppercase + string.digits
    return ''.join(random.choice(karakter_nomor_Pesanan) for _ in range(length))                   
def waktu(detik):
    time.sleep(detik)
    os.system('cls' if os.name == 'nt' else 'clear')

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

def cetak_kantong_belanja(username):
    file_name = f'Kantong_Belanja_User/kantong_belanja_{username}.json'
    try:
        with open(file_name, 'r') as file:
            kantong_belanja = json.load(file)
            print("-----------------------------------")
            print("\tIsi Kantong Belanja:")
            print("-----------------------------------")
            produk_list = []  # List untuk menyimpan produk yang ditampilkan
            for index, list_user in enumerate(kantong_belanja):
                for item_index, item in enumerate(list_user["item"]):
                    produk_list.append(item)  # Simpan item ke dalam list
                    print(f"{item_index +1}. Produk         : {item['produk']}")
                    print(f"   Jenis Produk   : {item['jenis produk']}")
                    print(f"   Jumlah         : {item['jumlah']}")
                    print(f"   Harga per Unit : Rp {item['harga']:,.0f}")  # Format harga dengan ribuan
                    print(f"   Total          : Rp {item['total']:,.0f}")   # Format total dengan ribuan
                    print("-----------------------------------")
            print("===================================")
            return produk_list  # Kembalikan list produk
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except json.JSONDecodeError:
        print("Error saat membaca data dari file JSON.")

def proses_pembayaran(produk, username, index_produk):
    print(f"Proses pembayaran untuk produk: {produk['produk']}")
    print(f"Total yang harus dibayar: Rp {produk['total']:,.0f}")
    
    # Simulasi konfirmasi pembayaran
    konfirmasi = input("Apakah Anda yakin ingin melanjutkan pembayaran? (ya/tidak): ").strip().lower()
    
    if konfirmasi == 'ya':
        while True:
            try:
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
                            print(f"Total yang harus dibayar: Rp {produk['total']:,.0f}")
                            pembayaran_user = input("Silahkan Masukkan Nominal Pembayaran Sesuai Yang Tertera : Rp.")
                            pembayaran_user = int(pembayaran_user)
                            total = produk['total']
                            if pembayaran_user < total:
                                print("Nominal Pembayaran Anda Kurang")
                                continue
                            else:
                                kembalian = pembayaran_user - total
                                print(f"Uang Kembalian Anda Rp.{kembalian:,.0f}")
                                waktu(5)
                                print("Pembayaran sedang diproses...")
                                waktu(5) 
                                print("Pembayaran berhasil! Terima kasih atas pembelian Anda.")
                                status_pembayaran = "Lunas"

                            
                            # Keluar dari fungsi setelah pembayaran berhasil
                    except ValueError:
                        print("Silahkan Masukkan Nominal Uang Berupa Angka")
                        continue
                    status_pembelian_user(produk["jenis produk"],produk['produk'], produk["jumlah"], produk['total'],alamat,pengiriman,user_bayar,status_pembayaran)
                    hapus_item_dari_kantong_belanja(username, index_produk)
                    while True:
                        try:
                            kondisi_user = input('Ingin Membayar Item Lain Lagi ? Jika Ya Ketik "Ya" Jika Tidak Ketik "No" : ')
                            if kondisi_user.lower() == "ya" :
                                waktu(2)
                                username = baca_user_aktif()
                                penyesuaian_user()
                        
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
        
            except ValueError:
                print("Silahkan Masukkan Nominal Uang Berupa Angka")
                continue
            break
    else:
        print("Pembayaran dibatalkan.")

def hapus_item_dari_kantong_belanja(username, index_produk):
    file_name = f'Kantong_Belanja_User/kantong_belanja_{username}.json'
    
    try:
        with open(file_name, 'r') as file:
            kantong_belanja = json.load(file)
            index_item = index_produk - 1
        # Menghapus produk yang dibayar dari kantong belanja
            for list_user in kantong_belanja:
                if 0 <= index_item < len(list_user['item']):
                    removed_item = list_user['item'].pop(index_item)
                else:
                    print("Index tidak valid, tidak ada item yang dihapus.")
        
        # Menyimpan kembali kantong belanja yang sudah diperbarui
        with open(file_name, 'w') as file:
            json.dump(kantong_belanja, file, indent=4)
    except FileNotFoundError:
        print(f"File {file_name} tidak ditemukan.")
    except json.JSONDecodeError:
        print("Error saat membaca data dari file JSON.")

def penyesuaian_user():
    username = baca_user_aktif()
    if username:
        produk_list = cetak_kantong_belanja(username)
        if produk_list:  
            try :
                penentuan_user =  int(input("Silahkan Anda Masukkan Nomor Berikut (1. Hapus Item / 2. Bayar Item / 0. Untuk Kembali Ke Halaman Utama ) : ) : "))
                if penentuan_user == 1 :
                    pemilihan_user = int(input("Silahkan Masukkan Nomor Produk yang ingin dihapus ( Ketik '0' untuk kembali ke Menu Utama ) : "))
                    if 1 <= pemilihan_user <= len(produk_list):
                            produk_terpilih = produk_list[pemilihan_user - 1]
                            print("-----------------------------------")
                            print(f"Anda memilih produk : {produk_terpilih['produk']}")
                            print(f"Jenis Produk        : {produk_terpilih['jenis produk']}")
                            print(f"Jumlah Item         : {produk_terpilih['jumlah']}")
                            print(f"Dan Total Harga     : {produk_terpilih['total']:,.0f}")
                            print("-----------------------------------")
                            verifikasi_user = input("Apakah Anda yakin ingin menghapus Item Tersebut ? (YA/NO): ").strip().lower()
                            if verifikasi_user == "ya" :
                                hapus_item_dari_kantong_belanja(username, pemilihan_user)
                                waktu(3)
                                print("Produk Tersebut Berhasil Di Hapus.....")
                                waktu(3)
                                penyesuaian_user()
                            elif verifikasi_user == "no" :
                                waktu(3)
                                penyesuaian_user()
                    elif pemilihan_user == 0 :
                        waktu(3)
                        penyesuaian_user()
                        
                        
                        
                    else:
                        print("Nomor produk tidak valid.")
                    
                    
                elif penentuan_user == 2 :
                    try:
                        pemilihan_user = int(input("Silahkan Masukkan Nomor Produk yang ingin dibayar ( Ketik '0' untuk kembali ke menu utama ) : "))
                        if 1 <= pemilihan_user <= len(produk_list):
                            produk_terpilih = produk_list[pemilihan_user - 1]
                            print(f"Anda memilih produk: {produk_terpilih['produk']}")
                            # Panggil fungsi untuk memproses pembayaran
                            proses_pembayaran(produk_terpilih, username,pemilihan_user)
                        elif pemilihan_user == 0 :
                            waktu(3)
                            
                            
                            
                        else:
                            print("Nomor produk tidak valid.")
                    except ValueError:
                        print("Input tidak valid. Harap masukkan nomor yang benar.")
                elif penentuan_user == 0 :
                    print("Anda Kembali Ke Halaman Utama")
                    return os.system("python Home/Home_Page.py")

                    
                else :
                    print("Nomor Yang Anda Masukan Tidak Valid !")
            except ValueError:
                print("Input tidak valid. Harap masukkan nomor yang benar.")        
        else:
            print("Kantong belanja kosong.")
    else:
        print("Tidak ada user yang aktif.")

penyesuaian_user()
