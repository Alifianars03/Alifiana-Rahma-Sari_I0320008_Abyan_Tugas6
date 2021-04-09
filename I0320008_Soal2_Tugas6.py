bnilai = int(input("Total banyaknya nilai yang di input : "))
print()
data = []

i = 1
while i <= bnilai:
    datanilai = int(input("Nilai %d : " %i))
    data.append(datanilai)
    i = i + 1
print()

totalrataan = sum(data)/bnilai
print("Hasil nilai rata-rata dari nilai tersebut ialah : %d" %totalrataan)