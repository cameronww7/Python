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

print("\n\nWeb Scrape")
print("- - - - - - - - - - ")
print(webScrape)
print(webScrape.text)


soupwebScrape = bs4.BeautifulSoup(webScrape.text, "lxml")

print("\n\nAuthors")
print("- - - - - - - - - - ")
print(soupwebScrape.select('author'))

print(soupwebScrape.select("author"))
products = soupwebScrape.select("author")

soupwebScrape = bs4.BeautifulSoup(webScrape.text, 'lxml')

print(soupwebScrape.select(".author"))

print("\n\nAuthors with HTML")
print("- - - - - - - - - - ")
for index in soupwebScrape.select(".author"):
    print(index)


print("\n\nAuthors without HTML")
print("- - - - - - - - - - ")
authors = set()
for name in soupwebScrape.select(".author"):
    authors.add(name.text)

for index in authors:
    print(index)


print(soupwebScrape.select(".quote"))

print("\n\nQuotes with HTML")
print("- - - - - - - - - - ")
for index in soupwebScrape.select(".quote"):
    print(index)


print("\n\nQuotes")
print("- - - - - - - - - - ")
quotes = set()
for name in soupwebScrape.select(".text"):
    quotes.add(name.text)


for index in quotes:
    print(index)

print("\n\nquotes.pop()")
print("- - - - - - - - - - ")
print(quotes)


print("\n\noneLiners with HTML")
print("- - - - - - - - - - ")

oneLiners = set()
for name in soupwebScrape.select(".tag-item"):
    oneLiners.add(name.text)


for index in oneLiners:
    print(index)
