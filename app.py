from flask import Flask, jsonify, render_template, request
from utils import esc_prediction
import requests
import json

app = Flask(__name__)  # created Flask application

PROJECTS = [{
    'id':
    1,
    'title':
    'Email Spam Classifier',
    'description':
    'This is a project used to classify any Spam mails from the texts of emails given. \nAlgorithm used for this model: Naive Bayes'
}, {
    'id': 2,
    'title': 'Marvel Character Recognition',
    'description': 
    'This is a project used to recognize Marvel characters based on eight characters: doctor strange, black widow, spider-man, captain america, thor, hulk, loki, and ironman. Algorithm used for this model: Vision Transformer (ViT)'
}]


@app.route("/")  #register a route to the application
def hello_world():
  return render_template('home.html', projects=PROJECTS, my_name='Chen')
  
@app.route("/api/projects")
def list_projects():
  return jsonify(PROJECTS)

@app.route('/project/<int:project_id>', methods=["GET", "POST"])
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


@app.route('/project/1/predict', methods=["POST"])
def predict_1():
  email = request.form.get("content")
  prediction = esc_prediction(email)
  return render_template("1.html", prediction=prediction, email=email)


@app.route('/project/1/api/predict', methods=["POST"])
def api_predict_1():
  data = request.get_json(force=True)
  email = data['content']
  prediction = esc_prediction(email)
  return jsonify({'prediction': prediction, 'email': email})


@app.route('/project/2/predict', methods=['POST'])
def predict_2():
  file = request.files['file']

  # Make a request to Marvel character recognition service
  response = requests.post(
      "https://marvel-character-recognition-xe6khmu5bq-lm.a.run.app/predict_image",  # Replace with your actual Google Cloud Run endpoint
      headers={
          "accept": "application/json",
          "Content-Type": "image/jpeg",
      },
      data=file,
  )

  # Parse the JSON response
  result = json.loads(response.text)

  # Display the result on the webpage
  return render_template('2.html', result=result)


if __name__ == "__main__":  #check if running app.py as a script, then start the app using Run
  app.run(host='0.0.0.0', debug=True)  #0000 runs locally
