import pandas as pd

# Fungsi untuk menghitung grade berdasarkan nilai akhir
def hitung_grade(nilai_akhir):
    if nilai_akhir >= 88:
        return 'A'
    elif nilai_akhir >= 75:
        return 'B'
    elif nilai_akhir >= 65:
        return 'C'
    elif nilai_akhir >= 55:
        return 'D'
    else:
        return 'E'

# Input persentase kontribusi
print("Masukkan persentase kontribusi total (Kehadiran, Tugas, UTS, UAS) dalam persen (Total harus 100%):")
persen_kehadiran = float(input("Persentase Kehadiran: "))
persen_tugas = float(input("Persentase Tugas: "))
persen_uts = float(input("Persentase UTS: "))
persen_uas = float(input("Persentase UAS: "))

# Validasi total persentase
if persen_kehadiran + persen_tugas + persen_uts + persen_uas != 100:
    print("Total persentase harus 100%!")
    exit(1)

# Input jumlah mahasiswa
jumlah_mahasiswa = int(input("Masukkan jumlah mahasiswa: "))

# List untuk menyimpan data mahasiswa
data_mahasiswa = []

# Input data mahasiswa
for i in range(jumlah_mahasiswa):
    print(f"Masukkan data mahasiswa ke-{i + 1}:")
    nama = input("Nama: ")
    npm = input("NPM: ")
    nilai_keadaan = float(input(f"Masukkan nilai kehadiran mahasiswa {nama}: "))
    nilai_tugas = float(input(f"Masukkan nilai tugas mahasiswa {nama}: "))
    nilai_uts = float(input(f"Masukkan nilai UTS mahasiswa {nama}: "))
    nilai_uas = float(input(f"Masukkan nilai UAS mahasiswa {nama}: "))

    # Hitung nilai akhir
    nilai_akhir = (nilai_keadaan * persen_kehadiran / 100 +
                   nilai_tugas * persen_tugas / 100 +
                   nilai_uts * persen_uts / 100 +
                   nilai_uas * persen_uas / 100)
    
    # Hitung grade
    grade = hitung_grade(nilai_akhir)

    # Simpan data mahasiswa dengan urutan kolom yang diinginkan
    data_mahasiswa.append({
        'Nama': nama,
        'NPM': npm,
        'Kehadiran': nilai_keadaan,
        'Tugas': nilai_tugas,
        'UTS': nilai_uts,
        'UAS': nilai_uas,
        'Nilai Akhir': nilai_akhir,
        'Grade': grade
    })

# Tampilkan hasil dalam bentuk tabel dengan urutan kolom yang diinginkan
df = pd.DataFrame(data_mahasiswa, columns=[
    'Nama', 'NPM', 'Kehadiran', 'Tugas', 'UTS', 'UAS', 'Nilai Akhir', 'Grade'
])

# Simpan ke file Excel
output_file = 'daftar_nilai_mahasiswa.xlsx'
df.to_excel(output_file, index=False)

print(f"\nHasil Nilai Mahasiswa telah disimpan ke '{output_file}'")
