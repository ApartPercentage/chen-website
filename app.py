from flask import Flask, render_template, jsonify

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

@app.route('/project/<int:project_id>')
def project(project_id):
    # Add code to retrieve project details based on project_id
    # For example: project = get_project_by_id(project_id)
    # Then pass the project details to the template
    # return render_template('project_detail.html', project=project)
    return f"Project {project_id} details"

if __name__ == "__main__":  #check if running app.py as a script, then start the app using Run
  app.run(host = '0.0.0.0', debug = True) #0000 runs locally