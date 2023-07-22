from flask import Flask, render_template, request, url_for, redirect
from flask import session as login_session

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super-secret-key'

@app.route('/', methods= ['GET', 'POST'] ) # What methods are needed?
def home():
	if request.method == 'POST':
		try:
			quote = request.form['quote']
			name = request.form['name']
			age = request.form['age']
			login_session['quote'] = quote
			login_session['name'] = name
			login_session['age'] = age
			return redirect(url_for('thanks'))
		except:
			return redirect(url_for('error'))
	return render_template('home.html')

@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():
	return render_template('display.html', q= login_session['quote'], n=login_session['name'], a=login_session['age'] ) # What variables are needed?


@app.route('/thanks', methods= ['GET', 'POST'])
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)