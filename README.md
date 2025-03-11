TR

# Selenium ile Ekşi Sözlük Veri Toplama Scripti

Bu Python scripti, Selenium kütüphanesini kullanarak Ekşi Sözlük'teki belirli bir başlıktan rastgele sayfalardan veri çekmek için tasarlanmıştır.

## Gereksinimler

Bu scriptin çalışabilmesi için aşağıdaki bağımlılıkların yüklenmiş olması gerekmektedir:
- Python 3.x
- Selenium
- Google Chrome
- ChromeDriver

## Kurulum

1. Python'u yükleyin (eğer yüklü değilse).
2. Selenium'u yüklemek için aşağıdaki komutu çalıştırın:
   ```bash
   pip install selenium
   ```
3. ChromeDriver'ı sisteminize uygun sürümünü [buradan](https://sites.google.com/chromium.org/driver/downloads) indirip sistem yoluna ekleyin.

## Kullanım

1. Scripti çalıştırmak için aşağıdaki komutu kullanın:
```bash
python eksi_sozluk.py
```
2. Script çalıştırıldığında, Ekşi Sözlük'teki "Real Madrid" başlığının rastgele 10 sayfasından içerik çeker ve entries.txt dosyasına kaydeder.
3. Çalışma tamamlandıktan sonra, entries.txt dosyasında çekilen içerikleri bulabilirsiniz.

## Kod Açıklaması

- webdriver.Chrome() ile Chrome tarayıcısı başlatılır.
- Belirtilen URL'ye giderek rastgele 10 farklı sayfadan veri çekilir.
- .content sınıfına sahip HTML elementleri toplanarak listeye eklenir.
- Elde edilen veriler entries.txt dosyasına kaydedilir.
- İşlem tamamlandıktan sonra tarayıcı kapatılır.

  ENG

  # Selenium Web Scraper for Ekşi Sözlük

  This Python script is designed to scrape data from Ekşi Sözlük using Selenium. It fetches data from random pages of a specific topic.

  ## Requirements
  
  To run this script, you need to have the following dependencies installed:
  - Python 3.x
  - Selenium
  - Google Chrome
  - ChromeDriver
 
  # Installation

  1. Install Python if it's not already installed.
  2. Install Selenium by running:
  ```bash
   pip install selenium
   ```
  3. Download the appropriate version of ChromeDriver from [here](https://sites.google.com/chromium.org/driver/downloads) and add it to your system path.
 
  ## Usage

  1. Run the script with the following command:
  ```bash
  python eksi_sozluk.py
  ```
  2. The script will fetch content from 10 random pages of the "Real Madrid" topic on Ekşi Sözlük and save it to entries.txt.
  3. After execution, you can find the extracted content in entries.txt.

  ## Code Explanation
  - webdriver.Chrome() initializes the Chrome browser.
  - The script navigates to a predefined URL and randomly selects 10 pages.
  - Elements with the class .content are extracted and added to a list.
  - The extracted data is saved to entries.txt.
  - The browser is closed after the process is completed.


  
