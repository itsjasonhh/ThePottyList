from app import app
from flask import render_template
@app.route('/')
@app.route('/index')
def index():
	user = {'username': 'Mr. Huang'}
	posts = [
		{
			'author': {'username': 'Mr. Stark'},
			'body': 'Best app ever!'
		},
		{
			'author': {'username': 'Mrs. Pennysworth'},
			'body': 'This app has helped me keep students in the classroom!'
		}

	]
	return render_template('index.html',title='Potty List Homepage',user=user, posts=posts)
	
