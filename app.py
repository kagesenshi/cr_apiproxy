from flask import Flask, request
from flask import Response
import requests

upstream = 'https://api.crunchyroll.com/'

app = Flask('API Forwarder')

@app.route('/', defaults={'path': ''}, methods=['GET','POST'])
@app.route('/<path:path>', methods=['GET','POST'])
def get_response(path):
    if request.method == 'GET':
        r = requests.get(upstream + path + '?' +
            request.query_string.decode('utf8'))
    elif request.method == 'POST':
        if request.form:
            r = requests.post(upstream + path, 
                            data=dict(request.form))
        elif request.json:
            r = requests.post(upstream + path,
                    json=request.json)
    return Response(r.text, mimetype=r.headers.get('Content-Type'))

if __name__ == '__main__':
    app.run()
