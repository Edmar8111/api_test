from flask import Flask, g, jsonify
import sqlite3
from time import sleep

app=Flask(__name__)

DATABASE='arquivosApi/database.db'

def requestDBconnect():
    runConn=sqlite3.connect(DATABASE) #efetua a conexão do banco
    runConn.cursor().execute('''
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY AUTOINCREMENT, --ID único, gerado automatico
        name TEXT NOT NULL,                   --Nome de user (campo obrigatorio)
        email TEXT NOT NULL UNIQUE            --Email do user (único e obrigatorio)
    )
    
    ''')
    # runConn.cursor().execute("INSERT INTO user (name, email) VALUES (?, ?)", ("Test", 'EmailTest@gmail.com')) #Efetua a adição de row dos valores na tabela
    # runConn.commit()
    sleep(1)
    runConn.row_factory=sqlite3.Row #converte os valores para dicionario
    return runConn


@app.route('/users')
def getUsers():
    dbRun=requestDBconnect()
    users=dbRun.execute('SELECT * FROM user').fetchall() #executa a query e retorna os valores
    print(users[0]['name'])
    response=[dict(user) for user in users]
    return jsonify(response)
    

if __name__=='__main__':
    app.run(debug=True)