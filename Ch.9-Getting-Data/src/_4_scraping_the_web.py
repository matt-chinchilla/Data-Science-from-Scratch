#1) Fetching webpages is easy! Making them make sense is not
from bs4 import BeautifulSoup
import requests

# Recall that whitespace-separated strings get concatenated.
url = ("https://raw.githubusercontent.com/"
       "joelgrus/data/master/getting-data.html")

html = requests.get(url).text
soup = BeautifulSoup(html, 'html5lib')  # make a BeautifulSoup object -> Parse string 'html' -> clean w/ 'html5lib'


#--------------------------------------------------------------------------------------------------

#2) working with "tag" objects // ex: find the FIRST <p> tag (and its contents)
first_paragraph = soup.find('p')                    #or just soup.p

assert str(soup.find('p')) == '<p id="p1">This is the first paragraph.</p>'

    # *getting the contents of a "tag" using its TEXT property

first_paragraph_text = soup.p.text
first_paragraph_words = soup.p.text.split()

assert first_paragraph_words == ['This', 'is', 'the', 'first', 'paragraph.']


    # ** extracting a tag's attributes by treating it like a "dict"
first_paragraph_id = soup.p['id']                   # raises a KeyError if no 'id'
first_paragraph_id2 = soup.p.get('id')              # returns None if no 'id'

assert first_paragraph_id == first_paragraph_id2 == 'p1'


    # *** getting multiple tags at once
all_paragraphs = soup.find_all('p')                 # or just soup('p')
paragraphs_with_ids = [p for p in soup('p') if p.get('id')] 

assert len(all_paragraphs) == 2
assert len(paragraphs_with_ids) == 1


    # **** finding tags with a specific class
important_paragraphs = soup('p', {'class': 'important'})
important_paragraphs2 = soup('p', 'important')
important_paragraphs3 = [p for p in soup('p')
                         if 'important' in p.get('class', [])] 

assert important_paragraphs == important_paragraphs2 == important_paragraphs3
assert len(important_paragraphs) == 1


#--------------------------------------------------------------------------------------------------
#3) Combining methods for elaborate logic --> Ex: get every <span> element inside a <div>
        # <span> == group & style small pieces of text || Ex: <span class = "highlight">highlighted text</span>
        # <div> == block-level HTML container that groups together large pieces of content

# Warning: will return the same <span> multiple times
# if it sits inside multiple <div>s
# Be more clever if that is the case
spans_inside_divs = [span
                     for div in soup('div')         # for each <div> tag
                     for span in div('span')]       # for each <span> inside