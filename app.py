from flask import Flask, render_template, request, jsonify
from scraper import get_rapidapi_jobs

app = Flask(__name__)

# Home route to render the main page
@app.route('/')
def home():
    return render_template('index.html')

# Search route with pagination and job level filtering
@app.route('/search', methods=['GET'])
def search_jobs():
    location = request.args.get('location') or "Ontario, Canada"
    job_type = request.args.get('job_type') or "software engineer"
    job_level = request.args.get('job_level') or "internship"
    
    # Ensure 'page' is correctly converted to an integer
    page = request.args.get('page', 1)
    
    try:
        page = int(page)  # Explicitly convert to integer
    except ValueError:
        page = 1  # If conversion fails, default to page 1

    # Log the page number for debugging
    print(f"Fetching jobs for page: {page}")

    # Fetch jobs with pagination and job level filtering
    jobs = get_rapidapi_jobs(location, job_type, job_level, page)

    return jsonify(jobs)

if __name__ == '__main__':
    app.run(debug=True)
