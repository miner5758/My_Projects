#UNDER HEAVY RECONSTRUCTION! DON"T RUN UNTIL YOU FIX IT!!!!!
from kaggle.api.kaggle_api_extended import KaggleApi
import zipfile
import folium
import os
from opencage.geocoder import OpenCageGeocode
import pandas as pd
import time as t
from sys import exit
import webbrowser


api = KaggleApi()
api.authenticate()

def get_cordinate_data(start):
    lat_list = []
    lng_list = []
    geocoder = OpenCageGeocode(start)
    
    api.dataset_download_files('gpreda/covid-world-vaccination-progress',path=os.getcwd())
    with zipfile.ZipFile(os.getcwd()+'\covid-world-vaccination-progress.zip', 'r') as zipref:
        zipref.extractall(os.getcwd())    
    os.remove(os.getcwd()+"\covid-world-vaccination-progress.zip")
    os.remove(os.getcwd()+"\country_vaccinations_by_manufacturer.csv")
    
    data = pd.read_csv(os.getcwd()+"\country_vaccinations.csv")
    data = data[['country','date','people_vaccinated','people_fully_vaccinated','daily_vaccinations']]
    data = data.drop_duplicates(subset=['country'],keep='last')
    data.index = data['country']
    data = data[['date','people_vaccinated','people_fully_vaccinated','daily_vaccinations']]
    data = data.dropna()
   
    for i in data.index:
        query = str(i)
        results = geocoder.geocode(query)
        lat = results[0]['geometry']['lat']
        lng = results[0]['geometry']['lng']
        lat_list.append(lat)
        lng_list.append(lng)
        t.sleep(3)
    
    data['lat'] = lat_list
    data['lng'] = lng_list
    data.to_csv('worldwide_vaccination_data.csv')
    print('Data has been created, Now making map...')
    make_map('go')




def make_map(start):
    map = folium.Map(location=[20,0], title="Worldwide Vaccination Map", zoom_start=2)
    Data = pd.read_csv(os.getcwd()+"\worldwide_vaccination_data.csv",index_col='country',parse_dates=['date'])

    for i in range(0,len(Data)):
        popup = folium.Popup("{0}, People fully Vaccinated: {1}<br>{0}, People with at least one dose: {2}".format(Data.index[i],Data['people_fully_vaccinated'][i],Data['people_vaccinated'][i]), min_width=320, max_width=320)
        folium.Marker(location=[Data['lat'][i],Data['lng'][i]],popup=popup).add_to(map)
        
    map.save("Worldwide Vaccination Map.html")
    os.remove(os.getcwd()+"\worldwide_vaccination_data.csv")
    os.remove(os.getcwd()+"\country_vaccinations.csv")
    print('Map has been created')
    t.sleep(3)
    url = r'file://' + os.getcwd() + '\Worldwide Vaccination Map.html'
    webbrowser.open(url)

print('In order to use this you must have the kaggle api libary installed, as well as a kaggle api(json file) installed on your computer or whatever compiler your using.')
t.sleep(4)
kaggle = input('Do you meet any of those requirments?')
kaggle = str(kaggle)
kaggle = kaggle.lower()
if kaggle == 'yes':
   pass
elif kaggle == 'no':
    print('go to the kaggle website, create a free account and follow the instuctions on the kaggle api document(it will be opened with the sign up page).')
    t.sleep(8)
    webbrowser.open("https://www.kaggle.com/docs/api")
    webbrowser.open("https://www.kaggle.com/account/login?phase=startRegisterTab&returnUrl=%2F")

    exit()
else:
    print('Answer must be Yes or No.')
    exit()
Api = input('Do you have an opencage api code?')
Api = str(Api)
Api = Api.lower()
if Api == 'yes':
    api_code = input('enter your api code:')
    print('Creating appropriate data...')
    get_cordinate_data(str(api_code))
elif Api == 'no':
    print('go to the opencage website, create a free account and get an api code.')
    t.sleep(4)
    webbrowser.open("https://opencagedata.com/users/sign_up")
    exit()
else:
    print('Answer must be Yes or No.')
    exit()