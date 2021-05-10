# Shahriyar Mammadli
# The code performs statistical (not AI based) corrections of spelling errors or typos.
# Import required libraries
import pickle
import helperFunctions as hf
# Set parameters
# Set reference text file name
refFileName = 'referenceText.txt'
# Set the alphabet path
alphabetPath = 'alphabet.txt'
# Set vocabulary file path
vocabFileName = 'wordList.pickle'
# Pickle file name
pickleFileName = 'container.pickle'

# Read the wordList which is Azerbaijani vocabulary
with open(vocabFileName, 'rb') as handle:
    vocabulary = pickle.load(handle)

# Read the alphabet
with open(alphabetPath, encoding="utf8") as f:
    alphabet = f.readline()

try:
    print("Trying to read pre-formed word-frequency table.")
    with open(pickleFileName, 'rb') as handle:
        frequencyList = pickle.load(handle)
except:
    print("Couldn't find the table, trying to recreate it using the reference text.")
    try:
        hf.createFrequencyList(refFileName, vocabulary['Words'].tolist(), enablePickle=True, pickleFileName=pickleFileName)
        with open(pickleFileName, 'rb') as handle:
            frequencyList = pickle.load(handle)
    except:
        print("Couldn't find the reference file.")
        quit()

print(hf.correct('Dünizin səthindakı üfüqq parlağlığ', alphabet, frequencyList))
