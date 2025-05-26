# Proje Raporu: Fuzzy Brake Controller

## 1. Giriş ve Amaç
Bu projede, araç frenleme sistemlerinde sürüş güvenliğini ve konforu artırmak amacıyla fren basıncı dağılımını ön ve arka tekerlekler arasında dinamik olarak ayarlayan bir bulanık mantık kontrolcüsü tasarlanmıştır.

## 2. Literatür Taraması
Günümüzde ABS ve ESP gibi sistemlerde bulanık mantık uygulamaları, değişken yol koşulları ve sürüş tarzlarına esneklik kazandırmak için kullanılmaktadır.

## 3. Problem Tanımı ve Değişkenler
- **Girdiler (5):**  
  - Hız (speed)  
  - Fren Basıncı (brake_pressure)  
  - Yol Tutuş Katsayısı (road_grip)  
  - Eğim Derecesi (slope)  
  - Lastik Sıcaklığı (tire_temp)

- **Çıktılar (2):**  
  - Ön Fren Dağılımı (front_bias)  
  - Arka Fren Dağılımı (rear_bias)

## 4. Bulanık Mantık Kuramı
Bulanık mantık, belirsizlik içeren sistemlerde insan mantığına yakın karar verme mekanizması sağlar. Üyelik fonksiyonları ve IF-THEN kuralları temel alınır.

## 5. Üyelik Fonksiyonları
Her girdi için 3 seviye (low, medium, high) ve çıktılar için 3 seviye (low, medium, high) kullanıldı. `trimf` (üçgen) üyelik fonksiyonları tercih edildi.

## 6. Kural Tabanı
- Kombinasyon kuralları: Fren basıncı + hız / yol tutuş / eğim / lastik sıcaklığı
- Fallback kuralları: Tek değişkene dayalı öncelikli kontroller  
Toplamda 20+ kural tanımlandı.

## 7. Uygulama Detayları
- Python 3.9+  
- `scikit-fuzzy`, `numpy`, `scipy`  
- GUI: `tkinter`  
- Modüler kod: `create_brake_controller()` ve `launch_gui()`

## 8. Test Sonuçları
Farklı senaryolarda, hız ve yol koşuluna göre ön/arka bias değerleri uygun seviyelerde belirlendi.  
Örnek Senaryo:

| Hız (km/h) | Fren Basıncı (%) | Yol Tutuş (%) | Ön Bias (%) | Arka Bias (%) |
|------------|------------------|---------------|-------------|---------------|
| 120        | 70               | 50            | 80.0        | 60.0          |
| 50         | 30               | 80            | 40.0        | 20.0          |

## 9. Sonuç ve Değerlendirme
Tasarlanan kontrolcü, değişken sürüş koşullarına esnek yanıt verdi. Ek olarak gerçek araç testi verileri ile kalibrasyon önerilir.

## 10. Geliştirme Önerileri
- Qt5 tabanlı arayüz  
- Gerçek zamanlı CAN bus entegrasyonu  
- Makine öğrenimi ile kural optimizasyonu  
