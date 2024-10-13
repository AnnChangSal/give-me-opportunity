import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_indeed_jobs(location, job_type):
    # Get the API key from the environment variable
    API_KEY = os.getenv('INDEED_API_KEY')
    if not API_KEY:
        raise ValueError("No API key found. Make sure to set INDEED_API_KEY in your .env file.")

    URL = "https://api.indeed.com/ads/apisearch"

    params = {
        'publisher': API_KEY,  # Use API key from the .env file
        'q': job_type,         # Job type query (e.g., remote, hybrid, etc.)
        'l': location,         # Location (e.g., city, region)
        'format': 'json',      # Response format
        'v': '2',              # API version
        'limit': 10            # Number of job results to return
    }

    response = requests.get(URL, params=params)
    
    if response.status_code == 200:
        data = response.json()
        jobs = []
        for job in data.get('results', []):
            title = job.get('jobtitle')
            company = job.get('company')
            location = job.get('formattedLocation')
            link = job.get('url')
            jobs.append({
                'title': title,
                'company': company,
                'location': location,
                'link': link
            })
        return jobs
    else:
        print("Error fetching data from Indeed API.")
        return []
