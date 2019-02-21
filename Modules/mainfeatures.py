from Modules.basemodules import Backend
import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import selenium
from selenium import webdriver
import pyowm
import http.client
import pandas

confirm = ["evet", "onaylıyorum", "onay", "evet onaylıyorum", "onaylıyorum evet"]


class Features:

    def __init__(self, multimedia_module):
        self.mediamodule = multimedia_module

    def mapfeature(self, data):
        data = data.split()
        location = data[0]  # sondan bir öncekiler olmalı
        self.mediamodule.speak("Bekle Emre Sana " + location + " in nerede olduğunu göstereceğim")
        driver = webdriver.Chrome(
            'C:/Users/yemre/Desktop/chromedriver.exe')  # Optional argument, if not specified will search path.
        driver.get("https://www.google.com/maps/place/" + location + "/&amp;");
        time.sleep(15)
        driver.quit()

    def timefunc(self, data):
        time = ctime().split(sep=" ")
        newtime = time[3]
        return newtime

    def gunfunc(self, data):
        time = ctime().split(sep=" ")
        if time[1] == "Jan":
            time[1] = "Ocak"
        if time[1] == "Feb":
            time[1] = "Şubat"
        newtime = time[2] + " " + time[1] + " " + time[-1] + " " + time[3]
        return newtime

    def animsaticiolustur(self, data):
        try:
            self.mediamodule.speak("Hangi Saat için Anımsatıcı Kurmak istiyorsun?")
            time.sleep(5)
            data2 = self.mediamodule.recordAudio()
            if "saat" in data2:
                data2 = data2.split(sep=" ")
                saat = data2[1]
            elif "buçuk" in data2.split(sep=" "):
                saat = data2[0] + ":30"
            elif "çeyrek" in data2.split(sep=" "):
                saat = data2[0] + ":15"
            else:
                data2 = data2.split(sep=".")
                if len(data2[0]) == 1:
                    saat = "0" + data2[0] + ":" + data2[1]
                else:
                    saat = data2[0] + ":" + data2[1]
            self.mediamodule.speak("Anımsatıcı Adı Nedir?")
            time.sleep(1)
            data3 = self.mediamodule.recordAudio()
            animsaticinot = data3
            saat2 = pandas.DataFrame(data=[saat])
            animsaticinot2 = pandas.DataFrame(data=[animsaticinot])
            animsaticidatay = pandas.concat([animsaticinot2, saat2], axis=1)
            animsaticidatay.columns = ["Not", "Saat"]
            animsaticix = pandas.read_excel("animsatici.xlsx")
            animsaticidata = pandas.concat([animsaticix, animsaticidatay], axis=0, ignore_index=True)
            self.mediamodule.speak("Anımsatıcını {} saatine {} notuyla kuruyorum Onaylıyor musun?".format(saat, animsaticinot))
            time.sleep(6)
            dataconfirm = self.mediamodule.recordAudio()
            if dataconfirm in confirm:
                animsaticidata.to_excel("animsatici.xlsx")
                self.mediamodule.speak("Anımsatıcın Kuruldu.")
            else:
                self.mediamodule.speak("Lütfen Komutları Baştan ver")
        except:
            self.mediamodule.speak("Bir Hata Oluştu, Lütfen Komutları Baştan Ver.")

    def animsaticioku(self, data):
        self.mediamodule.speak("Anımsatıcıların Şu Şekilde")
        animsaticidata = pandas.read_excel("animsatici.xlsx")
        for i in range(0, len(animsaticidata)):
            print(str(animsaticidata.Saat[i]) + "da" + str(animsaticidata.Not[i]))
            self.mediamodule.speak(animsaticidata.Saat[i] + "da" + animsaticidata.Not[i])
            time.sleep(3)

    def playyoutube(self, data):
        global driver
        data = data.split()
        parcaismi = ""
        for i in data[:-1]:
            parcaismi = parcaismi + i
        self.mediamodule.speak("Bekle Emre Senin için " + parcaismi + " yi çalıyorum")
        driver = webdriver.Chrome('C:/Users/yemre/Desktop/chromedriver.exe')
        driver.get("https://www.youtube.com/results?search_query=" + parcaismi);
        select_element = driver.find_elements_by_xpath('//*[@id="video-title"]')
        for option in select_element:
            option.find_element_by_xpath('//*[@id="video-title"]').click()
            break
        return driver

    def stopsong(self, driver):
        driver.quit()

    def searchquestion(self, data):
        data = data.split()
        soru = ""
        for i in data[:-1]:
            soru = soru + "+" + i

        # TODO: Driver path eklentisi arayuz ile hazırlanabilir.
        drivery = webdriver.Chrome(
            'C:/Users/yemre/Desktop/chromedriver.exe')  # Optional argument, if not specified will search path.
        drivery.get("http://www.wikizeroo.net/wiki/tr/" + soru);
        select_element = drivery.find_elements_by_xpath('//*[@id="mw-content-text"]/div[1]/p[1]')
        for option in select_element:
            x = option.find_element_by_xpath('//*[@id="mw-content-text"]/div[1]/p[1]').text
        if x == None:
            self.mediamodule.speak("Bunun hakkında birşey bulamadım")
        else:
            self.mediamodule.speak("Vikipedia'dan bulduklarıma göre")
            self.mediamodule.speak(x)
        time.sleep(5)

    def tempature(self, data):
        # TODO: Buradaki key public değilse, uygulamaya özel bir key alınabilir.
        owm = pyowm.OWM('c0e97d6ec40865116fea05d55fc64cc7')
        self.mediamodule.speak("Neresi için Hava Durumu Öğrenmek istiyorsun?")
        time.sleep(4)
        data2 = self.mediamodule.recordAudio()
        if data2[0] == "i":
            data2 = "istanbul"
        observation = owm.weather_at_place("{},TR".format(data2))
        w = observation.get_weather()
        detailstat = w.get_detailed_status()
        tempature = w.get_temperature('celsius')["temp"]
        if detailstat == "light rain" or "light intensity shower rain":
            detailstat = "hafif yağmurlu"
        self.mediamodule.speak("{} için Hava {} ve {} derece".format(data2, detailstat, tempature))
        time.sleep(4)

    def createnote(self, data):
        data = data[7:]
        file = open("notlar.txt", "w")
        file.write(str(data.encode("utf-8")))
        file.close()
        self.mediamodule.speak("Not aldım")

    def readnote(self, data):
        file = open("notlar.txt", "r")
        self.mediamodule.speak("Notların şu şekilde")
        self.mediamodule.speak(file.read()[2:-1])
        self.mediamodule.speak("notların bu kadar")
        time.sleep(3)

    def emotionplaylist(self, data):
        self.mediamodule.speak("Hangisini çalayım? Mutlu mu, Normal mi? Depresif mi?")
        time.sleep(3)
        data2 = self.mediamodule.recordAudio()
        driver = webdriver.Chrome('C:/Users/yemre/Desktop/chromedriver.exe')
        if "mutlu" in data2:
            driver.get("https://www.youtube.com/watch?v=uwT2kmral3A&start_radio=1&list=RDMMuwT2kmral3A");
        if "normal" in data2:
            driver.get("https://www.youtube.com/watch?v=wJGcwEv7838&start_radio=1&list=RDwJGcwEv7838");
        if "depresif" in data2:
            driver.get("https://www.youtube.com/watch?v=N3oCS85HvpY&start_radio=1&list=RDN3oCS85HvpY");
        return driver

    def news(self, data):
        self.mediamodule.speak("İşte senin için birkaç haber")
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
        Idlist = [Id1, Id2, Id3, Id4, Id5]

        basliklar, aciklamalar = [], []
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
        for i in range(0, len(basliklar)):
            self.mediamodule.speak(basliklar[i])
            time.sleep(4)
            self.mediamodule.speak(aciklamalar[i])
            time.sleep(15)