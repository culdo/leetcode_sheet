import csv
import requests

new_l = []
with open("leetcode_sln_urls.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        new_l.append(row[0])

new_l = list(reversed(new_l))
with open("all_content.cpp", "wb") as f:
    for url in new_l[:100]:
        url = url.replace("/blob", "")
        raw_url = "https://raw.githubusercontent.com"+url
        print(raw_url)
        resp = requests.get(raw_url)
        f.write(resp.content+b"\n-----------------------------------------------------------------------------------------------\n\n")

