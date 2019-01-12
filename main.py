from Modules.basemodules import Main as m
from Modules.mainfeatures import Features as f
from random import randint
from time import ctime
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
kaviopen = ["hey kavi","hey","alo","kavi","açıl","açıl susam açıl"]

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
    if data in search:
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
            

m.speak("Merhaba Emre, Senin için ne yapabilirim")
while True:
    data = m.recordAudio()
    if data in kaviopen:
        os.system("hello.mp3")
        time.sleep(0.5)
        data = m.recordAudio()
        if data in kapatma:
            m.speak("Görüşürüz")
            break
        else:
            kavi(data)