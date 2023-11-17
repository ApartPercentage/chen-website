from flask import Flask, jsonify, render_template, request
import pickle

with open("models/1/cv.pkl", "rb") as tokenized:
  tokenizer = pickle.load(tokenized)

with open("models/1/clf.pkl", "rb") as email_model:
  esc_model = pickle.load(email_model)
#tokenizer = pickle.load(open("models/1/cv.pkl", "rb"))
#esc_model = pickle.load(open("models/1/clf.pkl", "rb"))


app = Flask(__name__) # created Flask application

PROJECTS = [
  {
  'id': 1,
  'title': 'First',
  'description': 'First project'
  },
  {
  'id': 2,
  'title': 'Second',
  'description': 'Second project'
  }
]

@app.route("/") #register a route to the application
def hello_world():
  return render_template('home.html', projects = PROJECTS, my_name = 'Chen')

@app.route("/api/projects")
def list_projects():
  return jsonify(PROJECTS)

@app.route('/project/<int:project_id>', methods = ["GET", "POST"])
def project(project_id):
    # Add code to retrieve project details based on project_id
    # For example: project = get_project_by_id(project_id)
    # Then pass the project details to the template
    # return render_template('project_detail.html', project=project)
    project = next((p for p in PROJECTS if p['id'] == project_id), None)
    if project is None:
      return "Project not found"
    else:
      template_name = f"{project_id}.html"
      return render_template(template_name, project=project)

@app.route('/project/1/predict', methods = ["POST"])
def predict_1():
  email= request.form.get("content")
  tokenized_email = tokenizer.transform([email])
  prediction = esc_model.predict(tokenized_email)
  prediction = 1 if prediction == 1 else -1
  return render_template("1.html", prediction = prediction, email = email)

if __name__ == "__main__":  #check if running app.py as a script, then start the app using Run
  app.run(host = '0.0.0.0', debug = True) #0000 runs locally