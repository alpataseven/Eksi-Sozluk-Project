from selenium import webdriver
from selenium.webdriver.common.by import By

import random
import time

browser = webdriver.Chrome()

url = "https://eksisozluk.com/yonetim-bilisim-sistemleri--125101?p="

pageCount = 1
entries = []
entryCount = 1

while pageCount <=6:
    randomPage = random.randint(1,6)
    newUrl = url + str(randomPage)
    browser.get(newUrl)
    #Yukarıda 14 sayfadan 10 kere random sayfa açan kodu yazdık.
    elements = browser.find_elements(By.CSS_SELECTOR, ".content")
    for element in elements:
        entries.append(element.text)
    time.sleep(5)
    pageCount += 1

with open("entries.txt", "w", encoding="UTF-8") as file:
    for entry in entries:
        file.write(str(entryCount) + ".\n" + entry + "\n")
        file.write("**************************************\n")
        entryCount += 1

browser.close()