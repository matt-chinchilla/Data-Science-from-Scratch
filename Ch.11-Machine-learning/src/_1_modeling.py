#1) "What is a model?"
        # Model -> a specificaiton of a mathematical (or probabalistic) relationship
        #          that exists between different variables


#2) Define the term "machine learning"
        # ML -> Creating and using models that are "learned from data"


#3) The Types of Models
        # "supervised" -> there is a set of labeled data for the model to learn from
        # "unsupervised" -> there is no labeled data, the model must find structure IN the data
        # "semi-supervised" -> there is a small set of labeled data, and a large set of unlabeled data
        # "online" -> the model needs to continuously adjust to newly arriving data

        # "reinforcement" -> After making a series of predictions, the model receives a reward
        #                    or penalty based on the accuracy of its predictions


#4) The pitfalls I will fall into:
    # "overfitting" -> performs well on the data I train it on, but poorly on new data
        ## Could involve learning "noise" in the training data
        ## or learning to identify specific inputs instead of whatever factors are actually predictive

    # "underfitting" -> performs poorly even on the training data
        ## Should probably cause you to look for a new model


#5) How to avoid over-complexity in order to prevent our models from being too niche:
        # Simplest way -> Split the dataset 
            ## ex: train on first 2/3, test on last 1/3

import random
from typing import TypeVar, List, Tuple
X = TypeVar('X')  # generic type to represent a data point

def split_data(data: List[X], prob: float) -> Tuple[List[X], List[X]]:
    """Split data into fractions [prob, 1 - prob]"""
    data = data[:]                      # Make a shallow copy
    random.shuffle(data)                # because shuffle modifies the list
    cut = int(len(data) * prob)         # Use prob to find a cutoff
    return data[:cut], data[cut:]       # and split the shuffled data there

data = [n for n in range(1000)]
train, test = split_data(data, 0.75)

# The Proportions should be correct
assert len(train) == 750
assert len(test) == 250

# Preserve the OG data (in some order)
assert sorted(train + test) == data


#---------------------------------------------------------------------------------------------------
#6) Putting corresponding values together in either the training data, or the test data
Y = TypeVar('Y')

def train_test_split(xs: List[X],
                     ys: List[Y],
                     test_pct: float) -> Tuple[List[X], List[X], List[Y], List[Y]]:
    
    # Generate the indices and split them
    idxs = [i for i in range(len(xs))]
    train_idxs, test_idxs = split_data(idxs, 1 - test_pct)

    return ([xs[i] for i in train_idxs],   # x train
            [xs[i] for i in test_idxs],    # x test
            [ys[i] for i in train_idxs],   # y train
            [ys[i] for i in test_idxs])    # y test

    # Test the code
xs = [x for x in range(1000)]       # xs are 1 ... 1000
ys = [2 * x for x in xs]            # each y_i is twice x_i
x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.25)

# Check proportions
assert len(x_train) == len(y_train) == 750
assert len(x_test) == len(y_test) == 250

# Check that the corresponding data points are paired correctly
assert all(y == 2 * x for x, y in zip(x_train, y_train))
assert all(y == 2 * x for x, y in zip(x_test, y_test))

# doing something like
model = SomeKindOfModel()
x_train, x_test, y_train, y_test = train_test_split(xs, ys, 0.33)
model.train(x_train, y_train)
performance = model.test(x_test, y_test)

        # ** If it performs well on the test data, I can be more confident that it is fitting
        #    rather than "overfitting"


    # The best way to avoid pitfalls -> Split the data into 3 parts:
        # 1) "training set" for building models
        # 2) "validation set" for choosing among trained models
        # 3) "test set" for juding the final model