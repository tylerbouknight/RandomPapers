# NASA ADS Random Papers and VoIP Notification System

## Overview
This repository, based off the original `ads_rand.py` ([randompapers.net](http://randompapers.net)), hosts two scripts: the original, basic `NASA ADS randomPapers` and its VoIP version with MMS capabilities. While the basic script focuses on fetching random papers from the NASA Astrophysics Data System (ADS), the new addition incorporates the ability to send selected paper details via MMS using a VoIP.ms account, broadening its utility to include automated communication.

## Basic 
1. **Removed Modules**: Removed `os`, `time`, `glob`, and `FeedGenerator` from the original script.
2. **Directory Handling**: Removed directory-related variables and checks.

## VoIP Script
1. **VoIP.ms MMS Integration**: Added functionality to send messages using the VoIP.ms API.
2. **Message Preparation Function**: Formats fetched data into a structured message for sending.
3. **Error Handling**: Improved error checking by verifying the HTTP response status.

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