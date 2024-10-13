from flask import Flask, render_template, request, jsonify
from scraper import get_indeed_jobs

app = Flask(__name__)

# Home route to render the main page
@app.route('/')
def home():
    return render_template('index.html')

# Search route to handle job searches
@app.route('/search', methods=['GET'])
def search_jobs():
    location = request.args.get('location')
    job_type = request.args.get('job_type')
    jobs = get_indeed_jobs(location, job_type)
    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
