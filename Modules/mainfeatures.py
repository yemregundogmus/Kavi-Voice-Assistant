from Modules.basemodules import Main as m
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import selenium
from selenium import webdriver
import pyowm
import http.client

class Features:

    def mapfeature(data):
        data = data.split()
        location = data[0] #sondan bir öncekiler olmalı
        m.speak("Bekle Emre Sana " + location +" in nerede olduğunu göstereceğim")
        driver = webdriver.Chrome('C:/Users/yemre/Desktop/chromedriver.exe')  # Optional argument, if not specified will search path.
        driver.get("https://www.google.com/maps/place/" + location + "/&amp;");
        time.sleep(15)
        driver.quit()

    def playyoutube(data):
        global driver
        data = data.split()
        parcaismi = ""
        for i in data[:-1]:
            parcaismi = parcaismi + i
        m.speak("Bekle Emre Senin için "+ parcaismi + " yi çalıyorum")
        driver = webdriver.Chrome('C:/Users/yemre/Desktop/chromedriver.exe')
        driver.get("https://www.youtube.com/results?search_query="+parcaismi);
        select_element = driver.find_elements_by_xpath('//*[@id="video-title"]')
        for option in select_element:
            option.find_element_by_xpath('//*[@id="video-title"]').click()
            break
        return driver

    def stopsong(driver):
        driver.quit()

    def searchquestion(data):
        data = data.split()
        soru = ""
        for i in data[:-1]:
            soru = soru +"+"+ i
        drivery = webdriver.Chrome('C:/Users/yemre/Desktop/chromedriver.exe')# Optional argument, if not specified will search path.
        drivery.get("http://www.wikizeroo.net/wiki/tr/"+soru);
        select_element = drivery.find_elements_by_xpath('//*[@id="mw-content-text"]/div[1]/p[1]')
        for option in select_element:
            x = option.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[1]').text
        if x == None:
            m.speak("Bunun hakkında birşey bulamadım")
        else:
            m.speak("Vikipedia'dan bulduklarıma göre")
            m.speak(x)
        time.sleep(5)
    
    def tempature(data):
        owm = pyowm.OWM('c0e97d6ec40865116fea05d55fc64cc7') 
        m.speak("Neresi için Hava Durumu Öğrenmek istiyorsun?")
        time.sleep(4)
        data2 = m.recordAudio()
        if data2[0] == "i":
            data2 = "istanbul"
        observation = owm.weather_at_place("{},TR".format(data2))
        w = observation.get_weather()
        detailstat = w.get_detailed_status()
        tempature = w.get_temperature('celsius')["temp"]
        if detailstat == "light rain" or "light intensity shower rain":
            detailstat = "hafif yağmurlu"
        m.speak("{} için Hava {} ve {} derece".format(data2,detailstat,tempature))
        time.sleep(4)

    def createnote(data):
        data = data[7:]
        file = open("notlar.txt","w")
        file.write(str(data.encode("utf-8")))
        file.close()
        m.speak("Not aldım")

    def readnote(data):
        file = open("notlar.txt","r")
        m.speak("Notların şu şekilde")
        m.speak(file.read()[2:-1])
        m.speak("notların bu kadar")
        time.sleep(3)

    def emotionplaylist(data):
        m.speak("Hangisini çalayım? Mutlu mu, Normal mi? Depresif mi?")
        time.sleep(3)
        data2 = m.recordAudio()
        driver = webdriver.Chrome('C:/Users/yemre/Desktop/chromedriver.exe')
        if "mutlu" in data2:
            driver.get("https://www.youtube.com/watch?v=uwT2kmral3A&start_radio=1&list=RDMMuwT2kmral3A");
        if "normal" in data2:
            driver.get("https://www.youtube.com/watch?v=wJGcwEv7838&start_radio=1&list=RDwJGcwEv7838");
        if "depresif" in data2:
            driver.get("https://www.youtube.com/watch?v=N3oCS85HvpY&start_radio=1&list=RDN3oCS85HvpY");
        return driver

    def news(data):
        m.speak("İşte senin için birkaç haber")
        conn = http.client.HTTPSConnection("api.hurriyet.com.tr")

        headers = {
            'accept': "application/json",
            'apikey': "a82aa603c5eb49d8891c0dc36c19c44f"
            }

        conn.request("GET", "/v1/articles?%24select=Id&%24top=42&%24skip=0", headers=headers)

        res = conn.getresponse()
        data = res.read()

        Id1 = data.decode("utf-8")[8:-741]
        Id2 = data.decode("utf-8")[26:-723]
        Id3 = data.decode("utf-8")[44:-705]
        Id4 = data.decode("utf-8")[62:-687]
        Id5 = data.decode("utf-8")[80:-669]
        Idlist = [Id1,Id2,Id3,Id4,Id5]

        basliklar,aciklamalar = [],[]
        for i in Idlist:
            conn1 = http.client.HTTPSConnection("api.hurriyet.com.tr")
            conn2 = http.client.HTTPSConnection("api.hurriyet.com.tr")

            headers = {
                'accept': "application/json",
                'apikey': "a82aa603c5eb49d8891c0dc36c19c44f"
                }

            conn1.request("GET", "/v1/articles/{}?%24select=Title".format(i), headers=headers)
            conn2.request("GET", "/v1/articles/{}?%24select=Description".format(i), headers=headers)

            res1 = conn1.getresponse()
            res2 = conn2.getresponse()
            baslik = res1.read()
            aciklama = res2.read()
            aciklama = aciklama[16:-2].decode("utf-8")
            baslik = baslik[10:-2].decode("utf-8")

            basliklar.append(baslik)
            aciklamalar.append(aciklama)
        for i in range(0,len(basliklar)):
            m.speak(basliklar[i])
            time.sleep(4)
            m.speak(aciklamalar[i])
            time.sleep(15)