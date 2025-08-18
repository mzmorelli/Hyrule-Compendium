from flask import render_template, request, url_for, redirect
import urllib.request
import json

def init_app(app):
    @app.route('/', methods=['GET', 'POST'])
    @app.route('/<int:id>', methods=['GET', 'POST'])
    def home(id=None):
        urlApi = 'https://botw-compendium.herokuapp.com/api/v3/compendium/all'
        response = urllib.request.urlopen(urlApi)
        apiData = response.read()
        jsonData = json.loads(apiData)
        
        data = jsonData['data'] if 'data' in jsonData else []
        
        if id:
            entryInfo = None
            for entry in data:
                if entry['id'] == id:
                    entryInfo = entry
                    break
            if entryInfo:
                return render_template('info.html', entryInfo=entryInfo, entry=entry)
            else:
                return f'Entrada com a ID {id} não foi encontrada.'
            
        return render_template('index.html', data=data)