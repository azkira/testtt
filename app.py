from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])  
def home():
    return 'udhlah'
    
@app.route("/anjing", methods=['GET'])  
def hello_world():
    return {
    "message": "anjing luh bre"
  }
    
if __name__ == '__main__':
  app.run()