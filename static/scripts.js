document.getElementById('search-button').addEventListener('click', searchJobs);

function searchJobs() {
    const location = document.getElementById('location').value;
    const jobType = document.getElementById('job_type').value;
    
    fetch(`/search?location=${location}&job_type=${jobType}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('job-results');
            resultsDiv.innerHTML = '';
            if (data.length === 0) {
                resultsDiv.innerHTML = '<p>No jobs found.</p>';
            } else {
                data.forEach(job => {
                    const jobDiv = document.createElement('div');
                    jobDiv.className = 'job-listing';
                    jobDiv.innerHTML = `
                        <h3>${job.title}</h3>
                        <p>${job.company} - ${job.location}</p>
                        <a href="${job.link}" target="_blank">View Job</a>
                    `;
                    resultsDiv.appendChild(jobDiv);
                });
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
