print("Hello")
import random
karakter = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
uzunluk = int(input("Şifrenizin uzunluğunu giriniz"))
sifre = ""
for i in range(uzunluk):
    a = random.choice(karakter)
    sifre = sifre + a
print(sifre)



