from flask import Flask
 
app = Flask(__name__)
 
@app.route('/')
def home():
   return "Hello Everyone,This is Krushna's Flask Server Version 1 Added!"
 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)