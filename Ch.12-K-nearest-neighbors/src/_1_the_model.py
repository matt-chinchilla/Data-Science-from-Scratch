#1) "Nearest Neighbors Classification" -> looking at the neighbors who are closest to a given point
                                        # granted a large number of dimensions (features)

        # Neglects a lot of information consciously
            ## ^ b/c of this, may not tell you the "why" behind an outcome


#-------------------------------------------------------------------------------------------------
#2) The labels we will use (Vectors b/c we can use the "distance" function)
        # 1) Pick a number "k" like 3 | 5
        # 2) Classify some new data point
        # 3) Find the "k" nearest labeled points
        # 4) Let them vote on the new output

# Making a fxn that counts votes
from typing import List
from collections import Counter

def raw_majority_vote(labels: List[str]) -> str:
    votes = Counter[labels]
    winner, _ = votes.most_common(1)[0] # most_common returns a list of tuples
    return winner

assert raw_majority_vote(['a', 'b', 'c', 'b']) == 'b'

        # The issue // what do we do if there is a tie (ex: ['a', 'a', 'b', 'c', 'b'])?
        # The options:
            ## Pick one of the winners at random
            ## Weigh the votes by distance & pick the weighted winner
            ## reduce "k" until we find a unique winner


#-------------------------------------------------------------------------------------------------
#3) Choosing "option 3, reduce 'k'"
def majority_vote(labels: List[str]) -> str:
    """Assume that labels are ordered from nearest to farthest"""
    vote_counts = Counter(labels)
    winner, winner_count = vote_counts.most_common(1)[0]
    num_winners = len([count
                       for count in vote_counts.values()
                       if count == winner_count]) # count how many times the winner appears
    if num_winners == 1:
        return winner                      # Unique winner so return it
    else:
        return majority_vote(labels[:-1])  # try again without the farthest
    

#-----------------------------------------------------------------------------------------
#4) Creating a classifier with this function
from typing import NamedTuple
        # Import the linear algebra stuff
import sys
from pathlib import Path

# Assuming the project root is two levels up from this file:
project_root = Path(__file__).resolve().parents[2]
linear_algebra_src = project_root / "Ch.4-Linear-Algebra" / "src"
sys.path.append(str(linear_algebra_src))

from linear_algebra import Vector, distance

class LabeledPoint(NamedTuple):  
    # A point with a label made of a vector and a label
    point: Vector
    label: str

def knn_classify(k: int,
                 labeled_points: List[LabeledPoint],
                 new_point: Vector) -> str:
    
    # Order the points from nearest to farthest
    by_distance = sorted(labeled_points,
                         key=lambda lp: distance(lp.point, new_point)) 
    
     # Find the labels for the k closest
    k_nearest_labels = [lp.label for lp in by_distance[:k]]

    # and let them vote.
    return majority_vote(k_nearest_labels)