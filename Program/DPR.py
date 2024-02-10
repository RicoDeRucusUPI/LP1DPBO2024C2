# ==========================================================================
# Saya Rico Valentino 1909263 mengerjakan (LP1)
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak
# melakukan kecurangan seperti yang telah dispesifikasikan.
# ==========================================================================


# Alur OOP
# class dengan nama DPR memiliki properti dpr_data dengan berbentuk object dalam array
# memiliki 4 method yaitu add, show, update, dan delete

import time

class DPR:
    # Membuat class dengan nama DPR
    __dpr_data = []
    # properti private

    def __init__(self):
        self.__dpr_data = []
        # initialisasi property

    def add(self, nama=None, nama_bidang=None, nama_partai=None):
        # method add untuk menambahkan data
        self.__dpr_data.append({
            "id" : str(int(time.time())),
            "nama" : nama or "",
            "nama_bidang" : nama_bidang or "",
            "nama_partai" : nama_partai or ""
        })
        # tambahkan data
        print("======================================")
        print("======= BERHASIL DI TAMBAHKAN ========")
        print("======================================")
        # info berhasil


    def show_all(self):
        # method tampilkan semua data
        i = 0
        for item in self.__dpr_data:
            # tampilkan sebanyak data yang ada
            print(f'{i+1}. ID: {item["id"]}, Nama: {item['nama']}, Nama Bidang: {item['nama_bidang']}, Nama Partai: {item["nama_partai"]}')
            i += 1

    def update(self, id, nama=None, nama_bidang=None, nama_partai=None):
        # method update dengan menambahkan parameter id untuk proses pencarian data yang akan di update
        i = 0;
        found = False;
        for item in self.__dpr_data:
            # loop semua data
            if(item['id'] == id):
                # jika data dengan id yang di cari sama maka ubah isi data tersebut
                self.__dpr_data[i] = {
                    "id" : item['id'],
                    "nama" : nama or "",
                    "nama_bidang" : nama_bidang or "",
                    "nama_partai" : nama_partai or ""               
                }
                found = True;
                break
                # berhenti ketika ketemu
            i += 1
        if(found == False):
            print("======================================")
            print("========= ID TIDAK DITEMUKAN =========")
            print("======================================")
        else:
            print("======================================")
            print(f"===== ID {id} BERHASIL DI UBAH =====")
            print("======================================")



    def delete(self, id):
        # method delete dengan menambahkan parameter id untuk proses pencarian data yang akan di delete
        i = 0;
        found = False;
        for item in self.__dpr_data:
            # loop semua data
            if(item['id'] == id):
                # jika data dengan id yang di cari sama maka ubah isi data tersebut
                del self.__dpr_data[i]
                # hapus data sesuai index yang ditemukan
                found = True;
                break
            i += 1
        if(found == False):
            print("======================================")
            print("========= ID TIDAK DITEMUKAN =========")
            print("======================================")
        else:
            print("======================================")
            print(f"===== ID {id} BERHASIL DI HAPUS =====")
            print("======================================")
