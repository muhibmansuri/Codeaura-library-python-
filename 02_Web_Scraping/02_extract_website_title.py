# ==========================================
# Codeaura Python Course: 02_extract_website_title.py
# ==========================================
# Concept: HTTP Requests & BeautifulSoup
# Real Life Example: Ek machine jo kisi bhi website ko khol kar uska naam (Title) padh sakti hai.

import requests
from bs4 import BeautifulSoup

print("--- Website Title Reader ---")

# Hum Python ki official website ka data nikalenge
url = "https://www.python.org/"
print(f"Connecting to {url} ...\n")

# Step 1: Website ka poora code (HTML) download karna
response = requests.get(url)

# Agar response 200 hai, matlab connection successful!
if response.status_code == 200:
    print("Connection Successful! Downloading data...\n")
    
    # Step 2: BeautifulSoup ki madad se code me se Title nikalna
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # <title> tag ko dhoondhna
    website_title = soup.title.string
    
    print(f"Result: The title of the website is: '{website_title}'")
else:
    print("Oops! Internet connection problem ya website galat hai.")

# Note for Students: Aap 'url' me kisi aur website (jaise wikipedia) ka link daal kar try karein!
