from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)


@app.route('/savedata')
def addstring():
    return render_template('addstring.html')

@app.route('/savedata', methods = ['POST', 'GET'])
def saved():    
    if request.method == 'POST':
	word = request.form['string']

	db = sqlite3.connect('data.db')
        db.execute('CREATE TABLE IF NOT EXISTS Strings (Entry)')
	db.execute('INSERT INTO Strings (Entry) values (?)', [word] )
	db.commit()
	db.close()
	return render_template('saved.html')

@app.route('/displaydata', methods = ['POST', 'GET'])
def displaydata():
    db = sqlite3.connect('data.db')
    c = db.execute('SELECT Entry FROM Strings')
    words = c.fetchall()
    return render_template('display.html', words=words)
			
if __name__ == '__main__':
   app.run(debug = True)
