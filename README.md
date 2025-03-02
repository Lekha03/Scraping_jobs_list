# Scraping_jobs_list
# Scraping Job Listings from Indeed

## Description
This repository contains a Python script that scrapes job listings from Indeed based on user input for the number of jobs required. The extracted job data is stored in `jobs.csv`.

## Features
- Scrapes job listings from Indeed.
- Allows users to specify the number of jobs to scrape.
- Extracted data includes job title, company, location, and job link.
- Saves data in `jobs.csv` for easy analysis.

## Installation

### Prerequisites
Ensure you have:
- Python 3.x installed.
- Required dependencies listed in `requirements.txt`.

### Steps to Install
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Scraping_Job_List_Indeed.git
   cd Scraping_Job_List_Indeed
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the script:
   ```bash
   python script.py
   ```
2. Enter the number of job listings to scrape when prompted.
3. The script will fetch job details from Indeed and store them in `jobs.csv`.
4. Output format:
   ```csv
   Job Title, Company, Location, Job Link
   Software Engineer, ABC Corp, New York, https://indeed.com/job/123
   ```

## Configuration
- Modify `script.py` to change search parameters (e.g., job title, location).
- Ensure compliance with Indeed’s scraping policies to avoid IP blocking.

## Contributing
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-branch`).
3. Commit your changes (`git commit -m 'Add new feature'`).
4. Push to the branch (`git push origin feature-branch`).
5. Submit a Pull Request.

## License
This project is licensed under the MIT License.

## Contact
For any issues or feature requests, please open an issue on the repository.

