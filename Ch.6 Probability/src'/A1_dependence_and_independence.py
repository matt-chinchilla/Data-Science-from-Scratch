#1a) "Probability" -> A way of quantifying the uncertainty associated with events chosen
#                     from a some universe of events

        ## Notation: P(E) == "probablity of Event E"

        ## Events F & E are independent if the probability that theyh BOTH happen
        ## is equal to the even that EACH happens (ex: heads, heads == tails, heads)
        ## P(E, F) == P(E)*P(F)


#-----------------------------------------------------------------------------------
#1b) "Conditional Probability" -> The probability of some event, given that some other
#                                event has happened

        ## P(E,F) = P(E|F)P(F)
                ### ^ Probability of E given that we know F happens
                ### Ex: given tails, what is the probability of heads?

# Next, lets look at the common probability example of boy/girl births
        # P(B) = "Both children are girls"
        # P(G) = "Older Child is a girl"

import enum, random

# An enum is a typed set of enumerated values. We can use them
# to make our code more descriptive and readable.

class Kid(enum.Enum):
    BOY = 0
    GIRL = 1

def random_kid() -> Kid:
    return random.choice([Kid.BOY, Kid.GIRL])

both_girls:     int = 0
older_girl:     int = 0
either_girl:    int = 0

random.seed(0)

for _ in range(10000):
    younger: Kid = random_kid()
    older: Kid = random_kid()

    if older == Kid.GIRL:
        older_girl += 1
    if older == Kid.GIRL and younger == Kid.GIRL:

        both_girls += 1
    if older == Kid.GIRL or younger == Kid.GIRL:
        either_girl += 1

# print(both_girls)
# print(older_girl)
# print(either_girl)
print("P(both | older):", both_girls / older_girl)      # 0.514 ~ 1/2
print("P(both | either):", both_girls / either_girl)    # 0.342 ~ 1/3   