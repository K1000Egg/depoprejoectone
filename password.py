import random


karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

sayi = int(input("Kaç karakterden oluşan bir şifre?"))
parola = ""

for i in range(sayi):
    parola += random.choice(karakterler)

print( "parola:", parola)
