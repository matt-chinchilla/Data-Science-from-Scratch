#4a) "Scatterplots" are the best choice for visualizing the relationship between 2 paired sets of data
        ## Ex: showing the relationship betwwen # of friends my users have
        ## vs. the # of minutes they spend on the site every day

from matplotlib import pyplot as plt
from typing import List

friends: List[int] = [70, 65, 72, 63, 71, 64, 60, 64, 67]
minutes: List[int] = [175, 170, 205, 120, 220, 130, 105, 145, 190]
labels: List[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

plt.scatter(friends, minutes)

# label each point
for label, friend_count, minute_count in zip(labels, friends, minutes):  # zip together the labels, friends, and minutes
    plt.annotate(label,                                      # this is the label for the point
                 xy=(friend_count, minute_count),            # put the label with its point
                 xytext=(5, -5),                             # but slightly offset
                 textcoords='offset points')
    
plt.title("Daily Minutes vs. Number of Friends")
plt.xlabel('# of friends')
plt.ylabel('daily number of minutes interacting w/ site')
plt.show()
