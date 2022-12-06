import time
from os import unlink

import requests
from fastapi import FastAPI, Form

from ykocr import ykocr

app = FastAPI()

@app.post("/")
def read_root(imgUrl: str = Form()):
    img = requests.get(imgUrl).content
    path = 'runtime/' + str(time.time())+'.png'
    with open(path, 'wb') as f:
        f.write(img)
    res = ykocr()
    res = res.imgToText(path)
    unlink(path)
    return {'result': res}
