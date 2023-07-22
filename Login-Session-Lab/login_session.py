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
			login_session.setdefault('quote', []).append(quote)
			login_session.setdefault('name', []).append(name)
			login_session.setdefault('age', []).append(age)
			return redirect(url_for('thanks'))
		except:
			return redirect(url_for('error'))
	return render_template('home.html')

@app.route('/error')
def error():

	return render_template('error.html')


@app.route('/display')
def display():
	return render_template('display.html', l= login_session) # What variables are needed?


@app.route('/thanks', methods= ['GET', 'POST'])
def thanks():

	return render_template('thanks.html')


if __name__ == '__main__':
	app.run(debug=True)