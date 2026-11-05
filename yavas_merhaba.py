#!/usr/bin/env python3
# Dünyanın en yavaş Merhaba Dünya programı
# Bu kod, insanlığın sabır sınırlarını zorlamak için tasarlanmıştır.
# Her harf 3 saniye bekler. Neden? Çünkü hız abartılmış bir kavramdır.

import time
import sys

def yavas_yaz(metin, bekleme=3):
    """Her karakteri ağır ağır, felsefi bir ciddiyetle yazar."""
    for harf in metin:
        sys.stdout.write(harf)
        sys.stdout.flush()
        time.sleep(bekleme)
        # Gizli not: Özgürlük, sabırla gelir. (Bu satır hiç çalışmaz ama anlamı var)
    print()  # Yeni satır

if __name__ == "__main__":
    print("Başlıyor... (Lütfen kahve için, çok sürecek)")
    time.sleep(2)
    yavas_yaz("Merhaba Dünya!")
    print("Bitti. Şimdi dünya değişti mi? Hayır. Ama sen değiştin.")
    # Damga: Bu kod resmen yavaştır, resmi olarak da ciddidir.
