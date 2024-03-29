from flask import Flask, render_template, jsonify

app = Flask(__name__)

JOBS = [
  {

    'id' : 1, 
    'title': 'Data Analyst', 
    'location': 'Utrecht', 
    'salary': 'Euro. 3500'
  },
  {

    'id' : 2, 
    'title': 'Data Analyst', 
    'location': 'Utrecht',
    'salary': 'Euro. 3500'
  },
 {

    'id' : 3, 
    'title': 'Frontend engineer',
    'location': 'Amsterdam',
    
  },
 {

    'id' : 4, 
    'title': 'Backend engineer',
    'location': 'San francisco',
    'salary': 'Euro. 3500'
  },
]

@app.route("/")
def hello_world():
    return render_template('home.html', 
                           jobs=JOBS,
                          )
@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
  
  

