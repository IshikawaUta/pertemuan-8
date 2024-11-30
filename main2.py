# Mengimpor modul warna
from colorama import Fore
from pprint import pprint

# Membuat dictionary
mahasiswa = {
    "nama": "Eka",
    "umur": 20,
    "jurusan": "informatika"
}

# Mengakses nilai
print(Fore.RED, mahasiswa["nama"]) # output: Eka

# Mengubah nilai dari kunci yang sama
mahasiswa.update({
    "umur": 19
})

# Menambahkan pasangan kunci-nilai
mahasiswa["nim"] = "12345"
print(Fore.MAGENTA, mahasiswa, Fore.RESET)
pprint(mahasiswa)