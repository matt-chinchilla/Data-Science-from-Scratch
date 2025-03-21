#1) Ex: find all Congress reps who have press releases about "data"
        # --> can be found at https://www.house.gov/representatives

        # this is what an example link looks like
        #<td>
        #<a href="https://lalota.house.gov"> LaLota, Nick</a>
        #</td>

# Step 1: collecting all the URLs from the page
from bs4 import BeautifulSoup
import requests

url = "https://www.house.gov/representatives"
text = requests.get(url).text
soup = BeautifulSoup(text, "html5lib")

all_urls = [a['href']
            for a in soup('a')
            if a.has_attr('href')]

print(len(all_urls))  #Gives 967, too many


# Step 2: Filtering The URLs by the following criteria:
            # 2a) starts w/ http:// or https://
            # 2b) Has some kind of name
            # 2c) Ends w/ .house.hoc OR .house.gov/

    # USE SOME REGULAR EXPRESSIONS BABYYYYY
import re

# Must start with http:// or https://
# Must end with .house.gov or .house.gov/
regex = r"^https?://.*\.house\.gov/?$"          # s? == optional s || /? == optional slash || $ == end of string

# Writing some tests
assert re.match(regex, "http://joel.house.gov")
assert re.match(regex, "https://joel.house.gov")
assert re.match(regex, "http://joel.house.gov/")
assert re.match(regex, "https://joel.house.gov/")
assert not re.match(regex, "joel.house.gov")
assert not re.match(regex, "http://joel.house.com")
assert not re.match(regex, "https://joel.house.gov/biography")

good_urls = [url for url in all_urls if re.match(regex, url)] # good url if it matches the syntax

print(len(good_urls))       #874


#Step 3: Filtering the URLs to get rid of duplicate mentions
good_urls = list(set(good_urls))  # set() removes duplicates, list() converts it back to a list

print(len(good_urls))       # this is 437 now


#-----------------------------------------------------------------------------------------------
#2) Looking at press releases
html = requests.get('https://jayapal.house.gov').text
soup = BeautifulSoup(html, 'html5lib')

# Use a set because the link may appear multiple times
links = {a['href'] for a in soup('a') if 'press releases' in a.text.lower()}

print(links) # {'/media/press-releases'}

        # *** This is RELATIVE --> need to remember originating site ***


#------------------------------------------------------------------------------------------------
#3) Doing some scraping
from typing import Dict, Set

press_releases: Dict[str, Set[str]] = {}

for house_url in good_urls:
        html = requests.get(house_url).text
        soup = BeautifulSoup(html, 'html5lib')
        pr_links = {a['href'] for a in soup('a') if 'press releases'
                                                 in a.text.lower()}  # a = hyperlink

#print(f"{house_url}: {pr_links}")
press_releases[house_url] = pr_links      


#---------------------------------------------------------------------------------------------------------
#4) Making a more general function wether a page or Press release mentions any given term
        # (because our goal is simply to see releases mentioning "data")

#Step 1: Check for snippets w/in a <p> tag
def paragraph_mentions(text: str, keyword: str) -> bool:
        """
        Returns True if a <p> inside the text mentions {keyword}
        """
        soup = BeautifulSoup(text, 'html5lib')
        paragraphs = [p.get_text() for p in soup('p')]

        return any(keyword.lower() in paragraph.lower()
                        for paragraph in paragraphs)


#Step 2: Write a test
text = """<body><h1>Facebook</h1><p>Twitter</p>"""
assert paragraph_mentions(text, "twitter")              # is inside a <p>
assert not paragraph_mentions(text, "facebook")         # is NOT inside a <p>


#Step 3: Finding relevant congresspeople
for house_url, pr_links in press_releases.items():
        for pr_link in pr_links:
                url = f"{house_url}/{pr_link}"
                text = requests.get(url).text

                if paragraph_mentions(text, 'data'):
                        print(f"{house_url}")
                        break # done with this house_url