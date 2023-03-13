# RTG code challenge 

The objective of this challenge is to give you a chance to demonstrate your abilities to tackle a common scenario using your technical coding skills. This will involve following instructions and asking questions where appropriate. It is very common to deal with situations that need clarifying in our work, so feel free to ask questions if something is unfamiliar or unclear. This can be especially important if you don't completely understand some terminology or a requirement, a quick question can save you a lot of time.    

## Instructions
Your task will be to complete (or improve) some code and produce some output for the client. By the end we should have a running script and some values to show the client. There will be some skeleton code to get you started but make sure to read the instructions carefully and come back to them as needed.

You are to modify the code in the `challenge_script.py` file to make it work and comply to the client requirements below. We have identified the places where you will need to modify the code to make it work between these kind of symbols `>>>>>>` & `<<<<<<`. Feel free to modify outside these symbols if you want to improve the standard of the code in any way. 

A text file of some short DNA sequences that are to be used as input has been provided by the client. Also provided by the client is another text file with the results of an algorithm that the client has already used to process the DNA sequences (these are where the 'true labels' come from). We will be processing the the DNA sequences with a very simple algorithm in the script you will work on and see how close the results are.

It could be a good idea to make a branch to work on your solution. 

## Requirements 
1. Read in the DNA sequences and true labels from the input files (provided by the client) and store them in two lists. 

2. Predict the labels for each DNA sequence using a simple algorithm that classifies a sequence as 'positive' if it contains the subsequence 'ATG' and is longer than 20 nucleotide long, other wise the label should be negative. The client has provided an algorithm from some previous work that they think might be useful. This should to be adapted to get the results we need. 

3. Create a confusion matrix that shows the number of true positive, false positive, true negative, and false negative classifications. Some previous work from the client also required a confusion matrix, so we can reference that code if we wanted to or feel free to implement your own way of doing this if that more comfortable. 

4. Report the accuracy, precision, and recall of the classifier algorithm. A simple print statement or writing the results to a file would suffice for this project.

5. Include some simple documentation so the client can run the script and know what to expect. 

## Definitions 
Here are the standard definitions we will use. 

### Outcomes:
- True positive (TP): item was correctly classified as positive
- False positive (FP): item was incorrectly classified as positive
- True Negative (TN): item was correctly classified as negative
- False Negative (FN): item was incorrectly classified as negative

### Metrics
- Accuracy: `(TP + TN) / (TP + TN + FP + FN)`
- Precision: `TP / (TP + FP)`
- Recall: `TP / (TP + FN)`