from flask import Flask, request, render_template
from recommendation import return_neighbors

app = Flask(__name__)

@app.route('/home')
def home():
  return render_template('index.html')

@app.route('/admin')
def admin():
  return render_template('index.html')

@app.route('/user', methods=['POST', 'GET'])
def user():
  if request.method == 'POST':
    query = request.form['search']
    lis = return_neighbors(query)
    if lis.empty:
      s = "Something is fishy!! The user Id doesn't exist."
      return s.to_html()
    else:
      return lis.to_html()
  else:
    return render_template('index.html')

if __name__ == '__main__':
  app.run(debug=True)