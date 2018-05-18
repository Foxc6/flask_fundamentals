from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
  return render_template("index.html")

@app.route('/users', methods=['GET', 'POST'])
def create_user():
   print "Got Post Info"

   first_name = request.form['first_name']
   last_name = request.form['last_name']
   email = request.form['email']
   age = request.form['age']
   bio = request.form['bio']

   full_name = first_name + " " + last_name

   return render_template('users.html', full_name = full_name, email = email, age = age, bio = bio)

app.run(debug=True) # run our server