# Shahriyar Mammadli
# The code performs statistical (not AI based) corrections of spelling errors or typos.
# Import required libraries
import re
from collections import Counter
import pickle

# Set parameters
# Set reference text file path
fileName = 'referenceText.txt'
# Set the alphabet path
alphabetPath = 'alphabet.txt'

# This function reads a text file and creates a table of words and their frequencies
def formDictionary(fileName):
    # Create the frequency table of the words
    WORDS = Counter(re.findall(r'\w+', open(fileName, encoding="utf8").read().lower()))
    # Write the result into a pickle file
    with open('container.pickle', 'wb') as handle:
        pickle.dump(WORDS, handle, protocol=pickle.HIGHEST_PROTOCOL)

# Returns the candidate words for the input string
# Possibilities are 1. input word is already a known word, no need...
# ...for correction, 2. input word is one edit away from the original word,
# ...3. input word is two edit away from the original word, 4. could not succeed...
# ...to find a candidate word and returns the input word itself.
def candidates(word, alphabet):
    return (known([word]) or known(distance1(word, alphabet)) or known(distance2(word, alphabet)) or [word])

# Filter out the words that are not in the dictionary
def known(words):
    return set(w for w in words if w in WORDS)

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

# Correct words of a sentence
def correctSentence(sentence, alphabet):
    corrections = [max(candidates(word, alphabet), key=P) for word in sentence.split()]
    return (' '.join(corrections))

try:
    print("Trying to read pre-formed word-frequency table.")
    with open('container.pickle', 'rb') as handle:
        WORDS = pickle.load(handle)
except:
    print("Couldn't find the table, trying to recreate it using the reference text.")
    try:
        formDictionary(fileName)
        with open('container.pickle', 'rb') as handle:
            WORDS = pickle.load(handle)
    except:
        print("Couldn't find the reference file.")
        quit()

# Probablity calculation of the word is calculated basing on the frequency of the word...
# ...in the reference text.
def P(word, N=sum(WORDS.values())):
    return WORDS[word] / N

# Read the alphabet
with open(alphabetPath, encoding="utf8") as f:
    alphabet = f.readline()
print(correctSentence('Dünizin səthinnda üfüqq xət', alphabet))
