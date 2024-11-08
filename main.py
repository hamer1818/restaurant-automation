import tkinter as tk
from tkinter import messagebox
import os

class Restoran:
    def __init__(self):
        self.pencere=tk.Tk()
        self.pencere.title("Restoran Otomasyon Uygulaması v1.0")
        self.pencere.config(bg="#22223b")
        self.pencere.protocol("WM_DELETE_WINDOW",self.kapatButonu)
        self.pencere.geometry("900x550")
        self.pencere.resizable(False,False)
        self.dosyaKontrol()
        self.urunleriOlustur()
        self.baslik()
        self.masalar()
        self.masaDegerYazdir()
        self.hesapla()
        self.yardim()
        self.pencere.mainloop()

    def baslik(self):
        self.uygulamaIsim=tk.Label(self.pencere,text="Restoran Otomasyonu",bg="#22223b",font=("Arial",30,'bold'),foreground="#f2e9e4")
        self.uygulamaIsim.pack(side="top")

    def urunleriOlustur(self):
        self.urunler = {
            'İçecekler': [
                ('Su', 3),
                ('Çay', 5),
                ('Kahve', 7),
                ('Gazoz', 4),
                ('Kola', 4),
                ('Soda', 4),
                ('Meyve Suyu', 4),
                ('Ihlamur', 4),
                ('Çikolatalı Süt', 4)
            ],
            'Yemekler': [
                ('Tavuk', 10),
                ('Köfte', 10),
                ('Kuru Fasulye', 10),
                ('Mercimek Çorbası', 10),
                ('Yayla Çorbası', 10),
                ('Pilav', 10),
                ('Makarna', 10),
                ('Patates Kızartması', 10),
                ('Tost', 10)
            ],
            'Tatlılar': [
                ('Kazandibi', 5),
                ('Baklava', 5),
                ('Künefe', 5),
                ('Profiterol', 5)
            ]
        }

        x_offsets = {'İçecekler': 5, 'Yemekler': 270, 'Tatlılar': 600}
        for kategori, urunler in self.urunler.items():
            baslik=tk.Label(self.pencere,text=kategori,bg="#22223b",font=("Arial",20,'bold','underline'),foreground="#f2e9e4")
            baslik.place(x=x_offsets[kategori],y=50)
            y = 100
            for urun, fiyat in urunler:
                etiket=tk.Label(self.pencere,font=("Arial",13),text=f"{urun} {fiyat}₺",bg="#22223b",foreground="#f2e9e4")
                etiket.place(x=x_offsets[kategori], y=y)

                entry=tk.Entry(self.pencere,bg="#c9ada7",width=5)
                entry.insert(0,"0")
                entry.place(x=x_offsets[kategori]+175, y=y+5)

                arttir=tk.Button(self.pencere,bg="#22223b",fg="white",text="+",command=lambda e=entry: self.miktar_degistir(e, "arttir"))
                arttir.place(x=x_offsets[kategori]+150, y=y+5)

                azalt=tk.Button(self.pencere,bg="#22223b",fg="white",text="-",command=lambda e=entry: self.miktar_degistir(e, "azalt"))
                azalt.place(x=x_offsets[kategori]+215, y=y+5)

                # Entry widget'ları saklıyoruz
                if not hasattr(self, 'urun_entries'):
                    self.urun_entries = {}
                self.urun_entries[urun] = (entry, fiyat)
                y += 50

    def miktar_degistir(self, entry, islem):
        mevcut_deger = int(entry.get())
        if islem == "azalt" and mevcut_deger <= 0:
            messagebox.showwarning("Uyarı", "Miktar 0'ın altına düşemez!")
            return
        yeni_deger = mevcut_deger + (1 if islem == "arttir" else -1)
        entry.delete(0, tk.END)
        entry.insert(0, str(yeni_deger))

    def hesapla(self):
        self.toplam=0
        for urun, (entry, fiyat) in self.urun_entries.items():
            miktar = int(entry.get())
            self.toplam += miktar * fiyat

        self.hesapButonu=tk.Button(self.pencere,bg="#22223b",fg="white",text="Hesapla",command=self.hesapla)
        self.hesapButonu.place(x=600,y=300)
        self.toplamEtiket=tk.Label(self.pencere,font=("Arial",13),text="Toplam Tutar: "+str(self.toplam)+"₺",bg="#22223b",foreground="#f2e9e4")
        self.toplamEtiket.place(x=700,y=300)
        self.fisButonu=tk.Button(self.pencere,bg="#22223b",fg="white",text="Fiş Yazdır",font=("Arial",20,'bold'),command=self.yazdirr,height=3,width=15)
        self.fisButonu.place(x=600,y=400)

    def masaDegerYazdir(self):
        self.girilenDeger = self.secilenMasa.get()
        self.masaNoEtiket.config(text=self.girilenDeger)

    def masalar(self):
        self.secilenMasa = tk.StringVar()
        self.masaSecYazi=tk.Button(self.pencere,font=("Arial",10),text="Masa Seç",command=self.masaDegerYazdir,bg="#22223b",fg="white")
        self.masaSecYazi.place(x=600,y=350)
        self.masaNoSecim = [str(i) for i in range(0,21)]
        self.masaNo = tk.OptionMenu(self.pencere, self.secilenMasa, *self.masaNoSecim)
        self.masaNo.config(bg="#22223b",fg="white")
        self.masaNo.place(x=750,y=348,width=50,height=25)
        self.masaNoEtiket = tk.Label(self.pencere,font=("Arial",13),bg="#22223b")

    def yazdirr(self):
        if self.masaNoEtiket.cget('text') == "":
            messagebox.showerror("Hata", "Lütfen masa numarasını seçiniz ve 'Masa Seç' butonuna basınız")
        else:
            with open("fis.txt", "a", encoding="utf-8") as dosya:
                dosya.write("\n--------------------------------------------------\n")
                if self.masaNoEtiket.cget('text') == "0":
                    dosya.write("Paket Sipariş\n")
                else:
                    dosya.write(f"Masa no: {self.masaNoEtiket.cget('text')}\n")
                dosya.write(f"{self.toplamEtiket.cget('text')}\n")
            self.mesajPenceresi()

    def yardim(self):
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

    def kapatButonu(self):
        if messagebox.askokcancel("Çıkış", "Çıkış yapılıyor kabul ediyor musun?"):
            self.pencere.destroy()

    def mesajPenceresi(self):
        messagebox.showinfo("Bilgi", "Fiş başarıyla oluşturuldu.\n fis.txt dosyasına kaydedildi.")

    def fisGecmisi(self):
        self.fisGecmisi = tk.Toplevel(self.pencere)
        self.fisGecmisi.title("Fiş Geçmişi")
        self.fisGecmisi.geometry("500x500")
        self.fisGecmisi.resizable(False, False)
        self.fisGecmisi.config(bg="#22223b")
        with open("fis.txt", "r",encoding="utf-8") as file:
            dosya_icerigi = file.readlines()
        if len(dosya_icerigi) < 12:
            for satir in range(len(dosya_icerigi)):
                tk.Label(self.fisGecmisi,text=dosya_icerigi[satir],bg="#22223b",fg="white").pack()
        else:
            for satir in range(len(dosya_icerigi)-12,len(dosya_icerigi)):
                tk.Label(self.fisGecmisi,text=dosya_icerigi[satir],bg="#22223b",fg="white").pack()

    def dosyaKontrol(self):
        if not os.path.exists("fis.txt"):
            with open("fis.txt", "w",encoding="utf-8") as file:
                file.write("")

restoran=Restoran()