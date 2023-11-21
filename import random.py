import random

PW = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

panjang = int(input("Masukkan panjang kata sandi: "))

hasil = ''

for i in range(panjang):
    hasil += random.choice(PW)
print("Kata Sandi yang Dihasilkan:", hasil)
