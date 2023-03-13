# A simple 2-by-2 confusion matrix is organized as follows:

#                         Actual Positive     |	 Actual Negative
# -------------------------------------------------------------------
# Predicted Positive	| True Positive (TP)  |	 False Positive (FP)
# -------------------------------------------------------------------
# Predicted Negative	| False Negative (FN) |	 True Negative (TN)


# Some test data that could be used to build a confusion matrix
real = [1, 0, 0, 0, 1, 0, 1, 1, 0, 1]
predicted =[0, 1, 0, 0, 0, 1, 0, 1, 1, 0] 

# A simple confusion matrix can be constructed like this
import numpy as np

confusion_matrix = np.zeros((2, 2)) # set up a empty 2-by-2 matrix

# Count the outcome and update the confusion matrix
for real, predicted in zip(real, predicted):
    if real == 'positive':
        if predicted == 'positive':
            confusion_matrix[0, 0] += 1 # add a count to the TP cell
        else:
            confusion_matrix[0, 1] += 1 # add a count to the FP cell
    else:
        if predicted == 'positive':
            confusion_matrix[1, 0] += 1 # add a count to the FN cell
        else:
            confusion_matrix[1, 1] += 1 # add a count to the TN cell

