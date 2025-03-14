# 1) Why we don't typically use "accuracy" to measure how good a (binary classification) model is

        # Ex: Building a model to make a "binary judgment" -> 'is this email spam?'
        # Given: 
                ## A set of labeled data & such a predictive model, all data points fall into one
                ## of four categories:

        # 1) True Positive
                 # 'This message is spam, we correctly predicted it is spam'

        # 2) False Positive (type 1 error)
                 # 'This message is not spam, but we predicted it is spam'

        # 3) False Negative (Type 2 error)
                 # 'This message is spam, but we predicted it is not spam'

        # 4) True Negative
                 # 'This message is not spam, we correctly predicted it is not spam'


#--------------------------------------------------------------------------------------------------
#2) Why accuracy is not a good measure of model performance:
    # "Accuracy" -> The fraction of correct predictions
    # Accuracy = (TP + TN) / (TP + TN + FP + FN)
        ## Where TP = True Positives, TN = True Negatives, FP = False Positives, FN = False Negatives

def accuracy(tp: int, tn: int, fp: int, fn: int) -> float:
    correct = tp + tn
    total = tp + tn + fp + fn
    return correct / total

assert accuracy(70, 4930, 13931, 981070) == 0.98114


#--------------------------------------------------------------------------------------------------
#3) why we need to use "precision" and "recall" to measure model performance
        # "Precision" -> The fraction of positive predictions that are correct

        # 'Recall' -> What fraction of positives our model identified

def precision(tp: int, fp: int, tn: int, fn: int) -> float:
    return tp / (tp + fp)
assert precision(70, 4930, 13930, 981070) == 0.014 # 1.4%

def recall(tp: int, fp: int, tn: int, fn: int) -> float:
    return tp / (tp + fn)
assert recall(70, 4930, 13930, 981070) == 0.005 # 0.5% of the time, our model predicts "luke w/ leukemia"


#--------------------------------------------------------------------------------------------------
#4) Using an "F1 score" to combine recall and precision
def f1_score(tp: int, fp: int, fn: int, tn: int) -> float:
    p = precision(tp, fp, fn, tn)
    r = recall(tp, fp, fn, tn)
    
    return 2 * p * r / (p + r)