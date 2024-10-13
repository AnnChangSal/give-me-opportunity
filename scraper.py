import requests
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Function to fetch jobs from RapidAPI with pagination and job level filtering
def get_rapidapi_jobs(location="Ontario, Canada", job_type="software engineer", job_level="internship", page=1):
    RAPID_API_KEY = os.getenv('RAPID_API_KEY')
    URL = "https://jsearch.p.rapidapi.com/search"

    # Map job levels (group internship/co-op/student)
    if job_level == "internship":
        query_job_level = "internship co-op student"
    else:
        query_job_level = job_level

    # Build the query string for the API
    querystring = {
        "query": f"{job_type} {query_job_level} in {location}",
        "page": str(page),  # Pass the page number to the API
        "num_pages": "1",   # Always request one page at a time
        "date_posted": "all"
    }

    headers = {
        "x-rapidapi-key": RAPID_API_KEY,
        "x-rapidapi-host": "jsearch.p.rapidapi.com"
    }

    # Log the API request for debugging
    print(f"Making API request for page: {page}")

    response = requests.get(URL, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        jobs = []
        for job in data.get('data', []):
            title = job.get('job_title') or "No title available"
            company = job.get('employer_name') or "Unknown company"
            location = job.get('location') or "Unknown location"
            job_id = job.get('job_id')
            link = job.get('job_apply_link') or "#"
            description = job.get('job_description', '')[:150] + "..."

            jobs.append({
                'title': title,
                'company': company,
                'location': location,
                'link': link,
                'summary': description,
                'job_id': job_id
            })
        return jobs
    else:
        print(f"Error fetching data from RapidAPI: {response.status_code}, {response.text}")
        return []
