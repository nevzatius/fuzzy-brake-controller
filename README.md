# Fuzzy Brake Controller

Bu proje, Python ile gerçek dünyadan alınan bir otomotiv senaryosunda fren basıncı dağılımını bulanık mantık (Fuzzy Logic) kullanarak kontrol etmeyi amaçlar.

## Özellikler
- **5 Girdi**: Hız, Fren Basıncı, Yol Tutuş, Eğim, Lastik Sıcaklığı
- **2 Çıktı**: Ön Fren Dağılımı, Arka Fren Dağılımı
- **Python** ile geliştirilmiştir.
- **Scikit-Fuzzy** (skfuzzy) ve dolaylı olarak SciPy kullanır.
- **Tkinter** tabanlı kullanıcı dostu arayüz.

## Dosya Yapısı
```
fuzzy-brake-controller/
├── src/
│   └── fuzzy_brake_controller.py   # Uygulamanın tam Python kodu
├── docs/
│   └── report.md                   # Proje raporu ve açıklamalar
├── requirements.txt                # Gerekli Python paketleri
└── README.md                       # Proje tanıtımı ve kurulum
```

## Kurulum
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/nevzatcan/fuzzy-brake-controller.git
   cd fuzzy-brake-controller
   ```
2. Sanal ortam oluşturup etkinleştirin (önerilir):
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # Windows: venv\\Scripts\\activate
   ```
3. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## Çalıştırma
```bash
python src/fuzzy_brake_controller.py
```

## Kullanım
- Slider’ları ilgili değer aralıklarında ayarlayın.
- Arayüz, `Hesapla` butonuna basıldığında veya slider hareket ettiğinde ön ve arka fren dağılımını (%) gerçek zamanlı gösterir.

## Geliştirme ve Dokümantasyon
- `docs/report.md` dosyasında üyelik fonksiyonları, kural tabanı ve sistem mimarisi detaylıca anlatılmıştır.
- Qt5 veya farklı bir GUI arayüzü ekleyerek proje genişletilebilir.

---
**Nevzatcan Çelik** | 2025
