"""
YOUR DOCUMENTATIONS """
# Import directives.
import pandas as pd
from difflib import SequenceMatcher

# Constants:
SEQUENCE_DATA_PATH = "data/sequence_data.csv"
SEQUENCE_ANALYSIS_PATH = "sequence_analysis.csv"
# Your answers:

#------------- Objective 1 -------------#

# Read csv
seq_data = pd.read_csv(SEQUENCE_DATA_PATH, names=["Name", "Sequence"])

# Parse sequence_data and construct a dictionary
sequences_dict = seq_data.set_index('Name')['Sequence'].to_dict()
# print(sequences_dict['pevfvoes'])
# print(type(sequences_dict))


#------------- Objective 2 -------------#

original = 'GRMMMKYRDQRAGKISERLVITSEMIENIQSVKAYCWEEAMEKMIENLRQTELKLTRKAA'

# Instantiation of the class (for the purpose of this exercise, # it is essential that the first value of this class is "None".)
matcher = SequenceMatcher(None)


# Setting the sequence "to" which we want other sequences to # be compared to (original):
matcher.set_seq1(original)

comparison_dict = dict()

# Iterate through sequences_dict
for name in sequences_dict:
    # Get the sequence of the target and pass to matcher for comparison
    seq = sequences_dict[name]
    matcher.set_seq2(seq)

    # Obtain ratio between original and sequence
    ratio = matcher.ratio()
    # Add to comparison_dict with the key as name and value as ratio
    comparison_dict[name] = ratio

#------------- Objective 3 -------------#
# Find and print the unique ratios from the values of comparison_dict
unique_ratios = set(comparison_dict.values())
print('Unique ratios: ', len(unique_ratios))

#------------- Objective 4 -------------#
frequencies = dict()
# Ascendingly sorted
sorted = sorted(unique_ratios)
# Count frequency of unique ratios in comparison_dict and save them to frequencies dict key: unique ratio, value: count
for uratio in sorted:
    count = sum(ratio == uratio for ratio in comparison_dict.values())
    frequencies[uratio] = count

# https://stackoverflow.com/a/48371928

#------------- Objective 5 -------------#
# Find max and min ratios
max_ratio = max(comparison_dict.values())
min_ratio = min(comparison_dict.values())

print('Maximum similarity ratio: ', max_ratio)
print('Minimum similarity ratio: ', min_ratio)

#------------- Objective 6 -------------#
# Find max and min frequencies
max_ratio_frequency = frequencies[max_ratio]
min_ratio_frequency = frequencies[min_ratio]

print('Maximum similarity frequency: ', max_ratio_frequency)
print('Minimum similarity frequency: ', min_ratio_frequency)

#------------- Objective 7 -------------#
# Find max and min frequencies percentages
max_ratio_percentage = max_ratio_frequency/len(sequences_dict)*100
min_ratio_percentage = min_ratio_frequency/len(sequences_dict)*100

print('Percentage of maximum similarity: ', f'{max_ratio_percentage:.2f}')
print('Percentage of minimum similarity: ', f'{min_ratio_percentage:.2f}')

#------------- Objective 8 -------------#
max_ratio_sequence_names = []

for name in comparison_dict:
    if comparison_dict[name] == max_ratio:
        max_ratio_sequence_names.append(name)

print('Name of sequences with the highest similarity: ', ", ".join(max_ratio_sequence_names))

# https://www.kite.com/python/answers/how-to-make-a-list-into-a-comma-separated-string-in-python

#------------- Objective 9 -------------#
# Create new file with this format: sequence_name,sequence,ratio,ratio_freq,ratio_freq_percentage
with open(SEQUENCE_ANALYSIS_PATH, mode='w') as output_file:
    for name, seq in sequences_dict.items():
        ratio          = comparison_dict[name]
        ratio_freq     = frequencies[ratio]
        ratio_freq_pct = ratio_freq/len(sequences_dict)*100

        # Writing line into the file:
        print(name, seq, '{:.3f}'.format(ratio), '{:.3g}'.format(ratio_freq), '{:.2f}%'.format(ratio_freq_pct),  sep=',', file=output_file)

    print('\n>>> Results of the analysis have been saved.')
    output_file.close()
