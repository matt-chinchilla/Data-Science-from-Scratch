from typing import List
import random

def run_experiment() -> List[bool]:
    """Flips a fair coin 1000 times, True = heads, False = tails"""
    return [random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment: List[bool]) -> bool:
    """Using the 5% significance levels"""
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads > 531
                    #45th %               #55th %

random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections = len([experiment
                      for experiment in experiments
                      if reject_fairness(experiment)]) # Count how many times we reject the null hypothesis

assert num_rejections == 46

# ** "p-hacking" --> manipulating data to cherry-pick results (ex: removing outliers, running multiple tests)
