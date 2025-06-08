from bs4 import BeautifulSoup
import requests
import pprint

url = "https://www.numbeo.com/cost-of-living/country_result.jsp?country=United+States"
result = requests.get(url).text
doc = BeautifulSoup(result, "html.parser")

table = doc.find("table", id="t2")
tbody = table.find("tbody")
rows = tbody.find_all("tr")

# Hold city names and links for each city
links = {}

for tr in rows:
    # Find the link for each city
    link = tr.find("a", class_ = "discreet_link")
    links[link.string] = link.get("href")

all_cities = []

for city_name, link in links.items():
    result = requests.get(link).text
    doc = BeautifulSoup(result, "html.parser")
    
    # Find the cost-of-living table
    table = doc.find("table", class_="data_wide_table")
    
    city_details = {}

    # Loop through rows
    for tr in table.find_all("tr"):
        tds = tr.find_all("td")
        if len(tds) >= 2:
            item = tds[0].text.strip()
            price = tds[1].text.replace("\xa0", "").strip()
            city_details[item] = price

    all_cities.append({"city": city_name, "data": city_details})

with open("cities.txt", "w", encoding="utf-8") as f:
    pprint.pprint(all_cities, stream=f)

    


