from colorama import Fore # import module warna
from pprint import pprint # import module pprint

buah = {
    "apel": {"harga": 15000, "rasa": "manis"},
    "pisang": {"harga": 10000, "rasa": "manis"},
    "anggur": {"harga": 20000, "rasa": "asam manis"}
} #variable keys dan values
print(Fore.GREEN + "Pisang memiliki harga Rp", buah["pisang"]["harga"], "dan rasanya", buah["pisang"]["rasa"]) #output harga dan rasa pisang
buah["mangga"] = {"harga": 15000, "rasa": "manis"} #menambahkan buah mangga
buah["anggur"]["harga"] = 25000 #mengubah harga anggur
buah["anggur"]["rasa"] = "enak" #mengubah rasa anggur
# del buah["apel"]
buah_copy = buah .copy() # metode copy digunakan untuk menyalin
daftar_buah = buah.keys() # metode keys digunakan untuk menampilkan kunci
daftar_nilai = buah.values() # metode values digunakan untuk menampilkan nilai
apel_info = buah.get("apel") # metode get digunakan untuk menampilkan informasi apel
pisang_info = buah.get("pisang") # metode get digunakan untuk menampilkan informasi pisang
anggur_info = buah.get("anggur") # metode get digunakan untuk menampilkan informasi anggur
apel_pop = buah.pop("apel") # metode pop digunakan untuk menghapus satu keys dan values sesuai yang kita hapus
last_item = buah.popitem() # metode popitem digunakan untuk menghapus akhir dari keys dan values
buah.setdefault("semangka", {"harga": 20000, "rasa": "manis"}) # metode setdeffault digunakan untuk menambahkan keys dan values
buah.update({
    "jeruk": {"harga": 20000, "rasa": "asam manis"} # metode update digunakan untuk mengubah nilai dari kunci yang sama
})

print(Fore.YELLOW, buah, "\n") # output variable buah
print(Fore.RED, buah_copy, "\n") # output variable buah_copy
print(Fore.CYAN + "Daftar buah:")
print(list(daftar_buah)) # output variable daftar_buah
print("\n=======================================")
print("Daftar nilai buah:")
for nilai in daftar_nilai:
    print(nilai) # output variable daftar_nilai
print()
print("Informasi apel yang di hapus", apel_pop) # output variable apel_pop 
print("\ndictionary setelah menghapus apel")
print(buah, "\n") # output variable buah setelah di pop
print("Item terakhir yang dihapus", last_item, "\n") # output variable last_item
print(Fore.MAGENTA + "Informasi apel:", apel_info) # output variable apel_info
print("Informasi pisang:", pisang_info) # output variable pisang_info
print("Informasi anggur:", anggur_info, "\n", Fore.GREEN) # output variable anggur_info
pprint(buah) # output variable bauh
print(Fore.RESET) # output reset warna
