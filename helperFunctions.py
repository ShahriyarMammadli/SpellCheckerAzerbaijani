# Shahriyar Mammadli
# This script contains helper functions for spell checking task
from collections import Counter
import re
import pickle
import pandas as pd
import numpy as np

# This function creates a frequency list from reference text file and from...
# ...the vocabulary list (where all words of a language are listed).
# If pickle parameter is enabled then, results will be written into...
# ... a pickle file.
def createFrequencyList(fileName, wordList):
    # Create counter object of vocabulary
    vocabulary = Counter(wordList)
    # Create the frequency list (counter object) from reference text
    frequencyList = Counter(re.findall(r'\w+', open(fileName, encoding="utf8").read().lower()))
    # Add vocabulary to the general frequency list
    frequencyList = frequencyList + vocabulary
    return frequencyList

# The following function writes frequency list into .txt file
def writeTXT(frequencyList, fileName):
    # Convert counter object to pandas file then write into .txt
    df = pd.DataFrame.from_dict(frequencyList, orient='index').reset_index()
    np.savetxt(fileName, df.values, fmt='%s', encoding="utf-8")