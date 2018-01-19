# -*- encoding: utf-8 -*-

# import os
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import http.client, urllib.parse, json 
from utils import *
from models import *

app = Flask(__name__)  

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

db = SQLAlchemy(app)


@app.route('/', methods=['GET', 'POST'])
@app.route('/desafio_1', methods=['GET', 'POST'])
def desafio_1():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        old_desc = request.form.get('desc')
        desc = corretorOrtografico(old_desc)
        language = textLanguage(desc)
        key = textKey(desc)
        sentiment = textSentiment(desc)

        data = UserSentiment(name, email, desc, language, key, sentiment)
        db.session.add(data)
        db.session.commit()

        msg = 'Dados cadastrados com sucesso!'
    else:
    	msg = ''
    return render_template('desafio_1.html', data=msg)


# @app.route('/envio_desafio_1', methods=['GET', 'POST'])
# def envio_desafio_1():
# 	if request.method == 'POST':
# 		name = request.form.get('name')
# 		email = request.form.get('email')
# 		old_desc = request.form.get('desc')
# 		desc = corretoOrtografico(old_desc)
# 		language = textLanguage(desc)
# 		key = textKey(desc)
# 		sentiment = textSentiment(desc)

# 		data = UserSentiment(name, email, desc, language, key, sentiment)
# 		db.session.add(data)
# 		db.session.commit()

# 	return redirect( url_for('desafio_1/'))


@app.route('/desafio_2', methods=['GET', 'POST'])
def desafio_2():
	#data = ''
	if request.method == 'POST':
		search = request.form.get('search')

		print (search)
		data = searchText(search)
		data = corretorOrtografico(data)
		if data == 'No good match found in the KB':
			data = 'Artigo não encontrado em nossa base de dados, favor digitar novamente.'
	else:
		data = ''

	return render_template('desafio_2.html', data=data)


@app.route('/desafio_3')
def desafio_3():

	user = UserSentiment.query.all() 
	return render_template('desafio_3.html', user=user)


if __name__ == '__main__':
	app.run(debug=True)