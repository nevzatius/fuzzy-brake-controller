# Proje Raporu: Fuzzy Brake Controller

## 1. Giriş ve Amaç

Araçlarda sürüş güvenliği ve konforu, fren basıncı dağılımının yol koşullarına ve sürüş tarzına dinamik uyumuyla artırılabilir. Bu projede, fren basıncı dağılımını ön ve arka tekerlekler arasında bulanık mantık kontrolcüsü kullanarak optimize etmeyi amaçladık.

## 2. Literatür Taraması

* Bulanık mantık, belirsiz ve sürekli verileri insan benzeri karar kurallarıyla işleme uygundur.
* Otomotivde ABS ve ESP sistemlerinde bulanık kontrolcü uygulamaları yaygındır.

## 3. Üyelik Fonksiyonları

Her girdi değişkeni (speed, brake\_pressure, road\_grip, slope, tire\_temp) için üçgen (trimf) üyelik fonksiyonları tanımlandı:

* **Düşük (Low)**: $\mu_{low}(x) = \begin{cases}1 - \frac{x - a}{b - a}, & a \le x \le b\\0, & \text{aksi halde}\end{cases}$
* **Orta (Medium)**: $\mu_{medium}(x) = \begin{cases}\frac{x - a}{b - a}, & a \le x \le b\\1 - \frac{x - b}{c - b}, & b \le x \le c\\0, & \text{aksi halde}\end{cases}$
* **Yüksek (High)**: $\mu_{high}(x) = \begin{cases}\frac{x - a}{b - a}, & a \le x \le b\\1, & x \ge b\\0, & \text{aksi halde}\end{cases}$

Örnek: Hız değişkeni için $a=0, b=0, c=80$ düşük üyelik, $a=60, b=100, c=140$ orta üyelik, $a=120, b=200, c=200$ yüksek üyelik.

## 4. Kural Tabanı ve Çıkarım Süreci

### 4.1. Örnek Kural

> **Kural:** Eğer hız **yüksek** ve yol tutuş **düşük** ise arka bias **yüksek**.

### 4.2. Adım Adım Çıkarım (Numerik Örnek)

1. **Girdiler:** hız = 150 km/h, fren\_basıncı = 60%, yol\_tutuş = 30%, eğim = 0°, lastik\_sıcaklığı = 50°C.
2. **Üyelik Değerleri:**

   * $\mu_{speed,high}(150) = \frac{150 - 120}{200 - 120} = 0.375$
   * $\mu_{road\_grip,low}(30) = 1 - \frac{30 - 0}{40 - 0} = 0.25$
3. **Kuralın Gücü (Activation):**
   $\alpha = \min(0.375, 0.25) = 0.25$
4. **Çıktı Üyelik Kesimi:**
   Arka bias **yüksek** üyelik fonksiyonunda kesme seviyesi = 0.25.
5. **Defuzzyfication (Merkez ağırlık Yöntemi):**
   $y^* = \frac{\int y \; \mu'(y) \, dy}{\int \mu'(y) \, dy}$ burada $\mu'$ kesilen üyelik.
   Yaklaşık olarak ön bias = 60%, arka bias = 75% elde edildi.

## 5. Mimari ve Uygulama Detayları

* **`create_brake_controller()`**: scikit-fuzzy kontrolcüsü tanımlanıp kural tabanı oluşturulur.
* **Tkinter UI**: `fuzzy_brake_controller.py` içinde slider ve etiket düzeni.
* **Qt5 UI**: `qt_gui.py` ile PyQt5 tabanlı alternatif arayüz.

## 6. Test Sonuçları

| Senaryo | Hız | Fren Basıncı | Yol Tutuş | Ön Bias % | Arka Bias % |
| ------- | --- | ------------ | --------- | --------- | ----------- |
| 1       | 120 | 80           | 50        | 85.2      | 68.5        |
| 2       | 50  | 30           | 80        | 45.0      | 20.3        |

Grafik ve detaylı kural değerlendirmesi rapor PDF'inde bulunmaktadır.

## 7. Sonuç ve Öneriler

* Kontrolcü, farklı yol ve sürüş koşullarına dinamik uyum gösterdi.
* Gelecek çalışmalar: gerçek araç verileriyle kalibrasyon, CAN bus entegrasyonu, Qt5 arayüz geliştirmeleri.

---

**Nevzatcan Çelik** | 2025
