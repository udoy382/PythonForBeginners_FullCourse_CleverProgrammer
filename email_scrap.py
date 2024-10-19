import requests
from bs4 import BeautifulSoup
import re

url = 'https://saifurrahmanudoy.netlify.app/'

# Send a request to the website
r = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

# Find all the email addresses on the page
emails = set(re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(soup)))

# Print the email addresses found
print(emails)
