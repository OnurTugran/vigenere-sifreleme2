# vigenere-sifreleme
Python ile yazılmış temel Vigenère şifreleme ve şifre çözme algoritması.

# Vigenère Şifreleme (Python)

Bu proje, Vigenère algoritması kullanılarak metinleri şifreleyip çözebilen basit bir Python uygulamasıdır.

## ✍️ Kullanım

1. `metin` ve `anahtar` girdilerini alır.
2. Şifreli metni üretir.
3. Şifrelenmiş metni anahtar ile çözer.

## Kodun Çalışma Mantığı
- Metindeki her harf sırayla alınır:
  - Eğer harf bir harf karakteriyse (`isalpha()` kontrolü):
    - `ord()` fonksiyonu ile harfin ASCII değeri alınır.
    - Anahtar harfinin ASCII değeri ile bir kaydırma değeri hesaplanır.
    - `(harf + kaydırma) % 26` işlemi ile yeni harf bulunur.
    - Yeni harf şifreli metne eklenir.
  - Harf değilse (boşluk, noktalama vs.), olduğu gibi eklenir.
- Anahtar, metin boyunca döngüsel şekilde ilerler.

           
