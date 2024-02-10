# ==========================================================================
# Saya Rico Valentino 1909263 mengerjakan (LP1)
# dalam mata kuliah DPBO untuk keberkahanNya maka saya tidak
# melakukan kecurangan seperti yang telah dispesifikasikan.
# ==========================================================================



from DPR import DPR
# import class DPR

anggota_DPR = DPR()
# initialisasi class DPR

print("======================================")
print("Fitur:")
print("1. Menambahkan Data")
print("2. Merubah Data")
print("3. Menghapus Data")
print("4. Tampilkan Data")
print("5. Selesai")
print("======================================\n")
# tampilan fitur yang tersedia

stop = 0
# untuk berhenti loop
while (stop != 1):
	# loop berhenti ketika variabel stop yaitu 1
	selected_fitur = input("\nPilih Fitur: ")
	# input memilih fitur
	if(selected_fitur == "1"):
		# fitur satu menambahkan data
		print("\nFitur Menambahkan Data")
		nama = input("Nama: ")
		nama_bidang = input("Nama Bidang: ")
		nama_partai = input("Nama Partai: ")
		# input data yang dibutuhkan
		anggota_DPR.add(nama, nama_bidang, nama_partai)
		# panggil method add pada class DPR
	elif(selected_fitur == "2"):
		# fitur dua merubah data
		print("\nFitur Merubah Data")
		id = input("ID Anggota: ")
		nama = input("Nama: ")
		nama_bidang = input("Nama Bidang: ")
		nama_partai = input("Nama Partai: ")
		# input data yang dibutuhkan
		anggota_DPR.update(id,nama, nama_bidang, nama_partai)
		# panggil method update pada class DPR
	elif(selected_fitur == "3"):
		# fitur tiga menghapus data 
		print("\nFitur Menghapus Data")
		id = input("ID Anggota: ")
		# input data yang dibutuhkan
		anggota_DPR.delete(id)
		# panggil method delete pada class DPR
	elif(selected_fitur == "4"):
		# fitur empat tampilkan semua data 
		anggota_DPR.show_all()
		# panggil method show_all pada class DPR
	elif(selected_fitur == "5"):
		# program berhenti
		stop = 1
