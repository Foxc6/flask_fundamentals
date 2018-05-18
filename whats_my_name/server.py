from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
	name = request.form['name']
	return render_template('index.html', name=name)

@app.route('/process', methods=['POST'])
def process():	
	return redirect('/')

app.run(debug=True)