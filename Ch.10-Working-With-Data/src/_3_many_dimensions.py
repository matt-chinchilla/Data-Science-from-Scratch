#1) Using a matrix to do correlation between any given data point in multiple dimensions

import sys
from pathlib import Path
project_root = Path(__file__).resolve().parents[2]
linear_algebra_src = project_root / "Ch.4-Linear-Algebra" / "src"
sys.path.append(str(linear_algebra_src))

from typing import List
from A_vectors import Vector
from B_matrices import Matrix, make_matrix

statistics_src = project_root / "Ch.5-Statistics" / "src"
sys.path.append(str(statistics_src))
from D_correlation import correlation

def correlation_matrix(data: List[Vector]) -> Matrix:
    """
    Returns the len(data) matrix whose (i,j)-th entry
    is the correlation between data[i] and data[j]
    """
    def correlation_ij(i: int, j: int) -> float:
        return correlation
    
    return make_matrix(len(data), len(data), correlation_ij)


#2) For a smaller amount of dimensions, we can make a Matrix of scatter plots
        # Uses "plt.subplots"
import matplotlib.pyplot as plt

# corr_data is a list of four 100-d vectors
num_points = 100
from _2_two_dimensions import random_normal
import random

def random_row() -> List[float]:
    row = [0.0, 0, 0, 0]
    row[0] = random_normal()
    row[1] = -5 * row[0] + random_normal()
    row[2] = row[0] + row[1] + 5 * random_normal()
    row[3] = 6 if row[2] > -2 else 0
    return row

random.seed(0)

corr_rows = [random_row() for _ in range(num_points)]
corr_data = [list(col) for col in zip(*corr_rows)]

num_vectors = len(corr_data)
fig, ax = plt.subplots(num_vectors, num_vectors)

for i in range(num_vectors):
    for j in range(num_vectors):

        # Scatter column_j on the x-axis vs. column_i on the y-axis
        if i!= j: ax[i][j].scatter(corr_data[j], corr_data[i])

        #unless i == j, in which case we show the series name
        else: ax[i][j].annotate("series " + str(i), (0.5, 0.5),
                                xycoords='axes fraction',
                                ha="center", va="center")
            
        # Then hide axis labels except for the left and bottom charts
        if i < num_vectors -1: ax[i][j].xaxis.set_visible(False)
        if j > 0: ax[i][j].yaxis.set_visible(False)

# Fix the bottom right and top left axis lavels, which are wrong because
# their charts only have text in them
ax[-1][-1].set_xlim(ax[0][-1].get_xlim())
ax[0][0].set_ylim(ax[0][1].get_ylim())

plt.show()