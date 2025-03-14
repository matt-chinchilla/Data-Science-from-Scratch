#2a) "Bar Charts" are good for when you want to show how some quantity 
#       varies among some discrete set of items

        # Ex: How many academy awards were won by a variety of movies
from matplotlib import pyplot as plt


movies = ["Annie Hall", "Ben-Hur", "Casablanca", "Gandhi", "West Side Story"]
num_oscars = [5, 11, 3, 8, 10]

# Plot bars with the left x-coordinates [0, 1, 2, 3, 4], heights [num_oscars]
plt.bar(range(len(movies)), num_oscars)

plt.title("My Favorite Movies")          # Give the chart a title
plt.ylabel("# of Academy Awards")       # Label the y-axis

#label x-axs with movie names at the center of the bars
plt.xticks(range(len(movies)), movies)

plt.show()


#-------------------------------------------------------------------------------------
#2b) Visually exploring how values are distributed with bar charts
from collections import Counter
grades = [83, 95, 91, 87, 70, 0, 85, 82, 100, 67, 73, 77, 0]

# Bucket grades by decile, but put 100 in with the 90s
histogram = Counter(min(grade // 10 * 10, 90) for grade in grades)

plt.bar([x + 5 for x in histogram.keys()],  # shift bars right by 5
        histogram.values(),                 # give each bar its correct height
        10,                                 # give each bar a width of 10
        edgecolor=(0, 0, 0))                # black edges for each bar

plt.axis([-5, 105, 0, 5])                   # x-axis from -5 to 105 (adds a little space on either side),
                                            # y-axis from 0 to 5

plt.xticks([10 * i for i in range(11)])     # x-axis labels at 0, 10, ..., 100
plt.xlabel("Decile")
plt.ylabel("# of Students")
plt.title("Distribution of Exam 1 Grades")
plt.show()


#-------------------------------------------------------------------------------------
#2c) Misleading bar charts occur when your y-axis in ply.axis does not start at 0

mentions = [500, 505]
years = [2017, 2018]

plt.bar(years, mentions, 0.8)               # years = x coordinates of the bars, mentions is the height, .08 is the width
plt.xticks(years)                           # label the x-axis with the value of each year
plt.ylabel("# of times I heard someone say 'data science'")

# if you don't do this, matplotlib will label the x-axis 0, 1
# and then add a +2.013e3 off in the corner (bad matplotlib!)
plt.ticklabel_format(useOffset=False)       # causes whole numbers, not scientific notation

# misleading y-axis only shows the part above 500

plt.axis([2016.5, 2018.5, 499, 506])        # x-axis from 2016.5 to 2018.5, y-axis from 499 to 506
plt.title("Look at the 'Huge' Increase!")
plt.show()