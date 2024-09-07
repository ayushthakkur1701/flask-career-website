from flask import Flask, render_template , jsonify
from database import get_all_jobs
app = Flask(__name__)

@app.route("/")
def hello_world():
   JOBS = []
   JOBS = get_all_jobs()
   return render_template('home.html',jobs=JOBS)

@app.route("/api/jobs")
def list_jobs():
  return jsonify(JOBS)


if __name__ == "__main__":
  print("I am inside if now")
  app.run(host='0.0.0.0', debug=True)
