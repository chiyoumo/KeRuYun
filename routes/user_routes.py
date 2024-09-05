from routes import app
from flask import render_template

@app.route('/about.html')
def about_page():
    return render_template('about.html')

@app.route('/home.html')
def home_page():
    return render_template('home.html')