import tkinter as tk
from tkinter import messagebox
import os
# gerekli modülleri import ediyoruz

# restoan sınıfı oluşturuyoruz
class Restoran:
    # sınıfı constructor fonksiyonu ile başlatıyoruz
    def __init__(self):
        self.pencere=tk.Tk()
        self.pencere.title("Restoran Otomasyon Uygulaması v1.0")
        self.pencere.config(bg="#22223b")
        # ekranı kapatmak için kapat butonuna basınca çalışacak fonksiyonu tanımlıyoruz
        self.pencere.protocol("WM_DELETE_WINDOW",self.kapatButonu)
        # pencereyi sabit boyutlarda oluşturuyoruz
        self.pencere.geometry("900x550")
        self.pencere.resizable(False,False)
        # pencereyi oluşturduktan sonra fonksiyonları çağırıyoruz 
        self.dosyaKontrol()
        self.icecekOlustur()
        self.yemekOlustur()
        self.tatliOlustur()
        self.baslik()
        self.masalar()
        self.masaDegerYazdir()
        self.hesapla()
        self.yardim()
        self.pencere.mainloop()
    def baslik(self):
        # uygulama ismini yazdırıyoruz
        self.uygulamaIsim=tk.Label(self.pencere,text="Restoran Otomasyonu",bg="#22223b",font=("Arial",30,'bold'),foreground="#f2e9e4")
        self.uygulamaIsim.pack(side="top")
    # iceceklerin oluşturulduğu fonksiyon

    def icecekOlustur(self):
        # iceceklerin başlığı
        self.icecekBaslik=tk.Label(self.pencere,text="İçecekler",bg="#22223b",font=("Arial",20,'bold','underline'),foreground="#f2e9e4")
        self.icecekBaslik.place(x=5,y=50)

        self.suEtiket=tk.Label(self.pencere,font=("Arial",13),text="Su 3₺",bg="#22223b",foreground="#f2e9e4")
        self.suEtiket.place(x=5,y=100)

        self.suEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.suEntry.insert(0,"0")
        self.suEntry.place(x=180,y=105)
        self.suArttir = tk.Button(self.pencere, bg="#22223b", fg="white", text="+", command=lambda: self.miktar_degistir(self.suEntry, "arttir"))
        self.suArttir.place(x=155, y=105)
        self.suAzalt = tk.Button(self.pencere, bg="#22223b", fg="white", text="-", command=lambda: self.miktar_degistir(self.suEntry, "azalt"))
        self.suAzalt.place(x=220, y=105)
        self.cayEtiket=tk.Label(self.pencere,font=("Arial",13),text="Çay 5₺",bg="#22223b",foreground="#f2e9e4")
        self.cayEtiket.place(x=5,y=150)

        self.cayEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.cayEntry.insert(0,"0")
        self.cayEntry.place(x=180,y=155)
        self.cayArttir = tk.Button(self.pencere, bg="#22223b", fg="white", text="+", command=lambda: self.miktar_degistir(self.cayEntry, "arttir"))
        self.cayArttir.place(x=155, y=155)
        self.cayAzalt = tk.Button(self.pencere, bg="#22223b", fg="white", text="-", command=lambda: self.miktar_degistir(self.cayEntry, "azalt"))
        self.cayAzalt.place(x=220, y=155)

        self.kahveEtiket=tk.Label(self.pencere,font=("Arial",13),text="Kahve 7₺",bg="#22223b",foreground="#f2e9e4")
        self.kahveEtiket.place(x=5,y=200)

        self.kahveEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.kahveEntry.insert(0,"0")
        self.kahveEntry.place(x=180,y=205)
        self.kahveArttir = tk.Button(self.pencere, bg="#22223b", fg="white", text="+", command=lambda: self.miktar_degistir(self.kahveEntry, "arttir"))
        self.kahveArttir.place(x=155, y=205)
        self.kahveAzalt = tk.Button(self.pencere, bg="#22223b", fg="white", text="-", command=lambda: self.miktar_degistir(self.kahveEntry, "azalt"))
        self.kahveAzalt.place(x=220, y=205)

        self.gazozEtiket=tk.Label(self.pencere,font=("Arial",13),text="Gazoz 4₺",bg="#22223b",foreground="#f2e9e4")
        self.gazozEtiket.place(x=5,y=250)

        self.gazozEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.gazozEntry.insert(0,"0")
        self.gazozEntry.place(x=180,y=255)
        self.gazozArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.gazozEntry, "arttir"))
        self.gazozArttir.place(x=155,y=255)
        self.gazozAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.gazozEntry, "azalt"))
        self.gazozAzalt.place(x=220,y=255)

        self.kolaEtiket=tk.Label(self.pencere,font=("Arial",13),text="Kola 4₺",bg="#22223b",foreground="#f2e9e4")
        self.kolaEtiket.place(x=5,y=300)

        self.kolaEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.kolaEntry.insert(0,"0")
        self.kolaEntry.place(x=180,y=305)
        self.kolaArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.kolaEntry, "arttir"))
        self.kolaArttir.place(x=155,y=305)
        self.kolaAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.kolaEntry, "azalt"))
        self.kolaAzalt.place(x=220,y=305)

        self.sodaEtiket=tk.Label(self.pencere,font=("Arial",13),text="Soda 4₺",bg="#22223b",foreground="#f2e9e4")
        self.sodaEtiket.place(x=5,y=350)

        self.sodaEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.sodaEntry.insert(0,"0")
        self.sodaEntry.place(x=180,y=355)
        self.sodaArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.sodaEntry, "arttir"))
        self.sodaArttir.place(x=155,y=355)
        self.sodaAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.sodaEntry, "azalt"))
        self.sodaAzalt.place(x=220,y=355)

        self.meyveSuyuEtiket=tk.Label(self.pencere,font=("Arial",13),text="Meyve Suyu 4₺",bg="#22223b",foreground="#f2e9e4")
        self.meyveSuyuEtiket.place(x=5,y=400)

        self.meyveSuyuEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.meyveSuyuEntry.insert(0,"0")
        self.meyveSuyuEntry.place(x=180,y=405)
        self.meyveSuyuArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.meyveSuyuEntry, "arttir"))
        self.meyveSuyuArttir.place(x=155,y=405)
        self.meyveSuyuAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.meyveSuyuEntry, "azalt"))
        self.meyveSuyuAzalt.place(x=220,y=405)

        self.ıhlamurEtiket=tk.Label(self.pencere,font=("Arial",13),text="Ihlamur 4₺",bg="#22223b",foreground="#f2e9e4")
        self.ıhlamurEtiket.place(x=5,y=450)

        self.ıhlamurEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.ıhlamurEntry.insert(0,"0")
        self.ıhlamurEntry.place(x=180,y=455)
        self.ıhlamurArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.ıhlamurEntry, "arttir"))
        self.ıhlamurArttir.place(x=155,y=455)
        self.ıhlamurAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.ıhlamurEntry, "azalt"))
        self.ıhlamurAzalt.place(x=220,y=455)

        self.cikolatalıSutEtiket=tk.Label(self.pencere,font=("Arial",13),text="Çikolatalı Süt 4₺",bg="#22223b",foreground="#f2e9e4")
        self.cikolatalıSutEtiket.place(x=5,y=500)

        self.cikolatalıSutEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.cikolatalıSutEntry.insert(0,"0")
        self.cikolatalıSutEntry.place(x=180,y=505)
        self.cikolatalıSutArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.cikolatalıSutEntry, "arttir"))
        self.cikolatalıSutArttir.place(x=155,y=505)
        self.cikolatalıSutAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.cikolatalıSutEntry, "azalt"))
        self.cikolatalıSutAzalt.place(x=220,y=505)

    # yemeklerin oluşturulduğu fonksiyon
    def yemekOlustur(self):
        # yemeklerin başlığı
        self.yemekEtiket=tk.Label(self.pencere,font=("Arial",20,'bold','underline'),text="Yemekler",bg="#22223b",foreground="#f2e9e4")
        self.yemekEtiket.place(x=270,y=50)
        self.tavukEtiket=tk.Label(self.pencere,font=("Arial",13),text="Tavuk 10₺",bg="#22223b",foreground="#f2e9e4")
        self.tavukEtiket.place(x=270,y=100)

        self.tavukEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.tavukEntry.insert(0,"0")
        self.tavukEntry.place(x=485,y=105)
        self.tavukArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.tavukEntry, "arttir"))
        self.tavukArttir.place(x=460,y=105)
        self.tavukAzaalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.tavukEntry, "azalt"))
        self.tavukAzaalt.place(x=525,y=105)

        self.kofteEtiket=tk.Label(self.pencere,font=("Arial",13),text="Köfte 10₺",bg="#22223b",foreground="#f2e9e4")
        self.kofteEtiket.place(x=270,y=150)

        self.kofteEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.kofteEntry.insert(0,"0")
        self.kofteEntry.place(x=485,y=155)
        self.kofteArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.kofteEntry, "arttir"))
        self.kofteArttir.place(x=460,y=155)
        self.kofteAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.kofteEntry, "azalt"))
        self.kofteAzalt.place(x=525,y=155)

        self.kuruFasulyeEtiket=tk.Label(self.pencere,font=("Arial",13),text="Kuru Fasulye 10₺",bg="#22223b",foreground="#f2e9e4")
        self.kuruFasulyeEtiket.place(x=270,y=200)

        self.kuruFasulyeEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.kuruFasulyeEntry.insert(0,"0")
        self.kuruFasulyeEntry.place(x=485,y=205)
        self.kuruFasulyeArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.kuruFasulyeEntry, "arttir"))
        self.kuruFasulyeArttir.place(x=460,y=205)
        self.kuruFasulyeAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.kuruFasulyeEntry, "azalt"))
        self.kuruFasulyeAzalt.place(x=525,y=205)

        self.mercimekEtiket=tk.Label(self.pencere,font=("Arial",13),text="Mercimek Çorbası 10₺",bg="#22223b",foreground="#f2e9e4")
        self.mercimekEtiket.place(x=270,y=250)

        self.mercimekEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.mercimekEntry.insert(0,"0")
        self.mercimekEntry.place(x=485,y=255)
        self.mercimekArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.mercimekEntry, "arttir"))
        self.mercimekArttir.place(x=460,y=255)
        self.mercimekAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.mercimekEntry, "azalt"))
        self.mercimekAzalt.place(x=525,y=255)

        self.yaylaEtiket=tk.Label(self.pencere,font=("Arial",13),text="Yayla Çorbası 10₺",bg="#22223b",foreground="#f2e9e4")
        self.yaylaEtiket.place(x=270,y=300)

        self.yaylaEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.yaylaEntry.insert(0,"0")
        self.yaylaEntry.place(x=485,y=305)
        self.yaylaArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.yaylaEntry, "arttir"))
        self.yaylaArttir.place(x=460,y=305)
        self.yaylaAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.yaylaEntry, "azalt"))
        self.yaylaAzalt.place(x=525,y=305)

        self.pilavEtiket=tk.Label(self.pencere,font=("Arial",13),text="Pilav 10₺",bg="#22223b",foreground="#f2e9e4")
        self.pilavEtiket.place(x=270,y=350)

        self.pilavEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.pilavEntry.insert(0,"0")
        self.pilavEntry.place(x=485,y=355)
        self.pilavArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.pilavEntry, "arttir"))
        self.pilavArttir.place(x=460,y=355)
        self.pilavAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.pilavEntry, "azalt"))
        self.pilavAzalt.place(x=525,y=355)

        self.makarnaEtiket=tk.Label(self.pencere,font=("Arial",13),text="Makarna 10₺",bg="#22223b",foreground="#f2e9e4")
        self.makarnaEtiket.place(x=270,y=400)

        self.makarnaEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.makarnaEntry.insert(0,"0")
        self.makarnaEntry.place(x=485,y=405)
        self.makarnaArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.makarnaEntry, "arttir"))
        self.makarnaArttir.place(x=460,y=405)
        self.makarnaAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.makarnaEntry, "azalt"))
        self.makarnaAzalt.place(x=525,y=405)

        self.patatesEtiket=tk.Label(self.pencere,font=("Arial",13),text="Patates kızartması 10₺",bg="#22223b",foreground="#f2e9e4")
        self.patatesEtiket.place(x=270,y=450)

        self.patatesEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.patatesEntry.insert(0,"0")
        self.patatesEntry.place(x=485,y=455)
        self.patatesArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.patatesEntry, "arttir"))
        self.patatesArttir.place(x=460,y=455)
        self.patatesAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.patatesEntry, "azalt"))
        self.patatesAzalt.place(x=525,y=455)

        self.tostEtiket=tk.Label(self.pencere,font=("Arial",13),text="Tost 10₺",bg="#22223b",foreground="#f2e9e4")
        self.tostEtiket.place(x=270,y=500)

        self.tostEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.tostEntry.insert(0,"0")
        self.tostEntry.place(x=485,y=505)
        self.tostArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.tostEntry, "arttir"))
        self.tostArttir.place(x=460,y=505)
        self.tostAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.tostEntry, "azalt"))
        self.tostAzalt.place(x=525,y=505)


    # tatlıların oluştulduğu fonksiyon
    def tatliOlustur(self):
        # tatlıların başlığı
        self.tatliBaslik=tk.Label(self.pencere,font=("Arial",20,'bold','underline'),text="Tatlılar",bg="#22223b",foreground="#f2e9e4")
        self.tatliBaslik.place(x=600,y=50)
        self.kazandibiEtiket=tk.Label(self.pencere,font=("Arial",13),text="Kazandibi 5₺",bg="#22223b",foreground="#f2e9e4")
        self.kazandibiEtiket.place(x=600,y=100)

        self.kazandibiEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.kazandibiEntry.insert(0,"0")
        self.kazandibiEntry.place(x=765,y=105)
        self.kazandibiArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.kazandibiEntry, "arttir"))
        self.kazandibiArttir.place(x=740,y=105)
        self.kazandibiAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.kazandibiEntry, "azalt"))
        self.kazandibiAzalt.place(x=805,y=105)
        

        self.baklavasEtiket=tk.Label(self.pencere,font=("Arial",13),text="Baklava 5₺",bg="#22223b",foreground="#f2e9e4")
        self.baklavasEtiket.place(x=600,y=150)

        self.baklavaEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.baklavaEntry.insert(0,"0")
        self.baklavaEntry.place(x=765,y=155)
        self.baklavaArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.baklavaEntry, "arttir"))
        self.baklavaArttir.place(x=740,y=155)
        self.baklavaAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.baklavaEntry, "azalt"))
        self.baklavaAzalt.place(x=805,y=155)

        self.kunefeEtiket=tk.Label(self.pencere,font=("Arial",13),text="Künefe 5₺",bg="#22223b",foreground="#f2e9e4")
        self.kunefeEtiket.place(x=600,y=200)

        self.kunefeEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.kunefeEntry.insert(0,"0")
        self.kunefeEntry.place(x=765,y=205)
        self.kunefeArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.kunefeEntry, "arttir"))
        self.kunefeArttir.place(x=740,y=205)
        self.kunefeAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.kunefeEntry, "azalt"))
        self.kunefeAzalt.place(x=805,y=205)

        self.profiterolEtiket=tk.Label(self.pencere,font=("Arial",13),text="Profiterol 5₺",bg="#22223b",foreground="#f2e9e4")
        self.profiterolEtiket.place(x=600,y=250)

        self.profiterolEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.profiterolEntry.insert(0,"0")
        self.profiterolEntry.place(x=765,y=255)
        self.profiterolArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda: self.miktar_degistir(self.profiterolEntry, "arttir"))
        self.profiterolArttir.place(x=740,y=250)
        self.profiterolAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda: self.miktar_degistir(self.profiterolEntry, "azalt"))
        self.profiterolAzalt.place(x=805,y=250)
    
    # miktar değiştirme fonksiyonu
    def miktar_degistir(self, entry, islem):
        mevcut_deger = int(entry.get())

        # Eğer işlem azaltma ise ve mevcut değer zaten 0 ise uyarı ver ve işlemi sonlandır
        if islem == "azalt" and mevcut_deger <= 0:
            messagebox.showwarning("Uyarı", "Miktar 0'ın altına düşemez!")
            return

        # Yeni değeri hesapla
        yeni_deger = mevcut_deger + (1 if islem == "arttir" else -1)

        # Yeni değeri entry'ye yaz
        entry.delete(0, tk.END)
        entry.insert(0, str(yeni_deger))


    
    # hesapalam işleminin yapıldığı fonksiyon
    def hesapla(self):

        self.toplam=0
        self.toplam+=int(self.suEntry.get())*3
        self.toplam+=int(self.cayEntry.get())*5
        self.toplam+=int(self.kahveEntry.get())*7
        self.toplam+=int(self.gazozEntry.get())*5
        self.toplam+=int(self.kolaEntry.get())*5
        self.toplam+=int(self.sodaEntry.get())*5
        self.toplam+=int(self.sodaEntry.get())*5
        self.toplam+=int(self.meyveSuyuEntry.get())*5
        self.toplam+=int(self.ıhlamurEntry.get())*5
        self.toplam+=int(self.cikolatalıSutEntry.get())*5
        # self.toplam+=int(self.turkKahvesiEntry.get())*5
        # self.toplam+=int(self.ayranEntry.get())*5

        self.toplam+=int(self.tavukEntry.get())*10
        self.toplam+=int(self.kofteEntry.get())*10
        self.toplam+=int(self.kuruFasulyeEntry.get())*10
        self.toplam+=int(self.mercimekEntry.get())*10
        self.toplam+=int(self.yaylaEntry.get())*10
        self.toplam+=int(self.pilavEntry.get())*10
        self.toplam+=int(self.makarnaEntry.get())*10
        self.toplam+=int(self.patatesEntry.get())*10
        self.toplam+=int(self.tostEntry.get())*10
        # self.toplam+=int(self.sandvicEntry.get())*10

        self.toplam+=int(self.kazandibiEntry.get())*5
        self.toplam+=int(self.baklavaEntry.get())*5
        self.toplam+=int(self.kunefeEntry.get())*5
        self.toplam+=int(self.profiterolEntry.get())*5

        self.hesapButonu=tk.Button(self.pencere,bg="#22223b",fg="white",text="Hesapla",command=self.hesapla)
        self.hesapButonu.place(x=600,y=300)
        self.toplamEtiket=tk.Label(self.pencere,font=("Arial",13),text="Toplam Tutar: "+str(self.toplam)+"₺",bg="#22223b",foreground="#f2e9e4")
        self.toplamEtiket.place(x=700,y=300)
        self.fisButonu=tk.Button(self.pencere,bg="#22223b",fg="white",text="Fiş Yazdır",font=("Arial",20,'bold'),command=self.yazdirr,height=3,width=15)
        self.fisButonu.place(x=600,y=400)


    # arttırma ve azaltma işlemlerinin yapıldığı fonksiyonlar
    def miktar_degistir(self, entry, islem):
        mevcut_deger = entry.get()
        yeni_deger = int(mevcut_deger) + (1 if islem == "arttir" else -1)

        entry.delete(0, tk.END)
        entry.insert(0, str(yeni_deger))

    # girilen masanın değerini yazdırma
    def masaDegerYazdir(self):
        self.girilenDeger = self.masaNo.cget('text')
        self.masaNoEtiket.config(text=self.girilenDeger)

    def masalar(self):
        self.secilenMasa = tk.StringVar()
        self.masaSecYazi=tk.Button(self.pencere,font=("Arial",10),text="masa seç ",command=self.masaDegerYazdir,bg="#22223b",fg="white")
        self.masaSecYazi.place(x=600,y=350)
        self.masaNoSecim = [str(i) for i in range(0,21)]
        self.masaNo = tk.OptionMenu(self.pencere, self.secilenMasa, *self.masaNoSecim)
        self.masaNo.config(bg="#22223b",fg="white")
        self.masaNo.place(x=750,y=348,width=50,height=25)
        # self.masaNo = tk.Entry(self.pencere,bg="#c9ada7")
        # self.masaNo.place(x=750,y=348,width=50,height=25)
        # self.toplamEtiket=tk.Label(self.pencere,font=("Arial",13),text="Toplam Tutar: "+str(self.toplam)+"TL",bg="#22223b")
        self.masaNoEtiket = tk.Label(self.pencere,font=("Arial",13),bg="#22223b")
    # toplam tutarı ve masa numarasını yazdırma
    def yazdirr(self):
        if self.masaNoEtiket.cget('text') == "":
            alert = messagebox.showerror("Hata", "Lütfen masa numarasını giriniz ve masa seç butonuna basınız")
        else:
            # eğer masaNoEtiket 0 ise paket şekliden dosyaya yazı yazdır
            if self.masaNoEtiket.cget('text') == "0":
                self.dosya = open("fis.txt","a",encoding="utf-8")
                self.dosya.write("\n--------------------------------------------------\n")
                self.dosya.write("Paket Sipariş\n")
                self.dosya.write(str(self.toplamEtiket.cget("text")))
                self.dosya.close()
                self.mesajPenceresi()
            else:
                self.dosya = open("fis.txt","a",encoding="utf-8")
                self.dosya.write("\n--------------------------------------------------\n")
                self.dosya.write("Masa no: "+str(self.masaNoEtiket.cget('text'))+"\n")
                self.dosya.write(str(self.toplamEtiket.cget("text")))
                self.dosya.close()
                self.mesajPenceresi()
    # üst menüleri oluşturma
    def yardim(self):
        # menüye yardım butonu ekleyeceğiz
        self.menu = tk.Menu(self.pencere, bg="#22223b", fg="white", activebackground="#c9ada7", activeforeground="black")
        self.pencere.config(menu=self.menu)
        self.yardimMenu = tk.Menu(self.menu, tearoff=0, bg="#22223b", fg="white", activebackground="#c9ada7", activeforeground="black")
        self.yardimMenu2 = tk.Menu(self.menu, tearoff=0, bg="#22223b", fg="white", activebackground="#c9ada7", activeforeground="black")
        self.menu.add_cascade(label="Yardım", menu=self.yardimMenu)
        self.menu.add_cascade(label="Fiş İşlemleri", menu=self.yardimMenu2)
        self.yardimMenu.add_command(label="Nasıl Kullanılır", command=self.yardimIcerik)
        self.yardimMenu.add_command(label="Hakkında", command=self.hakkinda)
        self.yardimMenu2.add_command(label="Fiş Oluştur", command=self.yazdirr)
        self.yardimMenu.add_separator()
        self.yardimMenu.add_command(label="Çıkış", command=self.pencere.quit)
        self.yardimMenu2.add_command(label="Fiş Geçmişini Göster", command=self.fisGecmisi)
    def hakkinda(self):
        # hakkında butonuna tıklandığında çalışacak fonksiyon
        self.hakkinda = tk.Toplevel(self.pencere)
        self.hakkinda.title("Hakkımda")
        self.hakkinda.geometry("300x100")
        self.hakkinda.resizable(False, False)
        self.hakkinda.config(bg="#22223b")
        self.hakkindaLabel = tk.Label(self.hakkinda, text="""
        Ad Soyad: Hamza ORTATEPE
        Okul: Ege Üniversitesi
        Bölüm: Bilgisayar Programcılığı
        Numara: 90210000172""",bg="#22223b",fg="white")
        self.hakkindaLabel.pack()
    def yardimIcerik(self):
        # yardım butonuna tıklandığında çalışacak fonksiyon
        self.yardim = tk.Toplevel(self.pencere)
        self.yardim.title("Yardım")
        self.yardim.geometry("500x150")
        self.yardim.resizable(False, False)
        self.yardim.config(bg="#22223b")
        self.yardimLabel = tk.Label(self.yardim, text="""Nasıl kullanılır?
        1. Sipariş edilen veya yenen yemeklerin adetini artırın veya el ile girin.
        2. Hesapla butonuna basarak hesaplayın.
        3. Masa no seçin.
        4. Masa seç butonuna basarak masayı seçin
        5. Yazdır butonuna basarak fiş yazdırın.
        Not: Yazdır butonuna bastığınızda masa numarası ve toplam tutar 
        fis.txt dosyasına kaydedilecektir.
        Eğer masa no yu 0 olarak seçerseniz paket olarak verilecektir.""",bg="#22223b",fg="white")
        self.yardimLabel.pack()
    # kapatma butonuna basılınca çalışacak fonksiyon
    def kapatButonu(self):
        if messagebox.askokcancel("Çıkış", "Çıkış yapılıyor kabul ediyor musun?"):
            self.pencere.destroy()
    # fiş oluşturulurken ekranda çıkan uyarı mesajı
    def mesajPenceresi(self):
        alert = messagebox.showinfo("Bilgi", "Fiş başarıyla oluşturuldu.\n fis.txt dosyasına kaydedildi.")
    def fisGecmisi(self):
        # fiş geçmişini göster butonuna tıklandığında çalışacak fonksiyon
        self.fisGecmisi = tk.Toplevel(self.pencere)
        self.fisGecmisi.title("Fiş Geçmişi")
        self.fisGecmisi.geometry("500x500")
        self.fisGecmisi.resizable(False, False)
        self.fisGecmisi.config(bg="#22223b")
        with open("fis.txt", "r",encoding="utf-8") as self.file:
            self.dosya_icerigi = self.file.readlines()
        # eğer dosya içeriği 12 satırdan az ise tüm satırları ekrana yazdır
        if len(self.dosya_icerigi) < 12:
            for satir in range(len(self.dosya_icerigi)):
                self.fisGecmisiLabel = tk.Label(self.fisGecmisi,text=self.dosya_icerigi[satir],bg="#22223b",fg="white")
                self.fisGecmisiLabel.pack()
        else:
            for satir in range(len(self.dosya_icerigi)-12,len(self.dosya_icerigi)):
                self.fisGecmisiLabel = tk.Label(self.fisGecmisi,text=self.dosya_icerigi[satir],bg="#22223b",fg="white")
                self.fisGecmisiLabel.pack()
    # daha önce fis.txt dosayı oluştulup oluşturulmadığını kontrol eden fonksiyon u yaz eğer oluşturulmamışsa oluşturuyor
    def dosyaKontrol(self):
        if os.path.exists("fis.txt"):
            print("Dosya var")
            pass
        else:
            with open("fis.txt", "w",encoding="utf-8") as self.file:
                self.file.write("")
                print("Dosya oluşturuldu")

restoran=Restoran()