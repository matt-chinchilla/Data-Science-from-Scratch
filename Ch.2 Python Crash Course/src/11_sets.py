#11a) "Sets" <==> a collection of unqiue elements || Represented by {}
primes_below_20 = {2, 3, 5, 7}
        # Does NOT work for empty sets
            # {} already means "empty dict"
        # Need to use set() itself

s = set()
s.add(1)        # s == {1}
s.add(2)        # s == {1, 2}
s.add(2)        # s is still == {1, 2}
x = len(s)      # == 2
y = 2 in s      # == True
z = 3 in s      # == False


#11b) WHY WE USE SETS ======> 2 main reasons
        # Reason 1: "in" is a very fast operation on sets
stopwords_list = ["a", "an", "at"] + hundreds_of_other_words + ["yet", "you"]

"zip" in stopwords_list         # False, but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set          # Very fast to check

        # Reason 2: Finding distinct items in a collection