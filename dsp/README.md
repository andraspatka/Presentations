# Struktúra

- Veszteségmentes adattömörítés
- Veszteséges adattömörítés
- Fourier transzform - mit tud?
- DCT képlet
- Tömörítő algoritmus - JPEG

# Veszteség nélküli tömörítés

- lehetséges a tömörített adatokból az eredeti adat pontos rekonstrukciója
- Huffman kódolás
- példa, kép

# Veszteséges tömörítés

Kvantálás: A kvantálás során az analóg jeleket olyan diszkrét jelekké alakítják át, mely a digitális számítógépek számára ’érthetők’. 

Alkalmazások:
 - Képtömörítés:
   - JPEG
 - Videótömörítés:
   - MPEG, H.26X

Béka, JPEG példa:
 - Eredeti kép 39.8 KB
 - Tömörítve, 97%-al kevesebb információ, 1.2 KB
 - Erős tömörítés után 98.5%-al kevesebb információ, 662 B - ezen is felismerhető a béka

# JPEG

- két alapötlet: 
  - az emberi szem a világosságra sokkal érzékenyebb, mint a színre
  - az emberi szem a magas frekvenciájú változásokat sokkal kevésébé érzékeli, mint az alacsony frekvenciájú változásokat: pld videóban hány kép van másodpercenként, videójátékok: fps

- kép transzformációja a frekvencia-tartományba DCT-vel


- RGB -> YCbCR: By Mike1024 - Based on the (public domain) photo Image:Barns grand tetons.jpg. Code above and resulting output by Mike1024., Public Domain, https://commons.wikimedia.org/w/index.php?curid=1493370
  - Y - luma komponens a kép világossága
  - Cb - chroma kék különbség
  - Cr - chroma piros különbség
  - Miért? Egy színkanálisban van a világosság információ, amire a legérzékenyebb az emberi szem. A többi színkanálist lehet ritkábban mintavételezni, így már el tudunk érni egy fokú sűrítést
- Downsampling
- A képet 8x8-as részképekre bontjuk
- DCT:
  - Az értékek 0 és 255 között vannak, ezeket át kell változtatni, hogy -128 és 127 között legyenek (cos -1 és 1 között veszi fel az értékeit)
  - együtthatók kiszámolása
- Kvantálás
  - kvantálási mátrix
- Entrópia kódolás

# Forrasok

- huffman kép https://www.journaldev.com/23246/huffman-coding-algorithm
- cosinusok: Computerphile