import sqlite3
from flask import Flask, request, redirect, url_for, g, render_template, flash, session, abort
import sys
sys.path.append('/home/ouwen/cs410/project/sys/controller')
from authorhelper import *

DEBUG = True
SECRET_KEY = 'development key'
USERNAME = '1@hotmail.com'
PASSWORD = '1'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    	if not session.get('logged_in'):
    		return render_template('index.html')
	else:
		return render_template('result.html')

@app.route('/check1', methods=['GET', 'POST'])
def check1():
    	if request.method == 'POST':
        	if request.form['username'] != app.config['USERNAME']:
            		error = 'Invalid username'
        	elif request.form['password'] != app.config['PASSWORD']:
            		error = 'Invalid password'
        	else:
	    		session['logged_in'] = True
			username=request.form['username']
			password=request.form['password']
			return render_template('result.html',username=username,password=password)
    	return render_template('index.html', error=error)

@app.route('/check', methods=['GET', 'POST'])
def check():
	if request.method == 'POST':
		dbhelper = Databasehelper()
		username = request.form['username']
		pwd = request.form['password']
		ahelper = AuthorHelper()
		check=ahelper.authorauthenticate(dbhelper,username,pwd)
		if check == True:
			session['logged_in'] = True
			return render_template('result.html',username=username,password=password)
		else:
			error = 'Invalid username or password'
    	return render_template('index.html', error=error)

@app.route('/register', methods=['PUT', 'POST'])
def register():
	username=request.form['register_username']
	password=request.form['register_password']
	return render_template('result.html',username=username,password=password)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.debug = True
    app.run()
