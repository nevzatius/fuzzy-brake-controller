# Fuzzy Brake Controller

Bu proje, Python ile gerçek dünyadan alınan bir otomotiv senaryosunda fren basıncı dağılımını bulanık mantık (Fuzzy Logic) kullanarak kontrol etmeyi amaçlar.

## Özellikler
- **5 Girdi**: Hız, Fren Basıncı, Yol Tutuş, Eğim, Lastik Sıcaklığı  
- **2 Çıktı**: Ön Fren Dağılımı, Arka Fren Dağılımı  
- **Python** ile geliştirilmiştir.  
- **Scikit-Fuzzy** (skfuzzy) ve dolaylı olarak SciPy kullanır.  
- **Tkinter** ve **PyQt5** tabanlı kullanıcı dostu arayüzler.  
- **Matplotlib** tabanlı üyelik fonksiyonu görselleştirme scripti.

## Dosya Yapısı
```
fuzzy-brake-controller/
├── src/
│   ├── __init__.py
│   ├── fuzzy_brake_controller.py
│   ├── qt_gui.py
│   └── membership_plots.py
├── docs/
│   └── report.md
├── main.py
├── requirements.txt
└── README.md
```

## Kurulum
1. Depoyu klonlayın:
   ```bash
   git clone https://github.com/nevzatius/fuzzy-brake-controller.git
   cd fuzzy-brake-controller
   ```
2. Sanal ortam oluşturup etkinleştirin (önerilir):
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Windows: venv\Scripts\activate
   ```
3. Gerekli paketleri yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

## Çalıştırma

### Tkinter GUI
```bash
python src/fuzzy_brake_controller.py
```

### PyQt5 GUI
```bash
python src/qt_gui.py
```

### Tek Script ile Seçim
```bash
python main.py --gui tk    # Tkinter arayüzü
python main.py --gui qt    # PyQt5 arayüzü
```

### Üyelik Fonksiyonu Grafikleri
```bash
python src/membership_plots.py
```

## Geliştirme ve Dokümantasyon
- `docs/report.md` dosyasında üyelik fonksiyonları, kural tabanı ve sistem mimarisi detaylıca anlatılmıştır.
- `.gitignore` ile gereksiz dosyaları filtreleyebilirsiniz.
- `LICENSE` ekleyerek açık lisans belirtebilirsiniz.
