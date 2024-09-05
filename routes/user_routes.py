from routes import app


@app.route('/about.html')
def about_page():
    return "About Page"