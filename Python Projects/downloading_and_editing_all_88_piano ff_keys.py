import cloudconvert
import os
import requests
from scipy.io import wavfile
from bs4 import BeautifulSoup
import webbrowser
import sys
import time as t

# I built this code to download a all Piano ff keys and it ended up becoming a whole project of downloading all 88 without losing my connection, converting them into wav files since aiff files suck, and then trimming them to reasonable length, so im gonna put it here

folder = input('which folder would you like to put all the piano keys in?(path):')
folder_of_choice = str(folder)
api_key = str(input('Put you cloud convert api key here:'))
Pianoff = []


def get_piano_keys(go):
    print('Downloading...')
    url = 'https://theremin.music.uiowa.edu/MISpiano.html'
    reqs = requests.get(url)
    soup = BeautifulSoup(reqs.text, 'html.parser')
    for link in soup.find_all('a'):
        if "Piano.ff" in link.get('href'):
            global Pianoff
            Pianoff.append(link.get('href'))
    Pianoff = [y.replace(' ', '%20') for y in Pianoff]
    for link in Pianoff:
        url = 'https://theremin.music.uiowa.edu/' + link
        download_url(url)
    print('Done downloading, now converting to wav file...')
    convert_to_wav('go')
    
    
def download_url(url):
    os.chdir(folder_of_choice)
    print("downloading: ",url)
    # assumes that the last segment after the / represents the file name
    # if url is abc/xyz/file.txt, the file name will be file.txt
    file_name_start_pos = url.rfind("/") + 1
    file_name = url[file_name_start_pos:]
 
    r = requests.get(url, stream=True)
    if r.status_code == requests.codes.ok:
        with open(file_name, 'wb') as f:
            for data in r:
                f.write(data)
    
    
    
def convert_to_wav(go):
    cloudconvert.configure(api_key = api_key, sandbox = False)
    q = next(os.walk(folder_of_choice), (None, None, []))[2]
    for i in q:
        job = cloudconvert.Job.create({
    "tasks": {
         'import-my-file': {
              'operation': 'import/upload',
              'file': os.path.join(folder_of_choice, i)
         },
         'convert-my-file': {
            "operation": "convert",
            "input_format": "aiff",
            "output_format": "wav",
            "engine": "ffmpeg",
            "input": [
                "import-my-file"
            ],
         },
         'export-my-file': {
             "operation": "export/url",
            "input": [
                'convert-my-file'
            ],
            "inline": False,
            "archive_multiple_files": False
         }
     }
 })
        os.chdir(folder_of_choice)
        upload_task_id = job['tasks'][0]['id']
        upload_task = cloudconvert.Task.find(id=upload_task_id)
        Res = cloudconvert.Task.upload(file_name=os.path.join(folder_of_choice, i), task=upload_task)
        exported_url_task_id = job['tasks'][2]['id']
        res = cloudconvert.Task.wait(id=exported_url_task_id) # Wait for job completion
        file = res.get("result").get("files")[0]
        res = cloudconvert.download(filename=file['filename'], url=file['url'])
        print(res)
        os.remove(os.path.join(folder_of_choice, i))
    print('done converting, now trimming...')
    trim_wav(1,8)



def trim_wav(start, end ):
    e = next(os.walk(folder_of_choice), (None, None, []))[2]
    for i in e:
        sampleRate, waveData = wavfile.read(os.path.join(folder_of_choice, i))
        startSample = int( start * sampleRate )
        endSample = int( end * sampleRate )
        wavfile.write(i.replace(".wav", "_trimmed.wav"), sampleRate, waveData[startSample:endSample])
        os.remove(os.path.join(folder_of_choice, i))
    print('All done')


sure = input("Are you SURE you want to run this? dont wanna download a bunch a stuff you don't want(yes or no):")
sure = sure.lower()
if sure == 'yes':
   get_piano_keys('go')
elif sure == 'no':
    sys.exit()
