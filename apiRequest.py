from flask import Flask, jsonify, request, request, abort, url_for, render_template
import os
from markupsafe import escape, Markup
import pandas as pd
from werkzeug.utils import secure_filename
from werkzeug.datastructures import FileStorage

from io import BytesIO, StringIO

class requestXLSX:
    def __init__(self, lista):
        self.lista=[]
        #pd.read_excel('Controle Contábil Geral 2025 - 13.02.2025.xlsx')['CNPJ/CPF/CAEPF']
        #pd.read_excel('Controle Contábil Geral 2025 - 13.02.2025.xlsx')['Municipio - Estado'] 'CUIABÁ-MT'
        for i in range(len(pd.read_excel('Controle Contábil Geral 2025 - 13.02.2025.xlsx')['CNPJ/CPF/CAEPF'])):
            if pd.read_excel('Controle Contábil Geral 2025 - 13.02.2025.xlsx')['Municipio - Estado'][i]=='CUIABÁ-MT':
                self.lista.append(pd.read_excel('Controle Contábil Geral 2025 - 13.02.2025.xlsx')['CNPJ/CPF/CAEPF'][i])
        print(self.lista)
        return None
    def requestFile(self, endpoint):
        return self.lista

app=Flask(__name__)

listagem=[]

#efetua a requisição atraves do name indicado na url
@app.route('/api/<name>/<int:post_id>', methods=['GET'])
def requestApi(name, post_id):
    data=[name, post_id]
    aninhamento_escape=[escape(i) for i in data]
    print(aninhamento_escape[1][0])
    return f'request api: {'Name:'+aninhamento_escape[0][0]+' ID: '+aninhamento_escape[1][0]}'

#metodo para acessar a pasta
BASE_DIR=os.path.abspath('xmlFolder')
@app.route('/xmlFolder/<path:parametro>', methods=['GET'])
def requestSubPath(parametro):
    pathDirect=os.path.abspath(os.path.join(BASE_DIR, parametro))
    
    #Impede path transversal: recusa acessos pastas acima de BASE_DIR
    if not BASE_DIR:
        abort(403)
    #lista os arquivos
    if os.path.isdir(pathDirect):
        file=os.listdir(pathDirect)
        return f'conteudo da pasta: {escape(parametro)} '+" ".join(f'{escape(i)}' for i in file)
    #Retorna o arquivo(caso seja arquivo)
    elif os.path.isfile(pathDirect):
        return f'Return parametro arquivo direto: {escape(parametro)}'
    else:
        abort(404)#not found path

#requisição dos dados de uma arquivo para retornar a api
@app.route('/project/', methods=['GET'])
def requestApiPOST():
    returnF=requestXLSX(list()).requestFile('')
    return jsonify(returnF)

#metodos de requisição com condição ativa de redirecionamento
@app.route('/data', methods=['GET', 'POST'])
def login():
    if request.method=="GET":
        return listagem 
    else:
        listagem.append(0)
        return 'Request POST'


#requisita o arquivo html via a pasta templates
@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', person=name)



#UPLOAD ARQUIVOS EFETUA O UPLOAD DE ARQUIVOS VIA FRONT 
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method=='POST':
        #requisição do arquivo por parte do cliente
        f0=request.files['the_file']
        print(f0)
        
        #requisita atraves do back de arquivos especificados pelo usuario
        with open('templates/hello.html', 'r') as file:
            f=file.read()
        #executa a conversão do arquivo para Bytes
        f=FileStorage(
            stream=BytesIO(f.encode('utf-8')),
            filename='valor.xml',
            content_type='text/plain' #gera arquivo direto a texto
            )
            
        f.save(os.path.join(os.path.abspath('arquivosApi'), secure_filename(f.filename)))
        return 'Arquivo Salvo!'
    else:
        return 'dados'
    return ''



#Retorna a requisição da url via function name
with app.test_request_context():
    print(url_for('requestApiPOST', next='/'))
    print(url_for('requestApi', name='Edmar', post_id=0))

    #requisita o arquivo css direto
    print(url_for('static', filename='style.css'))
    print(url_for('static', filename='script.js'))

#Define o metodo http e o path a ser efetuado o teste de requisição
with app.test_request_context('/data', method='POST'):   
    print('Caminho: ', request.path)
    print('Método HTTP: ', request.method)
    #verifica se a requisição esta confome passado no WITH
    assert request.path=='/data'
    assert request.method=='POST',f'Aguardo de POST, retornando: {request.method}'
    #Efetua requisição direto da url via return especificado do metodo
    print(login())

#Efetua a requisição da url via POST ou GET
with app.test_client() as client:
    response=client.post('/data')
    print(response.data.decode())


if __name__ == '__main__':
    app.run(debug=True)