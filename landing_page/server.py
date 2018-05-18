from flask import Flask, render_template, request, request, redirect

app = Flask(__name__)

@app.route('/')
def show_welcome():
	return render_template('index.html')

@app.route('/dojos')
def dojos():
  	return render_template("/dojos/new/dojos.html")

@app.route('/ninjas', methods=['GET', 'POST'])
def show_ninja():
	print "Got Post Info"
	name = request.form['name']
	skill = request.form['skill']

	return render_template('/ninjas/ninjas.html', name = name, skill = skill)


app.run(debug=True)
