#1) "Iris Dataset" -> A staple of ML | a bunch of measurements for 150 Irises x 3 species
        # Each flower has its own:
            ## 1) Petal length
            ## 2) Petal width
            ## 3) Sepal length
            ## 4) Sepal width
            ## 5) Species (setosa, versicolor, virginica)

import requests

data = requests.get(
    "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
)

with open('iris.dat', 'w') as f:
    f.write(data.text) # Save the data to a file

# Comes in a csv format with fields:
    # sepal_length, sepal_width, petal_length, petal_width, class

# Ex:
    #5.1,3.5,1.4,0.2,Iris-setosa


#-------------------------------------------------------------------------------------------------
#2) Trying to build a class that can predict the class (species) of the flower from first 4 measurements

from typing import Dict, List
import csv
from collections import defaultdict
from _1_the_model import LabeledPoint
    
def parse_iris_row(row: List[str]) -> LabeledPoint:
    """
    sepal_length, sepal_width, petal_length, petal_width, class
    """
    measurements = [float(value) for value in row[:-1]] # all but the last value
    # class is e.g. "Iris-virginica"; we just want "virginica"
    label = row[-1].split("-")[1]

    return LabeledPoint(measurements, label)

with open('iris.data') as f:
    reader = csv.reader(f)
    iris_data = [parse_iris_row(row) for row in reader]

# Also group just the points by species / label so we can plot them
from linear_algebra import Vector
points_by_species: Dict[str, List[Vector]] = defaultdict(list)
for labeled_point in iris_data:
    points_by_species[labeled_point.label].append(iris.point)