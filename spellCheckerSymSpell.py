# Shahriyar Mammadli
# The code performs smart spell checking using the SymSpell library
# Import required libraries
import helperFunctions as hf
import pickle
from symspellpy import SymSpell, Verbosity

# Set parameters
# Set reference text file path
refFileName = 'referenceText.txt'
# Set frequency list file path
freqFileName = 'frequency_list_aze.txt'


# Read the wordList which is Azerbaijani vocabulary
with open('wordList.pickle', 'rb') as handle:
    wordList = pickle.load(handle)

# Create frequency list of Azerbaijani language
frequencyList = hf.createFrequencyList(refFileName, wordList['Words'].tolist())

# Write frequency list into .txt file. Pickle can also be used for the same purpose
# Disable disable if .txt file is already generated
# hf.writeTXT(frequencyList, freqFileName)

# Create SymSpell object and read the frequency list
symspell = SymSpell()
symspell.load_dictionary(freqFileName, 0, 1, encoding="utf-8")

word = "yaxsı"
suggestions = symspell.lookup(word, Verbosity.CLOSEST,
                               max_edit_distance=2, include_unknown=True)

# List the suggestions for the word, in descending order
for suggestion in suggestions:
    print(suggestion)
