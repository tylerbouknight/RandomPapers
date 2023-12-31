# NASA ADS Random Papers and VoIP Notification System

## Overview
This repository, based off the original `ads_rand.py` ([randompapers.net](http://randompapers.net)), hosts two scripts: the original, basic `NASA ADS randomPapers` and its VoIP version with MMS capabilities. While the basic script focuses on fetching random papers from the NASA Astrophysics Data System (ADS), the new addition incorporates the ability to send selected paper details via MMS using a VoIP.ms account, broadening its utility to include automated communication.

## Key Features
- **Automated MMS Feature**: The VoIP script can send paper details through MMS, offering a unique way to share research articles.
- **Simplified Date Handling**: Automatically calculates the current date and adjusts the search to the previous month, ensuring up-to-date queries.
- **Refined Search Query**: A focused API request using the calculated `pubdate` fetches relevant data, catering to specific research needs.
- **Streamlined Codebase**: Removal of extraneous code for cleaner, more maintainable structure.

## VoIP Script
1. **VoIP.ms MMS Integration**: Added functionality to send messages using the VoIP.ms API.
2. **Message Preparation Function**: Formats fetched data into a structured message for sending.
3. **Error Handling**: Improved error checking by verifying the HTTP response status.
4. **Removed Modules**: Discarded `os`, `time`, `glob`, and `FeedGenerator` from the original script.
5. **Directory Handling**: Removed directory-related variables and checks.
6. **Date Calculation Logic**: New mechanism for automatic date range determination.
7. **Simplified API Request**: Enhanced API request structure for efficiency.

## Usage

### Basic Script
Run the script in a Python environment with the necessary dependencies installed. You'll need an API key for ADS. The script outputs a list of paper titles with their links.

### VoIP Script
Before running the enhanced script, you need a VoIP.ms account and its associated credentials. After setting up your account, configure the script with your VoIP.ms API username, password, and DID number. Also, provide your recipient phone number in the script. This script then fetches random papers and sends their details via MMS to the specified phone number.

#### Setting up VoIP.ms
1. **Create an Account**: Sign up at [VoIP.ms](https://voip.ms/).
2. **Configure API Access**: In your VoIP.ms dashboard, navigate to `API Configuration` to set up and retrieve your API credentials.
3. **Get a DID Number**: Purchase a DID number from VoIP.ms, which will be used as the sender ID in your messages.

### Dependencies

- `requests`: For making HTTP requests to the ADS and VoIP.ms APIs.
- `numpy`: For random selection of papers.
- `datetime`: To determine the current date and calculate the search month/year.
- `re`: For regular expression operations, especially in DOI handling.

---