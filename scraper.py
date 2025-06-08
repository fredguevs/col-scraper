from bs4 import BeautifulSoup
import requests

url = "https://www.numbeo.com/cost-of-living/in/New-York"

result = requests.get(url).text

doc = BeautifulSoup(result, "html.parser")

# Find the cost-of-living table
table = doc.find("table", class_="data_wide_table")

# Loop through rows
for tr in table.find_all("tr"):
    tds = tr.find_all("td")
    if len(tds) >= 2:
        item = tds[0].text.strip()
        price = tds[1].text.strip()
        print(f"{item}: {price}")
