import os
import time
import json
import re
import getpass
import sys
# Tampilan Menu Login
def tampilkan_menu_utama():
    print("-------------LOGIN-----------------")
    print("1. DAFTAR ( SIGN UP )")
    print("2. LOGIN ( SIGN IN )")
    print("0. KELUAR ( LOGOUT )")
    print("-----------------------------------")
# Waktu Bersihkan Layar
def waktu(detik):
  time.sleep(detik)
  os.system('cls' if os.name == 'nt' else 'clear')
# Ketentuan & Syarat Password SignUp
def validasi_password(password):
  if len(password) < 8 :
    return "Panjang Password Harus Minimal 8 Karakter"
  if not re.search("[a-z]", password):
    return "Password Harus Mengandung Satu Huruf Kecil"
  if not re.search("[A-Z]", password):
    return "Password Harus Mengandung Satu Huruf Besar"
  if not re.search("[0-9]", password):
    return "Password Setidaknya Harus Mengandung Satu Angka"
  return "Password Valid"
# Membaca File Json Setiap Ada Update File
def baca_data():
  try:
    with open("Menu_Login/data_user.json", "r") as filedata :
      return json.load(filedata)
  except(FileNotFoundError,json.JSONDecodeError):
    return []
  
def buat_username_aktif(username):
    # Memastikan Keberadaan File Menu_Login/user_active.json
    if os.path.exists('Menu_Login/user_active.json'):
        with open('Menu_Login/user_active.json', 'r') as file:
            try:
                data_user_aktif = json.load(file)
            except json.JSONDecodeError:
                #Jika File Tidak Ada, Otomatis Akan Mengembalikan Data Dictionary Kosong
                data_user_aktif = {}
    else:
        data_user_aktif = {}

    # Menyimpan username yang sedang aktif
    data_user_aktif["Username Yang Sedang Aktif"] = username
    with open('Menu_Login/user_active.json', 'w') as file:
        json.dump(data_user_aktif, file)
  

# Menyimpan Update Data User Di Json
def simpan_data(username,password):
  data = baca_data()
  data.append({"username":username,"password":password})
  with open("Menu_Login/data_user.json","w") as filedata :
    json.dump(data,filedata,indent=3)


# Verifikasi User Saat Sign In
def checking_data(username,password):
  data = baca_data()
  for userdata in data:
    if userdata["username"] == username and userdata["password"] == password:
      return True
  return False

# Proses Authentikasi Login
def proses_Login():
  while True:
    tampilkan_menu_utama()
    pemilihan_menu = int(input("Silahkan Pilih Menu Berdasarkan Kode (1/2/0) : "))
    waktu(2)
    if pemilihan_menu == 0 :
      print("----- TERIMA KASIH TELAH DATANG DI E - COMMERCE KAMI SAMPAI BERTEMU KEMBALI ----- ")
      waktu(4)
      break  
    elif pemilihan_menu == 1 :
        print("-------------------SIGN UP-------------------")
        while True:
          username_signUp = input("Masukkan Username Baru : ")
          if username_signUp.strip() == "" :
              print("Username tidak boleh kosong. Silakan coba lagi.")
              waktu(2)
              continue
          if any(user["username"] == username_signUp for user in baca_data()):
            print("Username Sudah Dipakai")
          else :
              break
        while True:
          password_SignUp = input("Masukkan Password Baru : ")
          print("---------------------------------------------")
          hasil_validasi = validasi_password(password_SignUp)
          if hasil_validasi == "Password Valid" :
            simpan_data(username_signUp,password_SignUp)
            print("SignUp Berhasil...., SIlahkan Melakukan SignIn Di Halaman Menu Utama !!!")
            waktu(3)
            break
          else:
            print(hasil_validasi)


    elif pemilihan_menu == 2 :
      percobaan_login = 0
      while True :
        print("-------------------SIGN IN-------------------")
        username_login = input("Masukkan Username Anda :  ")
        password_login = getpass.getpass("Masukkan Password Anda : ")
        print("---------------------------------------------")
        if checking_data(username_login,password_login):
          print("Login Berhasil....")
          waktu(3)
          buat_username_aktif(username_login)
          os.system("python Home/Home_Page.py")
          return username_login
        else:
          print("Maaf Username dan Password Yang Anda Masukkan Salah !!! Silahkan Coba Lagi....")
          waktu(2)
          percobaan_login += 1

          if percobaan_login >= 3 :
            print("Maaf Anda Sudah Gagal Login Sebanyak 3 kali Silahkan Pergi Ke Menu Utama Lalu SignUp")
            waktu(2)
            break
    else:
      print("Maaf Kode Nomor Tidak Tersedia, Silahkan Coba Lagi....")
      continue
proses_Login()
