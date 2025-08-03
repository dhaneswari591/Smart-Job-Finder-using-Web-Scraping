from flask import Flask, render_template, request
from job_matcher import find_matching_jobs

app = Flask(__name__)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/results', methods=['POST'])
def results():
    preferences = {
        'title': request.form['title'],
        'skills': request.form['skills'],
        'location': request.form['location'],
        'min_salary': int(request.form['min_salary'])
    }
    matches = find_matching_jobs(preferences)
    return render_template('results.html', matches=matches)

if __name__ == '__main__':
    app.run(debug=True)
