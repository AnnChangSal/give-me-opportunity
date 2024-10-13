let currentPage = 1;  // Track the current page

// Event listener for the search button
document.getElementById('search-button').addEventListener('click', function() {
    currentPage = 1;  // Reset to page 1 when a new search is made
    document.getElementById('job-results').innerHTML = '';  // Clear previous results
    searchJobs();
});

// Event listener for the Next button
document.getElementById('next-page').addEventListener('click', function() {
    currentPage++;  // Increment the page number
    searchJobs();
});

// Event listener for the Previous button
document.getElementById('prev-page').addEventListener('click', function() {
    if (currentPage > 1) {
        currentPage--;  // Decrement the page number (if not on the first page)
        searchJobs();
    }
});

// Function to fetch and display jobs
function searchJobs() {
    const jobType = document.getElementById('job_type').value || "software engineer";
    const location = document.getElementById('location').value || "Ontario, Canada";
    const jobLevel = document.getElementById('job_level').value;

    // Log the current page to the console for debugging
    console.log(`Fetching page ${currentPage}`);

    // Fetch jobs from the server with the current page number
    fetch(`/search?location=${location}&job_type=${jobType}&job_level=${jobLevel}&page=${currentPage}`)
        .then(response => response.json())
        .then(data => {
            const resultsDiv = document.getElementById('job-results');
            resultsDiv.innerHTML = '';  // Clear previous results

            if (data.length === 0) {
                resultsDiv.innerHTML = '<p>No jobs found.</p>';
            } else {
                // Display the fetched job results
                data.forEach(job => {
                    const jobDiv = document.createElement('div');
                    jobDiv.className = 'job-listing fade-in';
                    jobDiv.innerHTML = `
                        <h3>${job.title}</h3>
                        <p>${job.company} - ${job.location}</p>
                        <a href="${job.link}" target="_blank" class="btn btn-primary">More Details</a>
                        <p>${job.summary}</p>
                    `;
                    resultsDiv.appendChild(jobDiv);
                });
            }

            // Enable or disable pagination buttons
            document.getElementById('prev-page').disabled = currentPage === 1;
            document.getElementById('next-page').disabled = data.length < 10;  // Disable 'Next' if fewer than 10 results
        })
        .catch(error => {
            console.error('Error fetching jobs:', error);
        });
}
