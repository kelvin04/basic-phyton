theory_scores = int(input("Input nilai ujian teori : "))
practice_scores = int(input("Input nilai ujian praktek : "))

if theory_scores >= 70 and practice_scores >= 70:
    print("Selamat, anda lulus!")
elif theory_scores >= 70 and practice_scores < 70:
    print("Anda harus mengulang ujian praktek.")
elif theory_scores < 70 and practice_scores >= 70:
    print("Anda harus mengulang ujian teori.")
else:
    print("Anda harus mengulang ujian teori dan praktek.")