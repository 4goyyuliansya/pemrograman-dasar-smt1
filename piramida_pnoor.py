n = int(input("Masukkan tinggi pyramid: ")) # Meminta input dari pengguna untuk menentukan tinggi pyramid, lalu mengubahnya menjadi integer

for i in range(1, n + 1): # Perulangan untuk mencetak baris pyramid dari baris pertama sampai baris ke-n

    # Mencetak spasi sebanyak (n - i) untuk membuat pyramid terlihat rata tengah
    # end="" digunakan agar tidak pindah ke baris baru setelah mencetak spasi
    print(" " * (n - i), end="")

    # Mencetak simbol bintang sebanyak i kali untuk membentuk pola segitiga
    # Setiap baris akan memiliki jumlah bintang yang bertambah
    print("* " * i)