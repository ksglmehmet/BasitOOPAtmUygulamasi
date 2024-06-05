# Atm yapısı aslında tek başına sınıftır. Metotları-fonksiyonları vardır. Fonksiyonları çağırırız. Her yerde kullanmak için.
# Kendi başına ATM sınıfı oluşturucaz. Kendi içerisinde özellikler olucak, fonksiyonlar-metotlar yani. Giriş kontrolünü yapan. Çıkış yapan vs vs.
# Şuan herhangi Veritabanımızda ilgili örneğe dayalı verimiz olmadığı için Müşteri Sınıfı oluşturacağım.
# Geçen uygulamada yaptığımız gibi, ama sözlük tipinde değilde Sınıf olarak yapacağım.

class Musteri:
    def __init__(self, Ad, Soyad, KartSifre, HesapBakiye, KrediKartBorc, SonOdeme): # Müşterimizin özellikleri.
        self.Ad = Ad
        self.Soyad = Soyad
        self.KartSifre = KartSifre
        self.HesapBakiye = HesapBakiye
        self.KrediKartBorc = KrediKartBorc
        self.SonOdeme = SonOdeme

AhmetHesap = Musteri("Ahmet", "Candan", "1357", 5000, 4200, "20/11/2021") # Bu şekilde müşterilerimizi ekledik. Veritabanından veri alınır reelde.
MehmetHesap = Musteri("Mehmet", "Can", "2468", 6000, 3800, "28/11/2024")

TakilanKart = MehmetHesap

class ATM:
    def __init__(self, AtmAd):
        self.AtmAd = AtmAd
        self.GirisKontrol()
        self.dongu = True
        
    def GirisKontrol(self):
        
        Hak = 2
        for i in range(0, 3):
            Sifre = input(f"Merhaba {TakilanKart.Ad} {TakilanKart.Soyad}, Lütfen 4 Haneli Şifrenizi Giriniz: ")
            if Sifre == TakilanKart.KartSifre:
                print(f"Giriş Başarılı. Hoşgeldiniz Sayın {TakilanKart.Ad} {TakilanKart.Soyad}")
                self.program()
            elif Sifre != TakilanKart.KartSifre and Hak != 0:
                print(f"Sayın {TakilanKart.Ad} {TakilanKart.Soyad}, Şifrenizi Yanlış Girdiniz. Kalan Hakkınız {Hak}.")
                Hak -= 1
            elif Sifre != TakilanKart.KartSifre and Hak == 0:
                print(f"""\nSayın {TakilanKart.Ad} {TakilanKart.Soyad}, Şifrenizi 3 Defa Hatalı Girdiğinizden Dolayı Kartınız Bloke Olmuştur.
                      Lütfen En Yakın Şubemize Müracaat Ediniz.""")
                exit()
    
    def program(self):
        
        secim = self.menu()
        
        if secim == 1:
            self.bakiye()
        if secim == 2:
            self.kkborc()
        if secim == 3:
            self.paracek()
        if secim == 4:
            self.parayatir()
        if secim == 5:
            self.cikis()
    
    def menu(self):
        secim = int(input(f"****Merhaba, {self.AtmAd}'a Hoşgeldiniz Sayın {TakilanKart.Ad} {TakilanKart.Soyad}.\n\nLütfen Yapmak İstediğiniz İşlemi Seçiniz...\n\n[1] Bakiye Sorgulama\n[2] Kredi Kartı Borç Sorgulama\n[3] Para Çekme\n[4] Para Yatırma\n[5] Kart İade\n\nSeçim: "))
        
        while secim < 1 or secim > 5:
            print("\n\nLütfen 1 ve 5 Arasında Geçerli Bir Değer Giriniz...\nAna Menüye Dönülüyor...")
            self.program()
        return secim
    
    def bakiye(self):
        print(f"\nHesap Bakiyeniz: {TakilanKart.HesapBakiye} TL'dir.")
        self.menudon()
    
    def kkborc(self):
        print(f"\nKredi Kartı Borcunuz: {TakilanKart.SonOdeme} Son Ödeme Tarihli, {TakilanKart.KrediKartBorc} TL'dir.")
        self.menudon()
    
    def paracek(self):
        Tutar = int(input("Lütfen Çekmek İstediğiniz Tutarı Giriniz: "))
        if Tutar > TakilanKart.HesapBakiye:
            print(f"Sayın {TakilanKart.Ad} {TakilanKart.Soyad}, {Tutar} TL Hesabınızda Bulunmamaktadır.")
            self.menudon()
        elif Tutar < 0:
            print("Lütfen Pozitif Sayılar Giriniz: ")
            self.paracek()
        else:
            print(f"Sayın {TakilanKart.Ad} {TakilanKart.Soyad}, {Tutar} TL Hesabınızdan Çekilmektedir. Lütfen Bekleyiniz.")
            print("Paranızı Almayı Lütfen Unutmayınız.")
            TakilanKart.HesapBakiye = TakilanKart.HesapBakiye - Tutar
            print(f"Sayın {TakilanKart.Ad} {TakilanKart.Soyad}, İşlem Sonrası Hesap Bakiyeniz: {TakilanKart.HesapBakiye} TL'dir.")
            self.menudon()
    
    def parayatir(self):
        Tutar = int(input("Lütfen Yatırmak İstediğiniz Tutarı Giriniz: "))
        if Tutar < 0:
            print("Yatırmak İstediğiniz Tutar 0'dan Küçük Olamaz. Lütfen Pozitif Sayı Giriniz: ")
            self.parayatir()
        print(f"Yatırmak İstediğiniz {Tutar} TL, Hesabınıza Yatırılmaktadır. Lütfen Bekleyiniz.")
        TakilanKart.HesapBakiye = TakilanKart.HesapBakiye + Tutar
        print(f"Sayın {TakilanKart.Ad} {TakilanKart.Soyad}, İşlem Sonrası Hesap Bakiyeniz: {TakilanKart.HesapBakiye} TL'dir.")
        self.menudon()
    
    def cikis(self):
        print(f"Sayın {TakilanKart.Ad} {TakilanKart.Soyad}, {self.AtmAd}'ı Tercih Ettiğiniz İçin Teşekkür Eder, İyi Günler Dileriz.")
        exit()
    
    def menudon(self):
        x = int(input("""\nAna Menüye Dönmek İçin Lütfen 7 Tuşuna Basınız. Kart İade İçin 5'e Basınız: """))
        if x == 7:
            self.program()
        if x == 5:
            self.cikis()

Banka = ATM("KösoğluBank")
while Banka.dongu:
    Banka.program()