from flask import render_template, request, url_for, redirect
import urllib.request
import json

def init_app(app):
    
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/creatures', methods=['GET', 'POST'])
    @app.route('/creatures/<int:id>', methods=['GET', 'POST'])
    def creatures(id=None):
        urlApi = 'https://botw-compendium.herokuapp.com/api/v3/compendium/category/creatures'
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
            
        return render_template('creatures.html', data=data)
    
    @app.route('/monsters', methods=['GET', 'POST'])
    @app.route('/monsters<int:id>', methods=['GET', 'POST'])
    def monsters(id=None):
        urlApi = 'https://botw-compendium.herokuapp.com/api/v3/compendium/category/monsters'
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
            
        return render_template('monsters.html', data=data)
    
    @app.route('/materials', methods=['GET', 'POST'])
    @app.route('/materials/<int:id>', methods=['GET', 'POST'])
    def materials(id=None):
        urlApi = 'https://botw-compendium.herokuapp.com/api/v3/compendium/category/materials'
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
            
        return render_template('materials.html', data=data)
    
    @app.route('/equipment', methods=['GET', 'POST'])
    @app.route('/equipment/<int:id>', methods=['GET', 'POST'])
    def equipment(id=None):
        urlApi = 'https://botw-compendium.herokuapp.com/api/v3/compendium/category/equipment'
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
            
        return render_template('equipment.html', data=data)
    
    @app.route('/treasure', methods=['GET', 'POST'])
    @app.route('/treasure/<int:id>', methods=['GET', 'POST'])
    def treasure(id=None):
        urlApi = 'https://botw-compendium.herokuapp.com/api/v3/compendium/category/treasure'
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
            
        return render_template('treasure.html', data=data)