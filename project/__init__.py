from flask import Flask
from flask_sqlalchemy import SQLAlchemy


'''
Para criar um servidor web, basta criar uma instancia da classe Flask
= Flask(__name__)

Para rodar o servidor, basta usar o comando no terminal:
'' flask --app arquivo run '' ou
'' flask --app arquivo run --debug ''

'''
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///livros.sqlite3'

db = SQLAlchemy(app)


from project.routes import *
