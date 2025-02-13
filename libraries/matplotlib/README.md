# Matplotlib Library Documentation

## Overview
Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python. It is widely used in the data science community for its flexibility and ease of use.

## Installation
To install Matplotlib, you can use pip. Run the following command in your terminal:

```
pip install matplotlib
```

If you are using Anaconda, you can install it with:

```
conda install matplotlib
```

## Basic Usage
Here is a simple example of how to create a basic line plot using Matplotlib:

```python
import matplotlib.pyplot as plt

# Sample data
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

# Create a line plot
plt.plot(x, y)

# Add title and labels
plt.title('Sample Line Plot')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')

# Show the plot
plt.show()
```

## Additional Resources
For more detailed documentation and advanced usage, visit the official Matplotlib website: [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)