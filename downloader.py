# /bin/python3

import re
import requests
import argparse

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


parser = argparse.ArgumentParser()
parser.add_argument("model", help="Model name to be downloaded")
parser.add_argument(
    "media_quantity", help="Quantity of media to be downloaded")
args = parser.parse_args()

model_url = 'https://fapello.com/content/' + args.model[0] +'/'+ args.model[1:2]+'/' + \
    args.model

def check_num(no):
    if(no > 8999):
        return('/10000/')
    elif(no > 7999):
        return('/9000/')
    elif(no > 6999):
        return('/8000/')
    elif(no > 5999):
        return('/7000/')
    elif(no > 4999):
        return('/6000/')
    elif(no > 3999):
        return('/5000/')
    elif(no > 2999):
        return('/4000/')
    elif(no > 1999):
        return('/3000/')
    elif(no > 999):
        return('/2000/')
    else:
        return('/1000/')

def videoExists(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok


for i in range(int(args.media_quantity), 0, -1):
    j = check_num(i)
    complete_url = model_url + j + args.model + '_' + str(str(i).zfill(4)) + '.jpg'
    complete_video_url = model_url + j + args.model + '_' + str(str(i).zfill(4)) + '.mp4'
    
    print(complete_url)
    downloaded_file = requests.get(complete_url)
    file_name = complete_url[complete_url.rindex('/')+1:]
    open(file_name, 'wb').write(downloaded_file.content)

    videoAvailable = videoExists(complete_video_url);
    
    if(videoAvailable == True):
        print(complete_video_url)
        downloaded_video_file = requests.get(complete_video_url)
        video_file_name = complete_video_url[complete_video_url.rindex('/')+1:]
        open(video_file_name, 'wb').write(downloaded_video_file.content)
