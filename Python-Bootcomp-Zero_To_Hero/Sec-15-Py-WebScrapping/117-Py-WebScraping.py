from __future__ import print_function
import requests
import lxml
import bs4

"""
 Prompt 117-Py-WebScraping
"""

print("117-Py-WebScraping")

"""

"""
print("\n117-Py-WebScraping")
print("- - - - - - - - - - ")


# Step 1: Use the requests library to grab the page
# Note, this may fail if you have a firewall blocking Python/Jupyter
# Note sometimes you need to run this twice if it fails the first time
res = requests.get("http://www.example.com")

print("\nReturns Response Error Code")
print("- - - - - - - - - - ")
# Returns Response Error Code
print(res)

print("\ntype(res)")
print("- - - - - - - - - - ")
# object is a requests.models.Response object and it actually contains
# the information from the website
print(type(res))

print("\nDisplay Scrapped Website")
print("- - - - - - - - - - ")
# Displays the website that was scrapped
print(res.text)

