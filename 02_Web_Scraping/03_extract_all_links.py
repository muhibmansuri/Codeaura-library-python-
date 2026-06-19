# ==========================================
# Codeaura Python Course: 03_extract_all_links.py
# ==========================================
# Concept: Finding multiple elements (tags)
# Real Life Example: Kisi website par kitne aur kaun-kaun se click karne wale Links (URLs) hain, unhe ek second me dhoondh nikalna.

import requests
from bs4 import BeautifulSoup

print("--- Website Link Extractor ---")

url = "https://www.python.org/"
print(f"Searching for links on {url} ...\n")

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Step 1: Saare <a> tags (links) dhoondhna
    # HTML me link <a> tag se banta hai aur uske andar 'href' me link ka pata (URL) hota hai
    links = soup.find_all('a')
    
    print(f"Wow! I found {len(links)} links on this website.\n")
    print("Here are the first 5 links:")
    
    # Step 2: Shuru ke 5 links ko print karna
    for i in range(5):
        # 'href' attribute se actual link bahar nikalna
        link_url = links[i].get('href')
        link_text = links[i].text.strip() # Text ko saaf karna
        
        print(f"{i+1}. Text: '{link_text}' ---> URL: {link_url}")
        
else:
    print("Could not connect to the website.")

# Note for Students: Ye technique 'Search Engines' (jaise Google) use karte hain poore internet ko scan karne ke liye!
