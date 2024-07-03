from flask import render_template
from app import app 

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Nala'}
    posts = [
        {
            'author': {'username': 'Jonesma'},
            'body': 'Beautiful day in Missouri!'
        },
        {
            'author': {'username': 'Walter'},
            'body': 'Nightmare before Christmas was great!'
        },
        
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
    
