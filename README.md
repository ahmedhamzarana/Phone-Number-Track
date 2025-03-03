Phone Number Information Extractor

This script extracts detailed information about a given phone number using the phonenumbers library in Python.

Features

Extracts the national number and country code.

Identifies the location of the phone number.

Retrieves the time zone associated with the number.

Identifies the service provider (carrier).

Fetches the country name.

Requirements

Ensure you have Python installed on your system. You also need to install the phonenumbers library.

Installation

Run the following command to install the required library:

pip install phonenumbers

Usage

Run the script:

python script.py

Enter a phone number in international format (e.g., +14155552671).

The script will output details about the number, including:

National Number

Country Code

Location

Time Zone

Service Provider

Country Name

Example Output

Enter your phone number: +14155552671
National Number: 4155552671
Country Code: 1
Location: United States
Time Zone: ('America/Los_Angeles',)
Service Provider: AT&T
Country Name: United States

Notes

Ensure you enter a valid phone number in the correct format.

The accuracy of information depends on the phonenumbers library database.

License

This project is open-source and can be modified as needed.
