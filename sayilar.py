adet = int(input("Kaç adet sayı girmek istiyorsunuz? "))
sayılar = []
toplam = 0

for i in range(adet):
    sayı = int(input(f"{i+1}. Sayıyı giriniz: "))
    sayılar.append(sayı)
    toplam += sayı

print("Girdiğiniz sayıların toplamı: ", toplam)

if adet > 0:
    ortalama = toplam / adet
    print("Girdiğiniz sayıların ortalaması: ", ortalama)

sayılar.sort()
print("Girdiğiniz sayıların sıralaması: ", sayılar)
