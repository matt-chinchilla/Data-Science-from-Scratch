#1a) Using "counter" and plt.bar to create a histogram of friends
from matplotlib import pyplot as plt
from collections import Counter

num_friends = [100.0,49,41,40,25,21,21,19,19,18,18,16,15,15,15,15,14,14,13,13,13,13,12,12,11,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,9,8,8,8,8,8,8,8,8,8,8,8,8,8,7,7,7,7,7,7,7,7,7,7,7,7,7,7,7,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,6,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

friend_counts = Counter(num_friends)
xs = range(101)                         # highest value is 100
ys = [friend_counts[x] for x in xs]     # ys is a list of counts
plt.bar(xs, ys)                         # histogram with xs as x-axis and ys as y-axis
plt.axis([0, 101, 0, 25])
plt.title("Histogram of Friend Counts")
plt.xlabel('# of friends')
plt.ylabel('# of people')
plt.show()


#1b) Smart statistics to generate aside from a histogram
            ## Easiest statistic --> number of data points
num_points = len(num_friends)           # 204

            ## Next easiest, the max and the min
largest_value = max(num_friends)        # 100
smallest_value = min(num_friends)       # 1

            ## Nex most useful, finding out the values in sepcific positions
sorted_values = sorted(num_friends)
smallest_value = sorted_values[0]
second_smallest_value = sorted_values[1]
second_largest_value = sorted_values[-2]