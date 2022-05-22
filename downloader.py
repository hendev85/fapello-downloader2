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

model_url = 'https://fapello.com/content/b/e/' + \
    args.model + '/1000/' + args.model

for i in range(int(args.media_quantity), 0, -1):
    complete_url = model_url + '_' + str(str(i).zfill(4)) + '.jpg'
    print(complete_url)
    downloaded_file = requests.get(complete_url)
    file_name = complete_url[complete_url.rindex('/')+1:]
    open(file_name, 'wb').write(downloaded_file.content)
