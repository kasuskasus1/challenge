# About this script

This script is loading sequences with corresponding actual values (or true values) from 2 text files `sequences.txt` and `true_labels.txt` located in `./input_data` folder. Loaded data is then analysed with `predict_label` function (output is positive if sequence is longer than 20 nucleotides and it contains `ATG` motif at least once). 

Results are compared to `true_labels` using a 2x2 confusion matrix, then basic metrics like accuracy, precision and recall are calculated based on it and printed as an output.

## Requirements & Installation

Make sure Python 3 is installed, then install  `numpy` library:
```bash
pip3 install numpy
```

## Running the script

To run the script use the following command:
```bash
python3 challenge_scrypt.py
```

You should receive an output like:
```bash
Analysed 6 sequences
Accuracy:       50.0%
Precision:      50.0%
Recall:         66.7%
```

## Additional validations

* Input data length: number of `sequences` should be equal to number of `true_values`, if not print error and stop script execution.

* Sequences should contain only `A`, `T`, `G` and `C` letters, if not print error and stop script execution.

* `true_values` should contain only `positive` or `negative` values, if not print error and stop script execution.