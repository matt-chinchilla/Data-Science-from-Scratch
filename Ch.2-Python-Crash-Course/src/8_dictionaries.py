#8a) "Dictionary" ==> Fundamental data structure // basically a table in SQL
empty_dict = {}                                             # Pythonic
empty_dict2 = dict()                                        # less Pythonic
grades = {"Matthew": 80, "Dani": 95}                        # dictionary literal


#8b) How to look up a value in a dictionary
        # --> You do it with square brackets
dani_grade = grades["Dani"]                                 # == 95


#8c) "KeyError" => error that comes from looking up a key && it died :((
try:
    frank_grade = grades["Frank"]
except KeyError:
    print("no grades for Frank! Supid dumb idiot!")


#8d) checking for the existence of a key using the "in" keyword
matt_has_grade = "Matthew" in grades                        # == True
frank_has_grade = "Frank" in grades                         # == False
        # This is fast even for weewy weewy big dictionaries X3


#8e) Dictionaries have a "get" method --> returns default value // not an error
matts_grade = grades.get("Matthew", 0)                      # == 80 (default value)
franks_grade = grades.get("frank", 0)                       # == 0 (default value)
no_ones_grade = grades.get("No One")                        # default is None  


#8f) Assigning key-value pairs using the same square brackets
grades["Dani"] = 100                                       # replaces the old value
grades["Frank"] = 90                                       # adds a third entry
num_students = len(grades)                                 # == 3


#8g) Using dictionaries to represent structured data
tweet = {
    "user": "joelgrus",
    "text": "Data Science is Awesome",
    "retweet_count": 100,
    "hashtags": ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}


#8h) Looking up all of the keys of a dictionary instead of specific ones
tweet_keys = tweet.keys()                                  # iterable for the keys
tweet_values = tweet.values()                              # iterable for the values
tweet_items = tweet.items()                                # iterable for the (key, value) tuples

"user" in tweet_keys                                       # == True, but not pythonic
"user" in tweet                                            # Pythonic way of checking for keys
"joelgrus" in tweet_values                                 # == True (slow but the only way to check)