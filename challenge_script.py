# Import necessary libraries
import numpy as np
from pathlib import Path

# Set input path
INPUT_DIR=Path('input_data')

# Read in the DNA sequences input txt file
with open(INPUT_DIR/'sequences.txt', 'r') as f:
    sequences = f.read().splitlines()

#>>>>>>
# Read in the labels input txt file like above
true_labels = [] 
#<<<<<<


# "The client has provided an algorithm to be adapted to get the results we need" 
# Define a function to predict the label for a given DNA sequence
def predict_label(sequence):
#>>>>>>
    if 'ATG' in sequence and 'TAA' in sequence:
        start_index = sequence.index('ATG')
        end_index = sequence.index('TAA')
        if end_index - start_index <= 22:
            return 'positive'
    return 'negative'
#<<<<<<


# Predict the labels for each DNA sequence using the predict_label function
#<<<<<<
predicted_labels = [l for l in sequences]
#>>>>>>

# Create a confusion matrix to summarize the performance of the predictions
#>>>>>>
# Set up empty confusion_matrix matrix
confusion_matrix = np.zeros((2, 2)) 
# Count the outcomes and update the matrix
for T, P in zip(true_labels, predicted_labels):
    pass
#<<<<<<

# From the definitions 
TP_count = confusion_matrix[0, 0]
FP_count = confusion_matrix[0, 1]
TN_count = confusion_matrix[1, 1]
FN_count = confusion_matrix[1, 0]


# Calculate accuracy, precision, and recall
#>>>>>
accuracy = () / ()
precision = () / ()
recall = () / ()
#<<<<<







