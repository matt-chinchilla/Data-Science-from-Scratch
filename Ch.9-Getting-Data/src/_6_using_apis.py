#1) Often, HTML needs to be "serialized" (convert to string) --> Uses JSON often

#Ex of JSON text:
{ "title" : "Data Science Book",
  "author" : "Joel Grus",
  "publicationYear" : 2019,
  "topics" : [ "data", "science", "data science"] }


#--------------------------------------------------------------------------------------------------
#2) Parse JSON using the "json" module
import json
serialized = """{ "title" : "Data Science Book",
                  "author" : "Joel Grus",
                  "publicationYear" : 2019,
                  "topics" : [ "data", "science", "data science"] }"""

# Parse the JSON to create a Pyhton dict
deserialized = json.loads(serialized)
assert deserialized["publicationYear"] == 2019
assert "data science" in deserialized["topics"]


#--------------------------------------------------------------------------------------------------
#3) Using an unauthenticated API
import requests, json

github_user = "matt-chinchilla"
endpoint = f"https://api.github.com/users/{github_user}/repos"

repos = json.loads(requests.get(endpoint).text)
        # repos == list of pythong "dicts" of public repos on my account


    # ex: figuring out what days of the week I am most likely to create a repo
from collections import Counter
from dateutil.parser import parse

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

# Looking for the language of the last 5 repos
last_5_repositories = sorted(repos,
                                key=lambda r: r["pushed_at"],
                                reverse=True)[:5]

last_5_languages = [repo["language"]
                    for repo in last_5_repositories]


#--------------------------------------------------------------------------------------------------
#4) using the Twython library to work with Twitter API
import os
CONSUMER_KEY = "I am a key"
CONSUMER_SECRET = "I am a secret code"

import webbrowser
from twython import Twython

# Get a temp client to retrieve an authentication URL
temp_client = Twython(CONSUMER_KEY, CONSUMER_SECRET)
temp_creds = temp_client.get_authentication_tokens()
url = temp_creds['auth_url']                            # URL to authenticate

# Now visit that URL to authorize the application to get a pin
print(f"go visit {url} and get the PIN code and paste it below")
webbrowser.open(url)                                   # open the URL in a browser
PIN_CODE = input("please enter the PIN code: ")

# Now wr can use that PIN_CODE to get the actual tokens
auth_client = Twython(CONSUMER_KEY,
                      CONSUMER_SECRET,
                      temp_creds['oauth_token'],
                      temp_creds['oauth_token_secret'])
final_step = auth_client.get_authorized_tokens(PIN_CODE)
ACCESS_TOKEN = final_step['oauth_token']
ACCESS_TOKEN_SECRET = final_step['oauth_token_secret']

# Now we get a new Twython instance using them
twitter = Twython(CONSUMER_KEY,
                   CONSUMER_SECRET,
                   ACCESS_TOKEN,
                   ACCESS_TOKEN_SECRET)


#--------------------------------------------------------------------------------------------------
#5) Using twython to perform searches now that we have an authenticated instance
        # Searching for tweets containing the phrase "data science"
for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"]
    text = status["text"]
    print(f"{user}: {text}\n")