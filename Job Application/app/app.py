from flask import Flask, jsonify, render_template, request




app = Flask(__name__)


if __name__ == "__main__":
    app.run(debug=True)
    
# Load data from jobs.json
import json
with open('D:/Job Application/app/jobs.json') as f:
    jobs = json.load(f)

@app.route('/api/jobs', methods=['GET'])
def get_jobs():
    """API to fetch all jobs"""
    return jsonify(jobs)

@app.route('/api/jobs/<int:job_id>', methods=['GET'])
def get_job_by_id(job_id):
    """API to fetch a job by ID"""
    for job in jobs:
        if job['id'] == job_id:
            return jsonify(job)
    return jsonify({'error': 'Job not found'}), 404

@app.route('/')
def index():
    with open('jobs.json') as f:
        jobs_data = json.load(f)
    return render_template('index.html', jobs=jobs_data)

@app.route('/job/<int:job_id>')
def job_details(job_id):
    with open('jobs.json') as f:
        jobs_data = json.load(f)
    job = next((job for job in jobs_data if job['id'] == job_id), None)
    return render_template('details.html', job=job)
