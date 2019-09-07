from flask import Flask, request, render_template
from recommendation import return_neighbors
from redis import Redis


app = Flask(__name__)
redis = Redis(host='redis', port=6379)



@app.route('/home')
def home():
  redis.rpush("key_local", "hitted")
  print("here")
  print("redis is ",redis.lrange("key_local",0,-1))
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
      return s
    else:
      return lis.to_html()
  else:
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)