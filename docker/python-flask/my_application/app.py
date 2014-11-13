from flask import Flask
from flask import request
from os import listdir
from os.path import isfile, join
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/list")
def listfiles():
	filelist = [f for f in listdir(mypath) if isfile(join(mypath,f)) ]
	return(filelist)

@app.route("/Euler1")
def Euler1():
  finalsum = 0
  for i in range(1000):
    if i % 3 == 0:
      finalsum += i
    elif i % 5 == 0:
      finalsum += i
  return(finalsum)

@app.route("/Euler2")
def Euler2():
  x, y = 1, 1
  finalsum = 0
  while x <= 4000000:
    if x % 2 == 0:
      finalsum += x
    x, y = y, x+y
  print(finalsum)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save('./uploads/'+f.filename)
    return '',201
if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
