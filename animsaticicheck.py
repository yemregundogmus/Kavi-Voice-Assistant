from Modules.basemodules import Main as m
from time import ctime
import pandas as pd
import time
import os

def slice(x):
    return x[:-3]

while 1:
    data = pd.read_excel("animsatici.xlsx")
    data.Saat = data.Saat.astype(str)
    print
    if len(data[data.Saat.apply(slice) == str(ctime().split(" ")[3][:-3])]) > 0:
        os.system("animsatici.mp3")
        time.sleep(1)
        m.speak("Hey {} adet anımsatıcın var.".format(len(data[data.Saat.apply(slice) == str(ctime().split(" ")[3][:-3])])))
        time.sleep(3)
        for i in range(0,len(data[data.Saat.apply(slice) == str(ctime().split(" ")[3][:-3])])):
            m.speak(data[data.Saat.apply(slice) == str(ctime().split(" ")[3][:-3])].Saat.values[i] +"da"+ data[data.Saat.apply(slice) == str(ctime().split(" ")[3][:-3])].Not.values[i])
            time.sleep(2)
        time.sleep(15)
        continue
    else:
        continue