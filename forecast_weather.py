import os
import requests
import pandas as pd
from bs4 import BeautifulSoup


class ForecastWeather:
    
    def __init__(self, url):
        self.url = url

    def get_web_page(self):
        r = requests.get(self.url)
        if r.status_code != 200:
            raise IOError(f'Unable to download {url}, HTTP {r.status_code}')
        return r

    def parse_page(self):
        r = self.get_web_page()
        soup = BeautifulSoup(r.content, 'html.parser')
        seven_day = soup.find(id="seven-day-forecast")
        return seven_day

    def extract_data(self):
        seven_day = self.parse_page()
        period_tags = seven_day.select(".tombstone-container .period-name")
        periods = [pt.get_text() for pt in period_tags]
        short_descs = [sd.get_text() for sd in seven_day.select(".tombstone-container .short-desc")]
        temps = [t.get_text() for t in seven_day.select(".tombstone-container .temp")]
        descs = [d["title"] for d in seven_day.select(".tombstone-container img")]
        
        weather = pd.DataFrame({
        "period": periods,
        "short_desc": short_descs,
        "temp": temps,
        "desc":descs
        })
        print(weather)
        
            

if __name__ == '__main__':

    URL = "http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168"
    
    obj = ForecastWeather(URL)
    extract = obj.extract_data()
    