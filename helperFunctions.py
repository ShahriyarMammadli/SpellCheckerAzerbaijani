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
def createFrequencyList(fileName, wordList, enablePickle=False, pickleFileName='container.pickle'):
    # Create counter object of vocabulary
    vocabulary = Counter(wordList)
    # Create the frequency list (counter object) from reference text
    frequencyList = Counter(re.findall(r'\w+', open(fileName, encoding="utf8").read().lower()))
    # Add vocabulary to the general frequency list
    frequencyList = frequencyList + vocabulary
    with open(pickleFileName, 'wb') as handle:
        pickle.dump(frequencyList, handle, protocol=pickle.HIGHEST_PROTOCOL)
    return frequencyList

# The following function writes frequency list into .txt file
def writeTXT(frequencyList, fileName):
    # Convert counter object to pandas file then write into .txt
    df = pd.DataFrame.from_dict(frequencyList, orient='index').reset_index()
    np.savetxt(fileName, df.values, fmt='%s', encoding="utf-8")

# Do the spelling fixing operations in one distance
def distance1(word, alphabet):
    splits = [(word[:i], word[i:]) for i in range(len(word) + 1)]
    deletes = [L + R[1:] for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces = [L + c + R[1:] for L, R in splits if R for c in alphabet]
    inserts = [L + c + R for L, R in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

# Do the spelling fixing operations in two distance
def distance2(word, alphabet):
    return (e2 for e1 in distance1(word, alphabet) for e2 in distance1(e1, alphabet))

# Filter out the words that are not in the dictionary
def known(words, frequencyList):
    return set(w for w in words if w in frequencyList)

# Returns the candidate words for the input string
# Possibilities are 1. input word is already a known word, no need...
# ...for correction, 2. input word is one edit away from the original word,
# ...3. input word is two edit away from the original word, 4. could not succeed...
# ...to find a candidate word and returns the input word itself.
def candidates(word, alphabet, frequencyList):
    return (known([word], frequencyList)
            or known(distance1(word, alphabet), frequencyList)
            or known(distance2(word, alphabet), frequencyList)
            or [word])

# Probablity calculation of the word is calculated basing on the frequency of the word...
# ...in the reference text.
def P(word, frequencyList):
    N = sum(frequencyList.values())
    return frequencyList[word] / N

# Correct words of a sentence
def correct(sentence, alphabet, frequencyList):
    corrections = []
    for word in sentence.split():
        # List to hold candidate words with their corresponding probabilities
        probability = []
        for candidate in candidates(word, alphabet, frequencyList):
            probability.append((candidate, P(candidate, frequencyList)))
        corrections.append(max(probability,key=lambda x:x[1])[0])
    return (' '.join(corrections))

