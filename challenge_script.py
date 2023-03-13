# Import necessary libraries
import numpy as np
from pathlib import Path

# Set input path
INPUT_DIR=Path('input_data')

# Read in the DNA sequences input txt file
try: 
    with open(INPUT_DIR/'sequences.txt', 'r') as f:
        sequences = f.read().splitlines()
except IOError:
    print("Error: file 'sequences.txt' in folder './input_data' does not exist'")
    quit()

#>>>>>>
# Read in the labels input txt file like above
try:
    with open(INPUT_DIR/'true_labels.txt', 'r') as f:
        true_labels = f.read().splitlines() 
except IOError:
    print("Error: file 'true_labels.txt' in folder './input_data' does not exist'")
    quit()

#<<<<<<

# Validate input data
# 1. Length of both lists should be equal
if len(sequences)!=len(true_labels):
    print("Error: number of sequences ({0}) should be equal to number of true_labels ({1})".format(len(sequences),len(true_labels)))
    quit()
# 2. Sequences contain only A, T, G and Cs.
allowed_nucleotides = set('ATGC')
for seq in sequences:
    u = set(seq)
    if u <= allowed_nucleotides:
        pass
    else:
       print("Error: sequences contain unknown nucleotide")
       quit()
# 3. Check that only `positive` and `negative` values are in true_labels.txt
if (set(['positive', 'negative'])!=set(true_labels)) :
    print("Error: true_labels contain improper values, only 'positive' and 'negative' are allowed")
    quit()

# "The client has provided an algorithm to be adapted to get the results we need" 
# Define a function to predict the label for a given DNA sequence
def predict_label(sequence):
#>>>>>>
    if len(sequence)>20 and 'ATG' in sequence:
        return 'positive'
    return 'negative'
#<<<<<<


# Predict the labels for each DNA sequence using the predict_label function
#<<<<<<
predicted_labels = [predict_label(l) for l in sequences]
#>>>>>>

# Create a confusion matrix to summarize the performance of the predictions
#>>>>>>
# Set up empty confusion_matrix matrix
confusion_matrix = np.zeros((2, 2)) 
# Count the outcomes and update the matrix
for T, P in zip(true_labels, predicted_labels):
    if T == 'positive':
        if P == 'positive':
            confusion_matrix[0, 0] += 1 # add a count to the TP cell
        else:
            confusion_matrix[0, 1] += 1 # add a count to the FP cell
    else:
        if P == 'positive':
            confusion_matrix[1, 0] += 1 # add a count to the FN cell
        else:
            confusion_matrix[1, 1] += 1 # add a count to the TN cell

#<<<<<<

# From the definitions 
TP_count = confusion_matrix[0, 0]
FP_count = confusion_matrix[0, 1]
TN_count = confusion_matrix[1, 1]
FN_count = confusion_matrix[1, 0]


# Calculate accuracy, precision, and recall
#>>>>>
accuracy = (TP_count + TN_count) / (TP_count + FP_count + TN_count + FN_count)
precision = TP_count / (TP_count + FP_count)
recall = TP_count / (TP_count + FN_count)
#<<<<<

print("Analysed {0} sequences".format(len(sequences)))
print("Accuracy:\t{0:.1%}\nPrecision:\t{1:.1%}\nRecall:\t\t{2:.1%}"
      .format(accuracy, precision,recall))







