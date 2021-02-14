radius = input("Input jari-jari lingkaran : ")
try:
    radius_int = int(radius)
    area = 22 / 7 * radius_int ** 2
    area_float = round(area, 2)
    print(f"Luas lingkaran dengan jari-jari {radius} cm adalah {area_float} cm\u00b2.")
except ValueError:
    print("Anda harus menginput tipe data integer!")
