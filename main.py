from Modules.basemodules import Main as m
from Modules.mainfeatures import Features as f
from random import randint
from time import ctime
import pandas
import time
import os


nasilsincumeleleri = ["nasılsın","naber","ne haber","napıyorsun","nasıl gidiyor","naber","napıyon","nasıl","nabıyon"] 
iltifat = ["mükemmelsin","çok iyisin","mükemmel","efsane","saol","teşekkürler","çok","iyi","çok iyi"]
donus = ["iyiyim sen","çok iyiyim","biraz keyifsizim"]
donustesekkur = ["Çok teşekkürler","beni utandırıyorsun","utandım","teşekkürler","yardımcı olabildiysem ne mutlu bana"]
saat = ["saat","kaç","saat kaç","kaç saat","zaman"]
gun = ["bugün ayın kaçı","ayın","kaçı","bugün günlerden ne","günler","günlerden","bu gün ayın"]
maps = ["nerede","nerededir","nerda","nerde","neresi"]
playyoutube = ["çal","oynat","aç"]
search = ["nedir","kimdir","ne","nasıl"]
tempature = ["derece","hava","kaç","hava kaç","sıcaklık kaç","sıcaklık","hava durumu"]
note = ["not al","not alır mısın","not"]
noteread = ["notlarımı oku","notları oku","notlar"]
playlist = ["müzik listemi çal","müzik listem","müzik","playlist","listem","müzik listeleri"]
haber = ["haberler","haberleri","haber","gündem","gazete","oku","haberleri oku"]
stopsong = ["şarkıyı kapat","şarkıyı durdur","durdur","kapat"]
kapatma = ["sistemi kapat","uyu","kendini kapat"]
kaviopen = ["hey kavi","hey","alo","kavi","açıl","açıl susam açıl","açın"]
animsatici = ["anımsatıcı oluştur","anımsatıcı kur","anımsatıcı başlat","anımsatıcı oluş"]
animsaticioku = ["anımsatıcılarım","anımsatıcımı oku","anımsatıcılar","anımsatıcılarımı oku","anımsatıcı oku","anımsatıcım"]



def kavi(data):
    if data in nasilsincumeleleri:
        m.speak(donus[randint(0,2)])
    if data in iltifat:
        m.speak(donustesekkur[randint(0,4)])
    if data in saat:
        m.speak(f.timefunc(data))
    if data in gun:
        m.speak(f.gunfunc(data))
    if data in maps:
        f.mapfeature(data)
    if data in playyoutube:
        global driver
        driver = f.playyoutube(data)
    if data in stopsong:
        f.stopsong(driver)
    if data.split() in search:
        f.searchquestion(data)
    if data in tempature:
        f.tempature(data)
    if data in note:
        f.createnote(data)
    if data in noteread:
        f.readnote(data)
    if data in playlist:
        f.emotionplaylist(data)
    if data in haber:
        f.news(data)
    if data in animsatici:
        f.animsaticiolustur(data) 
    if data in animsaticioku:
        f.animsaticioku(data)

m.speak("Merhaba Emre, Senin için ne yapabilirim")
while True:
    datax = m.recordAudio()
    data = pandas.read_excel("animsatici.xlsx")
    data.Saat = data.Saat.astype(str)
    if len(data[data.Saat == str(ctime().split(" ")[3][:-3])]) > 0:
        os.system("animsatici.mp3")
        time.sleep(1)
        m.speak("Hey {} adet anımsatıcın var.".format(len(data[data.Saat == str(ctime().split(" ")[3][:-3])])))
        time.sleep(3)
        for i in range(0,len(data[data.Saat == str(ctime().split(" ")[3][:-3])])):
            m.speak(data[data.Saat == str(ctime().split(" ")[3][:-3])].Saat.values[i] +"da"+ data[data.Saat == str(ctime().split(" ")[3][:-3])].Not.values[i])
            time.sleep(2)
            continue
        time.sleep(15)
    else:
        if datax in kaviopen:
            os.system("hello.mp3")
            time.sleep(0.5)
            datax = m.recordAudio()
            if datax in kapatma:
                m.speak("Görüşürüz")
                break
            else: 
                kavi(datax)