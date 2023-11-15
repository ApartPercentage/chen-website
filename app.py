from flask import Flask

app = Flask(__name__) # created Flask application

@app.route("/") #register a route to the application
def hello_world():
  return "Hello World"

if __name__ == "__main__":  #check if running app.py as a script, then start the app using Run
  app.run(host = '0.0.0.0', debug = True) #0000 runs locally