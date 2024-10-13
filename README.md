# Give Me Opportunity

A simple web application that allows users to search for jobs by location and job type (remote, hybrid, in-person) using the Indeed API.

## Features

- Search jobs based on user input.
- Display job listings with title, company, location, and a link to the job posting.
- Responsive design with a purple, white, and black theme.

## Technologies Used

- Python
- Flask
- Requests
- HTML/CSS
- JavaScript

## Setup Instructions

### Prerequisites

- Python 3.x installed on your system.
- pip (Python package installer).

### Steps

1. **Clone the repository**

   ```
   bash
   git clone https://github.com/AnnChangSal/give-me-opportunity.git
   cd give-me-opportunity
   ```
2. **Create a virtual environment**

   ```
   python -m venv venv
   ```
3. **Activate the virtual environment**

   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```
     source venv/bin/activate
     ```
4. **Install dependencies**

   ```
   pip install -r requirements.txt
   ```
5. **Set up the environment variables**

   Create a `.env` file in the root directory and add the following:
   ```
   INDEED_API_KEY=your_indeed_api_key_here
   ```
6. **Run the application**

   ```
   python app.py
   ```
7. **Access the application**

   Open your web browser and navigate to `http://127.0.0.1:5000`.

## License

This project is licensed under the MIT License. See the `LICENSE` file for more details.
