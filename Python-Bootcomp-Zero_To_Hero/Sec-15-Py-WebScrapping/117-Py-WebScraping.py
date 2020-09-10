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

print("\nuse bs4 to beautify output")
print("- - - - - - - - - - ")
# Goal is to use make the scrap useful (in pycharm it looks fine) but
# if not in Pycharm is a glob
soup = bs4.BeautifulSoup(res.text, "lxml")

print(soup)

print("\nsoup.select('title')")
print("- - - - - - - - - - ")
print(soup.select('title'))

title_tag = soup.select('title')

print("\ntitle_tag[0]")
print("- - - - - - - - - - ")
print(title_tag[0])


# First get the request
res = requests.get('https://en.wikipedia.org/wiki/Grace_Hopper')

print(res)

# Create a soup from request
soup = bs4.BeautifulSoup(res.text, "lxml")

#print(soup)


# note depending on your IP Address,
# this class may be called something different
print("\nsoup.select(\".toctext\"")
print("- - - - - - - - - - ")
print(soup.select(".toctext"))

print("\nprint(item.text)")
print("- - - - - - - - - - ")
for item in soup.select(".toctext"):
    print(item.text)


res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")
soup = bs4.BeautifulSoup(res.text, 'lxml')
image_info = soup.select('.thumbimage')

# Grabs two Images
print("\nimage_info")
print("- - - - - - - - - - ")
print(image_info)

print("\nHow many Images")
print("- - - - - - - - - - ")
print(len(image_info))

computer = image_info[0]

print("\nImage Type")
print("- - - - - - - - - - ")
print(type(computer))

print("\nimage url path")
print("- - - - - - - - - - ")
print(computer['src'])

image2 = image_info[1]

print("\nimage 2 url path")
print("- - - - - - - - - - ")
print(image2['src'])


image_link = requests.get("https:{}".format(computer['src']))

print("\nDumps RAW image binary")
print("- - - - - - - - - - ")
print(image_link.content)

print("\nTaking RAW Binary to copy the image")
print("- - - - - - - - - - ")
f = open('my_new_file_name.jpg', 'wb')
f.write(image_link.content)
f.close()

print("\nSCrappping http://books.toscrape.com/catalogue/page-{}.html")
print("- - - - - - - - - - ")
base_url = 'http://books.toscrape.com/catalogue/page-{}.html'


res = requests.get(base_url.format('1'))


soup = bs4.BeautifulSoup(res.text, "lxml")

print(soup.select(".product_pod"))
