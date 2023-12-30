# NASA ADS randomPapers

## Overview
This script is a modified version of the original `ads_rand.py` ([randompapers.net](http://randompapers.net)), tailored to streamline the process of fetching random papers from the NASA Astrophysics Data System (ADS). Focused on simplicity and efficiency, this version introduces several key changes to optimize the user experience and adapt the script to more specific use cases.

## Key Features
- **Simplified Date Handling**: The script now automatically calculates the current date and adjusts the search to the previous month, ensuring up-to-date queries without manual input.
- **Refined Search Query**: By constructing a focused API request using the calculated `pubdate`, the script efficiently fetches relevant data, aligning with users' needs for current and specific research articles.
- **Streamlined Codebase**: Removal of extra modules and code sections like file handling and feed generation, leading to a cleaner, more maintainable code structure.

## Modifications from Original Script
1. **Removed Modules**: Discarded the use of `os`, `time`, `glob`, and `FeedGenerator`.
2. **Directory Handling**: Removed directory-related variables and checks.
3. **Date Calculation Logic**: Implemented a new mechanism to automatically determine the search date range based on the current month and year.
4. **Simplified API Request**: Overhauled the API request structure for enhanced efficiency and relevancy.

## Usage

Run the script in a Python environment with necessary dependencies installed. Ensure you have an API key for ADS. The script will output a list of paper titles along with their respective links.

### Dependencies

- `requests`: For making HTTP requests to the ADS API.
- `numpy`: For random selection of papers.
- `datetime`: To determine the current date and calculate the search month/year.
- `re`: For regular expression operations related to DOI handling.

---

Feel free to modify and expand this README to better fit the specifics of your project 