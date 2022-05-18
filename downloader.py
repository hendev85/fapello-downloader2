# /bin/python3

import re
import requests
import argparse

requests.packages.urllib3.disable_warnings()
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS += ':HIGH:!DH:!aNULL'


parser = argparse.ArgumentParser()
parser.add_argument("model", help="Model name to be downloaded")
args = parser.parse_args()

search_url = 'https://fapello.com//search/' + args.model

response = requests.get(search_url)
match = re.search(
    r'https:\/\/fapello.com\/content\/t\/a.*\d{4}.jpg', response.text)

model_url = match.group().split('_')[0]
model_max_media = match.group().split('_')[1]
model_max_media = model_max_media.split('.')[0]

for i in range(int(model_max_media), 0, -1):
    url = model_url + '_' + str(str(i).zfill(4)) + '.jpg'
    print(url)
    downloaded_file = requests.get(url)
    file_name = url[url.rindex('/')+1:]
    open(file_name, 'wb').write(downloaded_file.content)
