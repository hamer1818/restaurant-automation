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
        self.arttir()
        self.azaltt()
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
        self.suArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.suArttirr)
        self.suArttir.place(x=155,y=105)
        self.suAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.suAzaltt)
        self.suAzalt.place(x=220,y=105)

        self.cayEtiket=tk.Label(self.pencere,font=("Arial",13),text="Çay 5₺",bg="#22223b",foreground="#f2e9e4")
        self.cayEtiket.place(x=5,y=150)

        self.cayEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.cayEntry.insert(0,"0")
        self.cayEntry.place(x=180,y=155)
        self.cayArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.cayArttirr)
        self.cayArttir.place(x=155,y=155)
        self.cayAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.cayAzaltt)
        self.cayAzalt.place(x=220,y=155)

        self.kahveEtiket=tk.Label(self.pencere,font=("Arial",13),text="Kahve 7₺",bg="#22223b",foreground="#f2e9e4")
        self.kahveEtiket.place(x=5,y=200)

        self.kahveEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.kahveEntry.insert(0,"0")
        self.kahveEntry.place(x=180,y=205)
        self.kahveArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.kahveArttirr)
        self.kahveArttir.place(x=155,y=205)
        self.kahveAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.kahveAzaltt)
        self.kahveAzalt.place(x=220,y=205)

        self.gazozEtiket=tk.Label(self.pencere,font=("Arial",13),text="Gazoz 4₺",bg="#22223b",foreground="#f2e9e4")
        self.gazozEtiket.place(x=5,y=250)

        self.gazozEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.gazozEntry.insert(0,"0")
        self.gazozEntry.place(x=180,y=255)
        self.gazozArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.gazozArttirr)
        self.gazozArttir.place(x=155,y=255)
        self.gazozAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.gazozAzaltt)
        self.gazozAzalt.place(x=220,y=255)

        self.kolaEtiket=tk.Label(self.pencere,font=("Arial",13),text="Kola 4₺",bg="#22223b",foreground="#f2e9e4")
        self.kolaEtiket.place(x=5,y=300)

        self.kolaEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.kolaEntry.insert(0,"0")
        self.kolaEntry.place(x=180,y=305)
        self.kolaArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.kolaArttirr)
        self.kolaArttir.place(x=155,y=305)
        self.kolaAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.kolaAzaltt)
        self.kolaAzalt.place(x=220,y=305)

        self.sodaEtiket=tk.Label(self.pencere,font=("Arial",13),text="Soda 4₺",bg="#22223b",foreground="#f2e9e4")
        self.sodaEtiket.place(x=5,y=350)

        self.sodaEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.sodaEntry.insert(0,"0")
        self.sodaEntry.place(x=180,y=355)
        self.sodaArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.sodaArttirr)
        self.sodaArttir.place(x=155,y=355)
        self.sodaAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.sodaAzaltt)
        self.sodaAzalt.place(x=220,y=355)

        self.meyveSuyuEtiket=tk.Label(self.pencere,font=("Arial",13),text="Meyve Suyu 4₺",bg="#22223b",foreground="#f2e9e4")
        self.meyveSuyuEtiket.place(x=5,y=400)

        self.meyveSuyuEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.meyveSuyuEntry.insert(0,"0")
        self.meyveSuyuEntry.place(x=180,y=405)
        self.meyveSuyuArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.meyveSuyuArttirr)
        self.meyveSuyuArttir.place(x=155,y=405)
        self.meyveSuyuAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.meyveSuyuAzaltt)
        self.meyveSuyuAzalt.place(x=220,y=405)

        self.ıhlamurEtiket=tk.Label(self.pencere,font=("Arial",13),text="Ihlamur 4₺",bg="#22223b",foreground="#f2e9e4")
        self.ıhlamurEtiket.place(x=5,y=450)

        self.ıhlamurEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.ıhlamurEntry.insert(0,"0")
        self.ıhlamurEntry.place(x=180,y=455)
        self.ıhlamurArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.ıhlamurArttirr)
        self.ıhlamurArttir.place(x=155,y=455)
        self.ıhlamurAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.ıhlamurAzaltt)
        self.ıhlamurAzalt.place(x=220,y=455)

        self.cikolatalıSutEtiket=tk.Label(self.pencere,font=("Arial",13),text="Çikolatalı Süt 4₺",bg="#22223b",foreground="#f2e9e4")
        self.cikolatalıSutEtiket.place(x=5,y=500)

        self.cikolatalıSutEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.cikolatalıSutEntry.insert(0,"0")
        self.cikolatalıSutEntry.place(x=180,y=505)
        self.cikolatalıSutArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.cikolatalıSutArttirr)
        self.cikolatalıSutArttir.place(x=155,y=505)
        self.cikolatalıSutAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.cikolatalıSutAzaltt)
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
        self.tavukArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.tavukArttirr)
        self.tavukArttir.place(x=460,y=105)
        self.tavukAzaalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.tavukAzaltt)
        self.tavukAzaalt.place(x=525,y=105)

        self.kofteEtiket=tk.Label(self.pencere,font=("Arial",13),text="Köfte 10₺",bg="#22223b",foreground="#f2e9e4")
        self.kofteEtiket.place(x=270,y=150)

        self.kofteEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.kofteEntry.insert(0,"0")
        self.kofteEntry.place(x=485,y=155)
        self.kofteArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.kofteArttirr)
        self.kofteArttir.place(x=460,y=155)
        self.kofteAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.kofteAzaltt)
        self.kofteAzalt.place(x=525,y=155)

        self.kuruFasulyeEtiket=tk.Label(self.pencere,font=("Arial",13),text="Kuru Fasulye 10₺",bg="#22223b",foreground="#f2e9e4")
        self.kuruFasulyeEtiket.place(x=270,y=200)

        self.kuruFasulyeEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.kuruFasulyeEntry.insert(0,"0")
        self.kuruFasulyeEntry.place(x=485,y=205)
        self.kuruFasulyeArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.kuruFasulyeArttirr)
        self.kuruFasulyeArttir.place(x=460,y=205)
        self.kuruFasulyeAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.kuruFasulyeAzaltt)
        self.kuruFasulyeAzalt.place(x=525,y=205)

        self.mercimekEtiket=tk.Label(self.pencere,font=("Arial",13),text="Mercimek Çorbası 10₺",bg="#22223b",foreground="#f2e9e4")
        self.mercimekEtiket.place(x=270,y=250)

        self.mercimekEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.mercimekEntry.insert(0,"0")
        self.mercimekEntry.place(x=485,y=255)
        self.mercimekArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.mercimekArttirr)
        self.mercimekArttir.place(x=460,y=255)
        self.mercimekAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.mercimekAzaltt)
        self.mercimekAzalt.place(x=525,y=255)

        self.yaylaEtiket=tk.Label(self.pencere,font=("Arial",13),text="Yayla Çorbası 10₺",bg="#22223b",foreground="#f2e9e4")
        self.yaylaEtiket.place(x=270,y=300)

        self.yaylaEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.yaylaEntry.insert(0,"0")
        self.yaylaEntry.place(x=485,y=305)
        self.yaylaArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.yaylaArttirr)
        self.yaylaArttir.place(x=460,y=305)
        self.yaylaAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.yaylaAzaltt)
        self.yaylaAzalt.place(x=525,y=305)

        self.pilavEtiket=tk.Label(self.pencere,font=("Arial",13),text="Pilav 10₺",bg="#22223b",foreground="#f2e9e4")
        self.pilavEtiket.place(x=270,y=350)

        self.pilavEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.pilavEntry.insert(0,"0")
        self.pilavEntry.place(x=485,y=355)
        self.pilavArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.pilavArttirr)
        self.pilavArttir.place(x=460,y=355)
        self.pilavAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.pilavAzaltt)
        self.pilavAzalt.place(x=525,y=355)

        self.makarnaEtiket=tk.Label(self.pencere,font=("Arial",13),text="Makarna 10₺",bg="#22223b",foreground="#f2e9e4")
        self.makarnaEtiket.place(x=270,y=400)

        self.makarnaEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.makarnaEntry.insert(0,"0")
        self.makarnaEntry.place(x=485,y=405)
        self.makarnaArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.makarnaArttirr)
        self.makarnaArttir.place(x=460,y=405)
        self.makarnaAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.makarnaAzaltt)
        self.makarnaAzalt.place(x=525,y=405)

        self.patatesEtiket=tk.Label(self.pencere,font=("Arial",13),text="Patates kızartması 10₺",bg="#22223b",foreground="#f2e9e4")
        self.patatesEtiket.place(x=270,y=450)

        self.patatesEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.patatesEntry.insert(0,"0")
        self.patatesEntry.place(x=485,y=455)
        self.patatesArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.patatesArttirr)
        self.patatesArttir.place(x=460,y=455)
        self.patatesAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.patatesAzaltt)
        self.patatesAzalt.place(x=525,y=455)

        self.tostEtiket=tk.Label(self.pencere,font=("Arial",13),text="Tost 10₺",bg="#22223b",foreground="#f2e9e4")
        self.tostEtiket.place(x=270,y=500)

        self.tostEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.tostEntry.insert(0,"0")
        self.tostEntry.place(x=485,y=505)
        self.tostArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.tostArttirr)
        self.tostArttir.place(x=460,y=505)
        self.tostAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.tostAzaltt)
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
        self.kazandibiArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.kazandibiArttirr)
        self.kazandibiArttir.place(x=740,y=105)
        self.kazandibiAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.kazandibiAzaltt)
        self.kazandibiAzalt.place(x=805,y=105)
        

        self.baklavasEtiket=tk.Label(self.pencere,font=("Arial",13),text="Baklava 5₺",bg="#22223b",foreground="#f2e9e4")
        self.baklavasEtiket.place(x=600,y=150)

        self.baklavaEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.baklavaEntry.insert(0,"0")
        self.baklavaEntry.place(x=765,y=155)
        self.baklavaArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.baklavaArttirr)
        self.baklavaArttir.place(x=740,y=155)
        self.baklavaAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.baklavaAzaltt)
        self.baklavaAzalt.place(x=805,y=155)

        self.kunefeEtiket=tk.Label(self.pencere,font=("Arial",13),text="Künefe 5₺",bg="#22223b",foreground="#f2e9e4")
        self.kunefeEtiket.place(x=600,y=200)

        self.kunefeEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.kunefeEntry.insert(0,"0")
        self.kunefeEntry.place(x=765,y=205)
        self.kunefeArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.kunefeArttirr)
        self.kunefeArttir.place(x=740,y=205)
        self.kunefeAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.kunefeAzaltt)
        self.kunefeAzalt.place(x=805,y=205)

        self.profiterolEtiket=tk.Label(self.pencere,font=("Arial",13),text="Profiterol 5₺",bg="#22223b",foreground="#f2e9e4")
        self.profiterolEtiket.place(x=600,y=250)

        self.profiterolEntry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
        self.profiterolEntry.insert(0,"0")
        self.profiterolEntry.place(x=765,y=255)
        self.profiterolArttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=self.profiterolArttirr)
        self.profiterolArttir.place(x=740,y=250)
        self.profiterolAzalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=self.profiterolAzaltt)
        self.profiterolAzalt.place(x=805,y=250)
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
    def suArttirr(self):
        self.arttırılmışSu=self.suEntry.get()
        self.yeniSu=int(self.arttırılmışSu)+1

        self.suEntry.delete(0,tk.END)
        self.suEntry.insert(0,str(self.yeniSu))
    def cayArttirr(self):
        self.arttırılmışCay=self.cayEntry.get()
        self.yeniCay=int(self.arttırılmışCay)+1

        self.cayEntry.delete(0,tk.END)
        self.cayEntry.insert(0,str(self.yeniCay))
    def kahveArttirr(self):
        self.arttırılmışKahve=self.kahveEntry.get()
        self.yeniKahve=int(self.arttırılmışKahve)+1

        self.kahveEntry.delete(0,tk.END)
        self.kahveEntry.insert(0,str(self.yeniKahve))
    def gazozArttirr(self):
        self.arttırılmışGazoz=self.gazozEntry.get()
        self.yeniGazoz=int(self.arttırılmışGazoz)+1

        self.gazozEntry.delete(0,tk.END)
        self.gazozEntry.insert(0,str(self.yeniGazoz))
    def kolaArttirr(self):
        self.arttırılmışKola=self.kolaEntry.get()
        self.yeniKola=int(self.arttırılmışKola)+1

        self.kolaEntry.delete(0,tk.END)
        self.kolaEntry.insert(0,str(self.yeniKola))
    def sodaArttirr(self):
        self.arttırılmışSoda=self.sodaEntry.get()
        self.yeniSoda=int(self.arttırılmışSoda)+1

        self.sodaEntry.delete(0,tk.END)
        self.sodaEntry.insert(0,str(self.yeniSoda))
    def meyveSuyuArttirr(self):
        self.arttırılmışMeyveSuyu=self.meyveSuyuEntry.get()
        self.yeniMeyveSuyu=int(self.arttırılmışMeyveSuyu)+1

        self.meyveSuyuEntry.delete(0,tk.END)
        self.meyveSuyuEntry.insert(0,str(self.yeniMeyveSuyu))
    def ıhlamurArttirr(self):
        self.arttırılmışIhlamur=self.ıhlamurEntry.get()
        self.yeniIhlamur=int(self.arttırılmışIhlamur)+1

        self.ıhlamurEntry.delete(0,tk.END)
        self.ıhlamurEntry.insert(0,str(self.yeniIhlamur))
    def cikolatalıSutArttirr(self):
        self.arttırılmışCikolatalıSut=self.cikolatalıSutEntry.get()
        self.yeniCikolatalıSut=int(self.arttırılmışCikolatalıSut)+1

        self.cikolatalıSutEntry.delete(0,tk.END)
        self.cikolatalıSutEntry.insert(0,str(self.yeniCikolatalıSut))

    def tavukArttirr(self):
        self.arttırılmışTavuk=self.tavukEntry.get()
        self.yeniTavuk=int(self.arttırılmışTavuk)+1

        self.tavukEntry.delete(0,tk.END)
        self.tavukEntry.insert(0,str(self.yeniTavuk))
    def kofteArttirr(self):
        self.arttırılmışKofte=self.kofteEntry.get()
        self.yeniKofte=int(self.arttırılmışKofte)+1

        self.kofteEntry.delete(0,tk.END)
        self.kofteEntry.insert(0,str(self.yeniKofte))
    def kuruFasulyeArttirr(self):
        self.arttırılmışKuruFasulye=self.kuruFasulyeEntry.get()
        self.yeniKuruFasulye=int(self.arttırılmışKuruFasulye)+1

        self.kuruFasulyeEntry.delete(0,tk.END)
        self.kuruFasulyeEntry.insert(0,str(self.yeniKuruFasulye))
    def mercimekArttirr(self):
        self.arttırılmışMercimek=self.mercimekEntry.get()
        self.yeniMercimek=int(self.arttırılmışMercimek)+1

        self.mercimekEntry.delete(0,tk.END)
        self.mercimekEntry.insert(0,str(self.yeniMercimek))
    def yaylaArttirr(self):
        self.arttırılmışYayla=self.yaylaEntry.get()
        self.yeniYayla=int(self.arttırılmışYayla)+1

        self.yaylaEntry.delete(0,tk.END)
        self.yaylaEntry.insert(0,str(self.yeniYayla))
    def pilavArttirr(self):
        self.arttırılmışPilav=self.pilavEntry.get()
        self.yeniPilav=int(self.arttırılmışPilav)+1

        self.pilavEntry.delete(0,tk.END)
        self.pilavEntry.insert(0,str(self.yeniPilav))
    def makarnaArttirr(self):
        self.arttırılmışMakarna=self.makarnaEntry.get()
        self.yeniMakarna=int(self.arttırılmışMakarna)+1

        self.makarnaEntry.delete(0,tk.END)
        self.makarnaEntry.insert(0,str(self.yeniMakarna))
    def patatesArttirr(self):
        self.arttırılmışPatates=self.patatesEntry.get()
        self.yeniPatates=int(self.arttırılmışPatates)+1

        self.patatesEntry.delete(0,tk.END)
        self.patatesEntry.insert(0,str(self.yeniPatates))
    def tostArttirr(self):
        self.arttırılmışTost=self.tostEntry.get()
        self.yeniTost=int(self.arttırılmışTost)+1

        self.tostEntry.delete(0,tk.END)
        self.tostEntry.insert(0,str(self.yeniTost))

    def kazandibiArttirr(self):
        self.arttırılmışKazandibi=self.kazandibiEntry.get()
        self.yeniKazandibi=int(self.arttırılmışKazandibi)+1

        self.kazandibiEntry.delete(0,tk.END)
        self.kazandibiEntry.insert(0,str(self.yeniKazandibi))
    def baklavaArttirr(self):
        self.arttırılmışBaklava=self.baklavaEntry.get()
        self.yeniBaklava=int(self.arttırılmışBaklava)+1

        self.baklavaEntry.delete(0,tk.END)
        self.baklavaEntry.insert(0,str(self.yeniBaklava))
    def kunefeArttirr(self):
        self.arttırılmışKunefe=self.kunefeEntry.get()
        self.yeniKunefe=int(self.arttırılmışKunefe)+1

        self.kunefeEntry.delete(0,tk.END)
        self.kunefeEntry.insert(0,str(self.yeniKunefe))
    def profiterolArttirr(self):
        self.arttırılmışProfiterol=self.profiterolEntry.get()
        self.yeniProfiterol=int(self.arttırılmışProfiterol)+1

        self.profiterolEntry.delete(0,tk.END)
        self.profiterolEntry.insert(0,str(self.yeniProfiterol))
    def arttir(self):
        self.suArttirr()
        self.cayArttirr()
        self.kahveArttirr()
        self.gazozArttirr()
        self.kolaArttirr()
        self.sodaArttirr()
        self.meyveSuyuArttirr()
        self.ıhlamurArttirr()
        self.cikolatalıSutArttirr()
        # self.turkKahvesiArttirr()
        # self.ayranArttirr()
        self.tavukArttirr()
        self.kofteArttirr()
        self.kuruFasulyeArttirr()
        self.mercimekArttirr()
        self.yaylaArttirr()
        self.pilavArttirr()
        self.makarnaArttirr()
        self.patatesArttirr()
        self.tostArttirr()
        # self.sandvicArttirr()
        self.kazandibiArttirr()
        self.baklavaArttirr()
        self.kunefeArttirr()
        self.profiterolArttirr()
    def suAzaltt(self):
        self.azaltılmışSu=self.suEntry.get()
        self.yeniSu=int(self.azaltılmışSu)-1

        self.suEntry.delete(0,tk.END)
        self.suEntry.insert(0,str(self.yeniSu))
    def cayAzaltt(self):
        self.azaltılmışCay=self.cayEntry.get()
        self.yeniCay=int(self.azaltılmışCay)-1

        self.cayEntry.delete(0,tk.END)
        self.cayEntry.insert(0,str(self.yeniCay))
    def kahveAzaltt(self):
        self.azaltılmışKahve=self.kahveEntry.get()
        self.yeniKahve=int(self.azaltılmışKahve)-1

        self.kahveEntry.delete(0,tk.END)
        self.kahveEntry.insert(0,str(self.yeniKahve))
    def gazozAzaltt(self):
        self.azaltılmışGazoz=self.gazozEntry.get()
        self.yeniGazoz=int(self.azaltılmışGazoz)-1

        self.gazozEntry.delete(0,tk.END)
        self.gazozEntry.insert(0,str(self.yeniGazoz))
    def kolaAzaltt(self):
        self.azaltılmışKola=self.kolaEntry.get()
        self.yeniKola=int(self.azaltılmışKola)-1

        self.kolaEntry.delete(0,tk.END)
        self.kolaEntry.insert(0,str(self.yeniKola))
    def sodaAzaltt(self):
        self.azaltılmışSoda=self.sodaEntry.get()
        self.yeniSoda=int(self.azaltılmışSoda)-1

        self.sodaEntry.delete(0,tk.END)
        self.sodaEntry.insert(0,str(self.yeniSoda))
    def meyveSuyuAzaltt(self):
        self.azaltılmışMeyveSuyu=self.meyveSuyuEntry.get()
        self.yeniMeyveSuyu=int(self.azaltılmışMeyveSuyu)-1

        self.meyveSuyuEntry.delete(0,tk.END)
        self.meyveSuyuEntry.insert(0,str(self.yeniMeyveSuyu))
    def ıhlamurAzaltt(self):
        self.azaltılmışIhlamur=self.ıhlamurEntry.get()
        self.yeniIhlamur=int(self.azaltılmışIhlamur)-1

        self.ıhlamurEntry.delete(0,tk.END)
        self.ıhlamurEntry.insert(0,str(self.yeniIhlamur))
    def cikolatalıSutAzaltt(self):
        self.azaltılmışCikolatalıSut=self.cikolatalıSutEntry.get()
        self.yeniCikolatalıSut=int(self.azaltılmışCikolatalıSut)-1

        self.cikolatalıSutEntry.delete(0,tk.END)
        self.cikolatalıSutEntry.insert(0,str(self.yeniCikolatalıSut))

    def tavukAzaltt(self):
        self.azaltılmışTavuk=self.tavukEntry.get()
        self.yeniTavuk=int(self.azaltılmışTavuk)-1

        self.tavukEntry.delete(0,tk.END)
        self.tavukEntry.insert(0,str(self.yeniTavuk))
    def kofteAzaltt(self):
        self.azaltılmışKofte=self.kofteEntry.get()
        self.yeniKofte=int(self.azaltılmışKofte)-1

        self.kofteEntry.delete(0,tk.END)
        self.kofteEntry.insert(0,str(self.yeniKofte))
    def kuruFasulyeAzaltt(self):
        self.azaltılmışKuruFasulye=self.kuruFasulyeEntry.get()
        self.yeniKuruFasulye=int(self.azaltılmışKuruFasulye)-1

        self.kuruFasulyeEntry.delete(0,tk.END)
        self.kuruFasulyeEntry.insert(0,str(self.yeniKuruFasulye))
    def mercimekAzaltt(self):
        self.azaltılmışMercimek=self.mercimekEntry.get()
        self.yeniMercimek=int(self.azaltılmışMercimek)-1

        self.mercimekEntry.delete(0,tk.END)
        self.mercimekEntry.insert(0,str(self.yeniMercimek))
    def yaylaAzaltt(self):
        self.azaltılmışYayla=self.yaylaEntry.get()
        self.yeniYayla=int(self.azaltılmışYayla)-1

        self.yaylaEntry.delete(0,tk.END)
        self.yaylaEntry.insert(0,str(self.yeniYayla))
    def pilavAzaltt(self):
        self.azaltılmışPilav=self.pilavEntry.get()
        self.yeniPilav=int(self.azaltılmışPilav)-1

        self.pilavEntry.delete(0,tk.END)
        self.pilavEntry.insert(0,str(self.yeniPilav))
    def makarnaAzaltt(self):
        self.azaltılmışMakarna=self.makarnaEntry.get()
        self.yeniMakarna=int(self.azaltılmışMakarna)-1

        self.makarnaEntry.delete(0,tk.END)
        self.makarnaEntry.insert(0,str(self.yeniMakarna))
    def patatesAzaltt(self):
        self.azaltılmışPatates=self.patatesEntry.get()
        self.yeniPatates=int(self.azaltılmışPatates)-1

        self.patatesEntry.delete(0,tk.END)
        self.patatesEntry.insert(0,str(self.yeniPatates))
    def tostAzaltt(self):
        self.azaltılmışTost=self.tostEntry.get()
        self.yeniTost=int(self.azaltılmışTost)-1

        self.tostEntry.delete(0,tk.END)
        self.tostEntry.insert(0,str(self.yeniTost))

    def kazandibiAzaltt(self):
        self.azaltılmışKazandibi=self.kazandibiEntry.get()
        self.yeniKazandibi=int(self.azaltılmışKazandibi)-1

        self.kazandibiEntry.delete(0,tk.END)
        self.kazandibiEntry.insert(0,str(self.yeniKazandibi))
    def baklavaAzaltt(self):
        self.azaltılmışBaklava=self.baklavaEntry.get()
        self.yeniBaklava=int(self.azaltılmışBaklava)-1

        self.baklavaEntry.delete(0,tk.END)
        self.baklavaEntry.insert(0,str(self.yeniBaklava))
    def kunefeAzaltt(self):
        self.azaltılmışKunefe=self.kunefeEntry.get()
        self.yeniKunefe=int(self.azaltılmışKunefe)-1

        self.kunefeEntry.delete(0,tk.END)
        self.kunefeEntry.insert(0,str(self.yeniKunefe))
    def profiterolAzaltt(self):
        self.azaltılmışProfiterol=self.profiterolEntry.get()
        self.yeniProfiterol=int(self.azaltılmışProfiterol)-1

        self.profiterolEntry.delete(0,tk.END)
        self.profiterolEntry.insert(0,str(self.yeniProfiterol))
    def azaltt(self):
        self.suAzaltt()
        self.cayAzaltt()
        self.kahveAzaltt()
        self.gazozAzaltt()
        self.kolaAzaltt()
        self.sodaAzaltt()
        self.meyveSuyuAzaltt()
        self.ıhlamurAzaltt()
        self.cikolatalıSutAzaltt()
        # self.turkKahvesiAzaltt()
        # self.ayranAzaltt()
        self.tavukAzaltt()
        self.kofteAzaltt()
        self.kuruFasulyeAzaltt()
        self.mercimekAzaltt()
        self.yaylaAzaltt()
        self.pilavAzaltt()
        self.makarnaAzaltt()
        self.patatesAzaltt()
        self.tostAzaltt()
        # self.sandvicAzaltt()
        self.kazandibiAzaltt()
        self.baklavaAzaltt()
        self.kunefeAzaltt()
        self.profiterolAzaltt()
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