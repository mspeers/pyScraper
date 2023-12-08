# Taken form https://realpython.com/beautiful-soup-web-scraper-python/

import requests
import sys
import sqlite3

if __name__ == "__main__":
    print(f"Arguments count: {len(sys.argv)}")
    for i, arg in enumerate(sys.argv):
        print(f"Argument {i:>6}: {arg}")


# take input for URL that you like to scrape

URL = "https://realpython.github.io/fake-jobs/"

## cerate Database
con = sqlite3.connect("tutorial.db")
cur.execute("CREATE TABLE websites(title, url, rawdata)")


# Get page
page = requests.get(URL)


# Store / print page
print(page.text)
cur.execute("INSERT INTO websites VALUES ('Fistpage',\"$URL\", \"$page.txt\")")
con.commit()


# proccess 



