from ast import main


class buku:
    def __init__(self,judul,penulis,genre,status):
        self.judul = judul
        self.penulis = penulis
        self.genre = genre
        self.status = status

    def __str__(self):
        return f"{self.judul} - {self.penulis} ({self.genre}) - staus: {self.status}"
    
#buat kelas perpustakaan:

class perpustakaan:
    def __init__(self):
        self.koleksi_buku = []

    def tampilam_buku(self):
        if self.koleksi_buku:
            print("-- Daftar Buku --")
            for buku in self.koleksi_buku:
                print(buku)
        else:
            print("Koleksi buku masih kosong.")
    def cari_buku(self, judul):
        for buku in self.koleksi_buku:
            if buku.judul.lower() == judul.lower():
                print(buku)
                return
        print(f"buku dengan judul '{judul}'tidak ditemukan.")

    def pinjam_buku(self, buku, anggota):
        if buku.status == "Tersedia":
           buku.status = "Dipinjam"
           anggota.buku_pinjaman.append(buku)
           print(f"buku '{buku.judul}' berhasil dipinjam oleh {anggota.nama}.")
        else:
           print(f"buku '{buku.judul}' tidak tersedia untuk dipinjam.")

#kelas anggota: 

class Anggota:
    def __init__(self,nama,ID):
        self.nama = nama
        self.ID = ID
        self.buku_pinjaman = []

    def tampilkan_buku_pinjaman(self):
        if self.buku_pinjaman:
            print(f"-- buku pinjaman {self.nama} --")
            for buku in self.buku_pinjaman:
                print(buku)
        else:
            print(f"{self.nama} tidak memiliki buku pinjaman.")

#kelas main:

    def main():
        #buat beberapa buku
        buku1 = buku("bumi", "tere liye", "fiksi", "tersedia")
        buku2 = buku("laskar pelangi", "andrea hirata", "fiksi", "tersedia")
        buku3 = buku("filosifi terbang", "dewi lestari", "fiksi", "dipinjam")

        #buat perpustakaan dan anggota
        perpustakaan = perpustakaan()
        perpustakaan.koleksi_buku.extend([buku1, buku2, buku3])

        Anggota1 = Anggota("adi", 12345)
        Anggota2 = Anggota("budi", 56789)

        #jalankan program
        print("\n-- menu perpustakaan")
        print("1. tampilkan daftar buku")
        print("2. cari buku")
        print("3. pinjam buku")
        print("4. kembalikan")
        angka=int(input("pilih menu :_"))

        if angka == 1:
            perpustakaan.tampilkan_buku();
        elif angka == 2:
            judul=input("input judul buku")
            perpustakaan.cari_buku(judul);
        elif angka == 3:
            buku=input("buku yang dipinjam:")
            anggota=input("input nama anggota:")
        else:
            print("anda salah pilih")

        if __name__=="__main__":
            main();