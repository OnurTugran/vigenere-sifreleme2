
def vigerne_sifrele(metin,anahtar):
    sifreli_metin = ""
    anahtar = anahtar.upper()
    metin = metin.upper()
    anahtar_index = 0  #Anahtarın Hangi Harfinde Olduğumuzu Takip Etmek İçin.

    for harf in metin:
        if harf.isalpha():
            kaydirma = ord(anahtar[anahtar_index]) - ord('A')
            yeni_harf = chr( (ord(harf)  - ord('A') + kaydirma) % 26 + ord('A')  )
            sifreli_metin += yeni_harf
            anahtar_index = (anahtar_index+1) % len(anahtar)
        else:
            sifreli_metin += harf
    return sifreli_metin

def vigerne_coz(metin,anahtar):
    cozulu_metin = ""
    anahtar = anahtar.upper()
    metin = metin.upper()
    anahtar_index = 0

    for harf in metin:
        if harf.isalpha():
            kaydirma = ord(anahtar[anahtar_index]) - ord('A')
            yeni_harf = chr((ord(harf) - ord('A') - kaydirma) % 26 + ord('A'))
            cozulu_metin += yeni_harf
            anahtar_index = (anahtar_index +1) % len(anahtar)
            
        else:
            cozulu_metin += harf
    return cozulu_metin 


metin = input("Şifrelemek İstediğiniz Metini Giriniz: ")

anahtar = input("Anahtar Kelimeyi Giriniz: ")

sifreli = vigerne_sifrele(metin,anahtar)
print(f"Şifreli Metin =\n{sifreli}")



cozulmus = vigerne_coz(sifreli,anahtar)
print(f"Şifreli Metinin Çözülmüş Hali=\n{cozulmus}")
