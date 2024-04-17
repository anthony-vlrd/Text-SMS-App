# SMS App

## Overview
The SMS App is a Python script designed to send SMS messages using the Twilio API. This script reads phone numbers from a CSV file, cleans them to ensure they are in a valid format, and then uses the Twilio API to send a predefined message to each cleaned phone number.

## Author
- Anthony Velarde, 2024

## Requirements
- Python 3.x
- Pandas Library
- Twilio Python Library

## Setup
1. **Install Required Libraries**:
    ```bash
    pip install pandas twilio
    ```

2. **Twilio Account**:
    - Sign up for a Twilio account at https://www.twilio.com.
    - Get your `Account SID` and `Auth Token` from the Twilio console.
    - Purchase an SMS-capable phone number.

3. **Environment Variables**:
    - It's recommended to store your Twilio credentials (`Account SID` and `Auth Token`) in environment variables or a secure place that is not hard-coded into your scripts.

4. **CSV File Format**:
    - Ensure you have a CSV file named `contacts-test.csv` with at least one column named `phone` that contains the phone numbers.

## Usage
1. **Configuration**:
    - Replace `'ACCOUNT_SID'` and `'AUTH_TOKEN'` in the script with your actual Twilio account SID and auth token, or modify the script to load them from environment variables.

2. **Running the Script**:
    - Execute the script from your terminal:
        ```bash
        python sms_app.py
        ```

## Example
The script will process phone numbers from `contacts-test.csv`, clean them to ensure they are in the correct format (e.g., '+11234567890'), and send a message that says "Message to send out. :)" to each number.

## Error Handling
- The script includes basic error handling for sending messages. If an error occurs while sending an SMS, it will print "an error occurred" to the console.


