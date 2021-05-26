import requests
import os
from datetime import date, datetime
from time import time, sleep

def get_path():
    today = date.today().strftime("%Y-%m/%Y-%m-%d")
    path = "images/"  + today
    if not os.path.exists(path):
        os.makedirs(path , exist_ok=True)

    return path


def download():
    save_as_filename=datetime.now().strftime("%Y-%m-%d-%H-%M") + ".jpg"
    save_as=get_path() + "/" + save_as_filename
    print("Downloading to " + save_as)

    #set the URL of the downloadable resource here:
    url = 'https://picsum.photos/500/300?random=1'

    r = requests.get(url, allow_redirects=True)
    open(save_as, 'wb').write(r.content)


while True:
    download()

    #Wait for a whole minute: (12:00, 12:01, 12:02 ...)
    sleep(60 - time() % 60)
