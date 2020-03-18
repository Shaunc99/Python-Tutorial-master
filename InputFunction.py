import requests;
import json;
import yagmail;

r = requests.get(url="http://a.astuce.media:9990/api/weather/groups.json?Group=North%20America&LevelOfDetail=High")
jsonText = json.loads(r.text)
jsonText = json.dumps(jsonText,indent=4)
print(jsonText)

with open('c:\\shayan\weather.json', 'w') as f:
    f.write(jsonText)
    f.close()


receiver = 'khalidi81@yahoo.com'
body = 'Shayan favorite car'
filename = 'c:\\shayan\\images\\ford.jpg'
pwd = "R1zwan!@#"
yag = yagmail.SMTP('developerkhi@gmail.com',password = pwd)
yag.send(
    to=receiver,
    subject="See shayan favorite car",
    contents=body,
    attachments=filename,
)