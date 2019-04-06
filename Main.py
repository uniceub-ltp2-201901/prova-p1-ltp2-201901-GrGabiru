#Gabriel Rocha Meneses // RA: 21804708

import os
from flask import Flask
from flask import render_template, request
from flaskext.mysql import MySQL
from controle import *

app = Flask(__name__)



mysql = MySQL()

mysql.init_app(app)

app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'Faculdade'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'




@app.route('/')
def menu():
    return render_template('menu.html')
@app.route('/listarprofessores')
def listarprofessores():
    cursor = mysql.get_db().cursor()
    nomes = get_proff(cursor)
    return render_template('listarprofessores.html', nomes=nomes)

@app.route('/exibirprofessor/gabiru')
def exibirprofessor():
    cursor = mysql.get_db().cursor()
    dados = get_data(cursor)
    cursor2 = mysql.get_db().cursor()
    disciplina = get_disciplinas(cursor2)
    return render_template('gabiru.html',dados=dados, disciplinas=disciplina)




if __name__ == "__main__":
    app.run(debug=True)
