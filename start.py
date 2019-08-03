from flask import Flask, request, render_template
from plot_function import city
app = Flask(__name__)

@app.route('/admin', methods = ["POST", "GET"])
def admin():

    return render_template('index.html')
@app.route('/user')
def index():
  return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)