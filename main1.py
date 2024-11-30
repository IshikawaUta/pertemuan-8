from colorama import Fore

buah = {
    "apel": {"harga": 15000, "rasa": "manis"},
    "pisang": {"harga": 10000, "rasa": "manis"},
    "anggur": {"harga": 20000, "rasa": "asam manis"}
}

buah["mangga"] = {"harga": 15000, "rasa": "manis"}
buah["anggur"]["harga"] = 25000
buah["anggur"]["rasa"] = "enak"
del buah["apel"]

def tampilkan_buah(buah):
    for nama_buah, detail in buah.items():
        print(f"{Fore.RED}Buah {nama_buah} memiliki harga Rp{detail['harga']} dan rasanya {detail['rasa']}{Fore.RESET}")

def cari_buah_berdasarkan_rasa(buah, rasa):
    buah_yang_ditemukan = []
    for nama_buah, detail in buah.items():
        if detail["rasa"] == rasa:
            buah_yang_ditemukan.append(nama_buah)
    return buah_yang_ditemukan

while True:
    print(Fore.YELLOW + "\nMenu:")
    print(Fore.YELLOW + "1. Tampilkan semua buah")
    print(Fore.YELLOW + "2. Cari buah berdasarkan rasa")
    print(Fore.YELLOW + "3. Keluar")
    pilihan = input(Fore.RED + "Pilih menu: ")

    if pilihan == "1":
        tampilkan_buah(buah)
    elif pilihan == "2":
        rasa_yang_dicari = input("Masukkan rasa yang ingin dicari: ")
        hasil_pencarian = cari_buah_berdasarkan_rasa(buah, rasa_yang_dicari)
        if hasil_pencarian:
            print(f"Buah dengan rasa {rasa_yang_dicari}:")
            for buah in hasil_pencarian:
                print(Fore.RED, f"- {buah}")
        else:
            print(f"Tidak ada buah dengan rasa {rasa_yang_dicari}")
    elif pilihan == "3":
        print(Fore.RESET + "")
        break
    else:
        print("Pilihan tidak valid")
        