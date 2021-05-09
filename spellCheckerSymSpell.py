# Shahriyar Mammadli
# The code performs smart spell checking using the SymSpell library
# Import required libraries
import helperFunctions as hf
import pickle
from symspellpy import SymSpell, Verbosity

# Set parameters
# Set reference text file name
refFileName = 'referenceText.txt'
# Set frequency list file name
freqFileName = 'frequency_list_aze.txt'
# Set vocabulary file name
vocabFileName = 'wordList.pickle'

# Read the wordList which is Azerbaijani vocabulary
with open(vocabFileName, 'rb') as handle:
    vocabulary = pickle.load(handle)

# Create frequency list of Azerbaijani language
frequencyList = hf.createFrequencyList(refFileName, vocabulary['Words'].tolist())

# Write frequency list into .txt file. Pickle can also be used for the same purpose
# Disable disable if .txt file is already generated
# hf.writeTXT(frequencyList, freqFileName)

# Create SymSpell object and read the frequency list
symspell = SymSpell()
symspell.load_dictionary(freqFileName, 0, 1, encoding="utf-8")

word = "yaxsı"
# Use documentation to perform custom edits
# https://symspellpy.readthedocs.io/en/latest/api/index.html
suggestions = symspell.lookup(word, Verbosity.CLOSEST,
                               max_edit_distance=2, include_unknown=True)

# List the suggestions for the word, in descending order
for suggestion in suggestions:
    print(suggestion)

# TODO: Create a better and clean reference text, REMOVE reference text from here, copy to datasets section