"""
Model Answer
============


# Imports
# ------------------------------------------------------------------------------------------------

from difflib import SequenceMatcher


# Constants
# ------------------------------------------------------------------------------------------------

SEQUENCE_DATA_PATH = "data/sequence_data.csv"
SEQUENCE_ANALYSIS_PATH = "sequence_analysis.csv"

DELIMITER = ','

SIMILARITY_PRECISION = 3


# Global variables
# ------------------------------------------------------------------------------------------------

original = 'GRMMMKYRDQRAGKISERLVITSEMIENIQSVKAYCWEEAMEKMIENLRQTELKLTRKAA'


# Dictionary of templates for producing the results,
# defined to ensure consistency across the board:
results_templates = {
    'unique ratio': 'Unique ratios: {}',
    'similarity': '{} similarity ratio: {}',
    'frequency': '{} similarity frequency: {}',
    'percentage': 'Percentage of {} similarity: {:.2%}',
    'similar sequences': 'Name of sequences with the highest similarity: {}',
    'file ratio': '{:.3f}',
    'file percentage': '{:.2%}',
    'finished': '\n>>> Results of the analysis have been saved.'
}



# ------------------------------------------------------------------------------------------------
# Question 1
# ------------------------------------------------------------------------------------------------
# Extracting the data from the file and constructing a dictionary from them:

with open(SEQUENCE_DATA_PATH, mode='r') as sequence_file:
    sequence_data = sequence_file.read()


sequence_dict = dict()

for line in sequence_data.splitlines():
    # Processing each line by splitting it on the `delimiter`.
    name, seq = line.split(DELIMITER)

    sequence_dict[name] = seq

## checking the code:
# > sequence_dict['MK1BvB5b']
# 'ACFRQYCHMARSMTAS...'

# to check examine one of the entries


# ------------------------------------------------------------------------------------------------
# Question 2
# ------------------------------------------------------------------------------------------------
# Similarity evaluation (rounded to `SIMILARITY_PRECISION`):

comparison_dict = dict()

matcher = SequenceMatcher(None)
matcher.set_seq1(original)

for name, seq in sequence_dict.items():
    matcher.set_seq2(seq)
    ratio = matcher.ratio()

    comparison_dict[name] = round(ratio, SIMILARITY_PRECISION)

## example entry to check your results:
# > comparison_dict['MK1BvB5b']
# 0.283


# ------------------------------------------------------------------------------------------------
# Question 3
# ------------------------------------------------------------------------------------------------
# Extracting the unique ratios:

unique_ratios = set(comparison_dict.values())

unique_ratios_len = len(unique_ratios)

print(results_templates['unique ratio'].format(unique_ratios_len))

# Unique ratios: 25


# ------------------------------------------------------------------------------------------------
# Question 4
# ------------------------------------------------------------------------------------------------
# Calculating the frequency (num of repetitions) for each *unique* ratio:

# To count the members, results of `.values()` must be
# converted to a `list` or a `tuple`:
ratios_tuple = tuple(comparison_dict.values())

frequencies = dict()

for ratio in sorted(unique_ratios):
    frequencies[ratio] = ratios_tuple.count(ratio)

## example entry to check your results:
# > frequencies[0.283]
# 786


# ------------------------------------------------------------------------------------------------
# Question 5
# ------------------------------------------------------------------------------------------------

# Maximum similarity observed (with `original`):
max_ratio = max(unique_ratios)
print(results_templates['similarity'].format('Maximum', max_ratio))

# Maximum similarity ratio: 0.433


# Minimum similarity observed (with `original`):
min_ratio = min(unique_ratios)
print(results_templates['similarity'].format('Minimum', min_ratio))

# Minimum similarity ratio: 0.033


# ------------------------------------------------------------------------------------------------
# Question 6
# ------------------------------------------------------------------------------------------------

# Number of sequences most similar to `original`:
max_ratio_frequency = frequencies[max_ratio]
print(results_templates['frequency'].format('Maximum', max_ratio_frequency))

# Maximum similarity frequency: 5

# Number of sequences least similar to `original`:
min_ratio_frequency = frequencies[min_ratio]
print(results_templates['frequency'].format('Minimum', min_ratio_frequency))

# Minimum similarity frequency: 16



# -------------------------------------------------------------------------------------------------
# Question 7
# -------------------------------------------------------------------------------------------------

sequence_dict_len = len(sequence_dict)

# Maximum (percentage of sequences most similar to `original`):
max_percentage_ratio = max_ratio_frequency / sequence_dict_len
print(results_templates['percentage'].format('maximum', max_percentage_ratio))

# Percentage of maximum similarity: 0.05%

# Minimum (percentage of sequences least similar to `original`):
min_percentage_ratio = min_ratio_frequency / sequence_dict_len
print(results_templates['percentage'].format('minimum', min_percentage_ratio))

# Percentage of minimum similarity: 0.16%


# -------------------------------------------------------------------------------------------------
# Question 8
# -------------------------------------------------------------------------------------------------
# Extracting the name of the ratios that are most similar to `original`:

max_ratio_sequence_names = list()

for name, ratio in comparison_dict.items():
    if ratio == max_ratio:
        max_ratio_sequence_names.append(name)


# Joining the array of sequences with maximum similarity to
# create a continuous piece of string:
space_char = ' '
delimiter_with_space = DELIMITER + space_char

sequence_names_str = delimiter_with_space.join(max_ratio_sequence_names)


print(results_templates['similar sequences'].format(sequence_names_str))

# Name of sequences with the highest similarity: q22h9BLw, 9be4FE8c, aqVwf40n, U6PZKTtG, ZxtdUrZv


# ------------------------------------------------------------------------------------------------
# Question 9
# ------------------------------------------------------------------------------------------------
# Storing the results of our analysis into a file:

with open(SEQUENCE_ANALYSIS_PATH, mode='w') as analysis_file:
    for name, seq in sequence_dict.items():
        # Extracting comparison info:
        ratio = comparison_dict[name]
        ratio_prepped = results_templates['file ratio'].format(ratio)

        # Extracting frequency info:
        freq = frequencies[ratio]

        # Working out percentages:
        percentage_ratio = freq / sequence_dict_len
        percentage = results_templates['file percentage'].format(percentage_ratio)

        # Writing line into the file:
        print(name, seq, ratio_prepped, freq, percentage, sep=DELIMITER, file=analysis_file)


# All done!
print(results_templates['finished'])


# to check your code opena and read a line:
with open(SEQUENCE_ANALYSIS_PATH, mode='r') as analysis_file:
    line = analysis_file.readline()
    print(line)

# note: dictionaries do not always preserve the order of
# data, so you may see a different 1st entry compared to
# the original order that the data was loaded.
# example line:
# MK1BvB5b,ACFRQYCHMARS...,0.283,786,7.86%
