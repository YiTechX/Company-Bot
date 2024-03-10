# Company Bot

Company Bot, Discord sunucuları arasında işbirliğini kolaylaştırmak için tasarlanmış bir bot projedir. Bu bot, farklı sunucular arasında "company" adı verilen yapıları oluşturarak üyelerin bir araya gelip projeler üzerinde çalışmasını sağlar.

## Özellikler

- **Company Oluşturma**: Sunucu sahipleri, belirli bir kanalı seçerek yeni bir company oluşturabilirler.
- **Company'ye Katılma**: Kullanıcılar, belirli bir katılım kodunu kullanarak bir company'e katılabilirler.
- **Company Listesi**: Bot, sunucuda bulunan company'leri listeler ve en popüler 10 company'i gösterir.
- **Otomatik Güncelleme**: Bot, her bir company'deki değişiklikleri otomatik olarak takip eder ve main kanalında güncel bilgileri paylaşır.

## Kurulum

1. Bu projeyi kendi bilgisayarınıza klonlayın veya indirin.
2. Discord Developer Portal'dan bir bot oluşturun ve gerekli izinleri verin.
3. Ana dizinde bulunan `config.json` dosyasını düzenleyerek bot tokenınızı ekleyin.
4. Botunuzu çalıştırın: `python main.py`

## Kullanım

- `w!createcompany #kanal`: Belirli bir kanala yeni bir company oluşturur.
- `w!entercompany <kod>`: Belirli bir company'e katılım kodu kullanarak katılır.
- `w!leavecompany`: Mevcut company'den ayrılır.
- `w!companies`: En popüler 10 company'i listeler.

## Katkıda Bulunma

Pull request'ler her zaman açıktır. Büyük değişiklikler yapmadan önce lütfen tartışmak için bir konu açın.

## Lisans

Bu proje [MIT Lisansı](LICENSE) altında lisanslanmıştır.
