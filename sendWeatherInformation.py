import urllib.request
from bs4 import BeautifulSoup
import requests

weather_icon_abspath = 'PycharmProjects//pythonProject//weather_icon//'
line_notify_token = 'line_notify_token'
line_notify_api = 'https://notify-api.line.me/api/notify'

rssurl = 'https://rss-weather.yahoo.co.jp/rss/days/4620.xml'
URL = 'https://weather.yahoo.co.jp/weather/jp/8/4010/8201.html'

tenki = []
detail = []

#HTML parser function
def Parser(rssurl):
    with urllib.request.urlopen(rssurl) as res:
        xml = res.read()
        soup = BeautifulSoup(xml, "html.parser")
        for item in soup.find_all('item'):
            title = item.find('title').string
            description = item.find('description').string

            if title.find("[ PR ]") == -1:
                tenki.append(title)
                detail.append(description)


#exprot weather icon function
def weather_icon(i, detail):
    if (detail[i].find('晴')) != -1 and (detail[i].find('曇')) == -1 and (detail[i].find('雨')) == -1 and (detail[i].find('雪')) == -1:
        files = {'imageFile': open(weather_icon_abspath + 'sunny.jpg', 'rb')}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)


    elif (detail[i].find('曇')) != -1 and (detail[i].find('晴')) == -1 and (detail[i].find('雨')) == -1 and (detail[i].find('雪')) == -1:
        files = {'imageFile': open(weather_icon_abspath + 'cloudy.jpg', 'rb')}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)


    elif (detail[i].find('雨')) != -1 and (detail[i].find('晴')) == -1 and (detail[i].find('曇')) == -1 and (detail[i].find('雪')) == -1:
        files = {'imageFile': open(weather_icon_abspath + 'rain.jpg', 'rb')}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)


    elif (detail[i].find('晴')) != -1 and (detail[i].find('雨')) == -1 and (detail[i].find('曇')) != -1 and (detail[i].find('雪')) == -1:
        files = {'imageFile': open(weather_icon_abspath + 'sunny_cloudy.jpg', 'rb')}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)


    elif (detail[i].find('晴')) != -1 and (detail[i].find('雨')) != -1 and (detail[i].find('曇')) == -1 and (detail[i].find('雪')) == -1:
        files = {'imageFile': open(weather_icon_abspath + 'sunny_rain.jpg', 'rb')}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)


    elif (detail[i].find('晴')) == -1 and (detail[i].find('雨')) != -1 and (detail[i].find('曇')) != -1 and (detail[i].find('雪')) == -1:
        files = {'imageFile': open(weather_icon_abspath + 'cloudy_rain.jpg', 'rb')}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)


    elif (detail[i].find('晴')) == -1 and (detail[i].find('雨')) == -1 and (detail[i].find('曇')) != -1 and (detail[i].find('雪')) != -1:
        files = {'imageFile': open(weather_icon_abspath + 'cloudy_snow.jpg', 'rb')}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)


    elif (detail[i].find('晴')) == -1 and (detail[i].find('雨')) == -1 and (detail[i].find('曇')) != -1 and (detail[i].find('雷')) != -1:
        files = {'imageFile': open(weather_icon_abspath + 'cloudy_thunder.jpg', 'rb')}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)


    elif (detail[i].find('晴')) == -1 and (detail[i].find('雨')) == -1 and (detail[i].find('曇')) == -1 and  (detail[i].find('雪')) != -1:
        files = {'imageFile': open(weather_icon_abspath + 'snow.jpg', 'rb')}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)


    elif (detail[i].find('晴')) == -1 and (detail[i].find('雨')) == -1 and (detail[i].find('曇')) == -1 and (detail[i].find('雷')) != -1:
        files = {'imageFile': open(weather_icon_abspath + 'cloudy_thunder.jpg', 'rb')}
        line_notify = requests.post(line_notify_api, data=payload, headers=headers, files=files)

#main function
Parser(rssurl)
for i in range(0,1):
    message = tenki[i]
    payload = {'message': '\n' + message}
    headers = {'Authorization': 'Bearer'+' '+line_notify_token}

    weather_icon(i, detail)

message = URL
payload = {'message': message}
headers = {'Authorization': 'Bearer'+' '+line_notify_token}
line_notify = requests.post(line_notify_api, data=payload, headers=headers)




