# Student Grade Input System

## Description

This Python script is used to calculate and save student grades in an Excel format. The script prompts the user for input on the contribution percentages for attendance, assignments, mid-term exams (UTS), and final exams (UAS). Based on this input, the script calculates the final grade and grade letter for each student, and then saves the results in an Excel file.

## Features

- Input total contribution percentages (Attendance, Assignments, UTS, UAS) with validation that the total must be 100%.
- Input the number of students and data for each student.
- Calculate the final grade based on contribution percentages.
- Calculate the grade letter based on the final grade.
- Save the results in an Excel file (`.xlsx`).

## How to Use

1. **Install Required Libraries**

   Make sure you have the `pandas` and `openpyxl` libraries installed. You can install them using pip:

```sh
pip install pandas openpyxl
```

2. Run the Script

Save the following code into a Python file, for example input_student_grades.py, and run the script:

```python
import pandas as pd

# Function to calculate grade based on final score
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

# Input contribution percentages
print("Enter the total contribution percentages (Attendance, Assignments, UTS, UAS) in percent (Total must be 100%):")
persen_kehadiran = float(input("Attendance Percentage: "))
persen_tugas = float(input("Assignments Percentage: "))
persen_uts = float(input("UTS Percentage: "))
persen_uas = float(input("UAS Percentage: "))

# Validate total percentage
if persen_kehadiran + persen_tugas + persen_uts + persen_uas != 100:
    print("Total percentage must be 100%!")
    exit(1)

# Input number of students
jumlah_mahasiswa = int(input("Enter the number of students: "))

# List to store student data
data_mahasiswa = []

# Input student data
for i in range(jumlah_mahasiswa):
    print(f"Enter data for student {i + 1}:")
    nama = input("Name: ")
    npm = input("NPM: ")
    nilai_keadaan = float(input(f"Enter attendance score for student {nama}: "))
    nilai_tugas = float(input(f"Enter assignment score for student {nama}: "))
    nilai_uts = float(input(f"Enter UTS score for student {nama}: "))
    nilai_uas = float(input(f"Enter UAS score for student {nama}: "))

    # Calculate final score
    nilai_akhir = (nilai_keadaan * persen_kehadiran / 100 +
                   nilai_tugas * persen_tugas / 100 +
                   nilai_uts * persen_uts / 100 +
                   nilai_uas * persen_uas / 100)

    # Calculate grade letter
    grade = hitung_grade(nilai_akhir)

    # Save student data with desired column order
    data_mahasiswa.append({
        'Name': nama,
        'NPM': npm,
        'Attendance': nilai_keadaan,
        'Assignments': nilai_tugas,
        'UTS': nilai_uts,
        'UAS': nilai_uas,
        'Final Score': nilai_akhir,
        'Grade': grade
    })

# Display results in table with desired column order
df = pd.DataFrame(data_mahasiswa, columns=[
    'Name', 'NPM', 'Attendance', 'Assignments', 'UTS', 'UAS', 'Final Score', 'Grade'
])

# Save to Excel file
output_file = 'student_grades.xlsx'
df.to_excel(output_file, index=False)

print(f"\nStudent grades have been saved to '{output_file}'")

```

## Output

After running the script, an Excel file named student_grades.xlsx will be created in the same directory as the script, containing a table with the data for each student that was input.
