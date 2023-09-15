from flask import Flask, render_template
import requests
from time import sleep
import random

app = Flask(__name__)


@app.route('/')
def home():
  random_count = random.randint(1, 10)
  random_numbers = []
  for _ in range(random_count):
    random_number = random.randint(1, 6237)
    random_numbers.append(random_number)
  aa = random_numbers[0]
  url = 'http://quran.ksu.edu.sa/interface.php?ui=mobile&do=search&type=ids'
  data = {'query': f"{aa}, {1+aa}"}
  sleep(5)
  response = requests.post(url, data=data, verify=False)

  if response.status_code == 200:
    iid = response.json()['results']['1']['text']
    iidd = response.json()['results']['2']['text']
    aya2 = response.json()['results']['2']['aya']
    sura = response.json()['results']['1']['sura']
    aya = response.json()['results']['1']['aya']
    if int(aya2) < 10:
      aya2 = "00" + aya2
    elif int(aya2) < 100:
      aya2 = "0" + aya2
    if int(aya) < 10:
      aya = "00" + aya
    elif int(aya) < 100:
      aya = "0" + aya

    if int(sura) < 10:
      sura = "00" + sura
    elif int(sura) < 100:
      sura = "0" + sura

    audio_url = f"http://quran.ksu.edu.sa/ayat/mp3/Ali_Jaber_64kbps/{sura}{aya}.mp3"

    audio_url2 = f"http://quran.ksu.edu.sa/ayat/mp3/Ali_Jaber_64kbps/{sura}{aya2}.mp3"

    
    audio_url2= audio_url2
    audio_url= audio_url
    aya= aya + " " + aya2
    text= iid + " " + iidd
    
    return render_template('index.html',audio_url2=audio_url2,aya=aya,audio_url=audio_url,text=text)



if __name__ == '__main__':
  app.run(host='0.0.0.0', port=81)
