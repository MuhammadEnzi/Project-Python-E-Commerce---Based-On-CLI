#data
baris = "="*50
garis = "="*50
i = 0
a = 0
nama = []
berat= []
harga = []
total = []
rab = []

#header
print("\n")
print("Program Pengadaan Barang".center(50))
print("PT Daging Segar Selalu".upper().center(50))
print("Tahun 2024".center(50))
print(baris.center(50))
print("\r")
print("Data Barang Baru".center(50))
print("Masukan Data Barang Dibawah Ini!!!".center(50))
print("\r") 

#isi 
Jumlah_barang = int(input("Jumlah Data : "))
while i in range(Jumlah_barang):
    print ("Data ke-",str (i +1))
    nama.append(input("Nama   : "))
    berat.append(int(input("Quantity   : ")))
    harga.append(int(input(f"Harga per kg   : Rp.")))
    total.append(berat[i] * harga[i])
    i = i + 1
print("\r")
perintah = input("Tampilkan Data [y/t]  : ")
if perintah=="y" or perintah=="Y":
    print("\n")
    print("Anggaran Pengadaan Barang".center(73))
    print("PT Daging Segar Selalu".upper().center(73))
    print("Tahun 2024".center(73))
    print(baris.center(73))
    print("\r")
    print("Data Barang Baru".center(73))
    print("\r")
    print(garis.center(73))
    print("            | No |  Nama Barang  | Berat | Harga Per kg |   Total   |")
    print(garis.center(73))
    rab = 0
    while a < Jumlah_barang:
        rab = rab + total[a]
        print("    %i     %s     %i      Rp.%s    Rp.%s" % (a+1, nama[a], berat[a], format(harga[a], ',.0f').replace(',', '.'), format(total[a], ',.0f').replace(',', '.')))
        a = a + 1 
    print(garis.center(73))
    print(f"                     Total Anggaran    : Rp.{rab:,.0f}", )
    menu = input("Kembali ke Menu   : ")
    if menu=="y" or menu=="Y" :
        print("Dashboard")
    else:
        quit("Terimakasih")
