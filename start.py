from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/admin')
def admin():
  return render_template('index.html')

@app.route('/user')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)