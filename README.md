TCDD Bilet Kontrol ve Bildirim Otomasyonu

Bu proje, belirli TCDD tren seferleri için istasyon, tren ID'leri, kalkış zamanları ve koltuk tipleri gibi bilgileri girerek, belirli seferlerdeki bilet durumunu kontrol eder. Eğer istenilen bilet tipi mevcutsa, kullanıcıya otomatik olarak e-posta gönderilir.

Özellikler

TCDD tren seferleri için belirli istasyonlar, tren ID'leri ve kalkış zamanları girilerek, bilet durumu sorgulanabilir.
Belirli koltuk tiplerinde bilet olup olmadığı kontrol edilir.
Bilet mevcut olduğunda, kullanıcıya e-posta bildirimi gönderilir.
Kullanım
Bu otomasyonu kullanmak tamamen kullanıcı sorumluluğundadır.
TCDD API veya veri erişim izinlerinin geçerliliği ve doğru şekilde çalışması kullanıcıya aittir.
Kodu kullanmadan önce gerekli API anahtarlarını ve bağlantıları yapılandırdığınızdan emin olun.

Kurulum

Bu repo'yu klonlayın:

git clone https://github.com/muakyz/tcdd_bilet_otomasyonu.git

Gerekli bağımlılıkları yükleyin:

pip install -r requirements.txt

.env dosyasını düzenleyin ve API erişim bilgilerinizi girin.

Otomasyonu çalıştırarak belirli seferler için bilet sorgulaması yapın.

Sorumluluk Reddi

Bu otomasyonu kullanarak, herhangi bir sorumluluğunuzun kabul edilmesi gerektiğini ve yalnızca kişisel kullanım amaçlı olduğunu onaylarsınız. Kodu kullanarak herhangi bir sorun yaşarsanız, sorumluluk tamamen kullanıcının kendisine aittir.
