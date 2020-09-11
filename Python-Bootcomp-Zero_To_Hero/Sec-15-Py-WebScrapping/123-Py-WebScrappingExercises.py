from __future__ import print_function
import requests
import lxml
import bs4

"""
 123-Py-WebScrappingExercises
"""

print("123-Py-WebScrappingExercises")

"""

"""
print("\n123-Py-WebScrappingExercises")
print("- - - - - - - - - - ")


# TASK: Use requests library and BeautifulSoup to connect to
# http://quotes.toscrape.com/ and get the HMTL text from the homepage.

webScrape = requests.get("http://quotes.toscrape.com/")

print(webScrape)
print(webScrape.text)


soupwebScrape = bs4.BeautifulSoup(webScrape.text, "lxml")

print("\nAuthors")
print("- - - - - - - - - - ")
print(soupwebScrape.select('author'))

print(soupwebScrape.select("author"))
products = soupwebScrape.select("author")

soupwebScrape = bs4.BeautifulSoup(webScrape.text, 'lxml')

print(soupwebScrape.select(".author"))

for index in soupwebScrape.select(".author"):
    print(index)

