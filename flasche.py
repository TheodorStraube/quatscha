from bottle import Bottle, route, run, view, static_file, get, post

import random
from pathlib import Path

from read_pandas import load_parque

app = Bottle()

alle_bilder = list(p.name for p in Path('assets/images/').iterdir())
print(alle_bilder[:2])

@get('/')
@view('index.tpl')
def index():
    return {"name": "Brigitte"}


@get('/hello')
def hello():
    return "HI"

@post('/submitImage/<img>')
def submitImage(img):
    selected_image = random.choice(alle_bilder)
    return f'<img id="gridcell_{img}" src="/static/images/{selected_image}">'

@get('/static/<filepath:path>')
def server_static(filepath):
    return static_file(filepath, root='assets/')

if __name__ == '__main__':
    app.run(host='localhost', port=8080, debug=True, reloader=True)


class CatptchaGame:
    pass
