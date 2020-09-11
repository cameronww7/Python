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

res = requests.get("http://quotes.toscrape.com/")

print(res)
print(res.text)
