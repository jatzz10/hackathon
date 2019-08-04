from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/home')
def home():
  return render_template('index.html')

@app.route('/admin')
def admin():
  return render_template('index.html')

@app.route('/user')
def user():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)