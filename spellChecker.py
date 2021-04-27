# Shahriyar Mammadli
# Import required libraries
import re
from collections import Counter
import pickle

# Set parameters
# Read the alphabet
with open('alphabet.txt', encoding="utf8") as f:
    alphabet = f.readline()

def words(text):
    return re.findall(r'\w+', text.lower())

WORDS = Counter(words(open('referenceText.txt', encoding="utf8").read()))

with open('container.pickle', 'wb') as handle:
    pickle.dump(WORDS, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open('container.pickle', 'rb') as handle:
    WORDS = pickle.load(handle)

def P(word, N=sum(WORDS.values())):
    "Probability of `word`."
    return WORDS[word] / N

def correction(word, alphabet):
    "Most probable spelling correction for word."
    return max(candidates(word, alphabet), key=P)

def candidates(word, alphabet):
    "Generate possible spelling corrections for word."
    return (known([word]) or known(edits1(word, alphabet)) or known(edits2(word, alphabet)) or [word])

def known(words):
    "The subset of `words` that appear in the dictionary of WORDS."
    return set(w for w in words if w in WORDS)

def edits1(word, alphabet):
    "All edits that are one edit away from `word`."
    splits = [(word[:i], word[i:])    for i in range(len(word) + 1)]
    deletes = [L + R[1:]               for L, R in splits if R]
    transposes = [L + R[1] + R[0] + R[2:] for L, R in splits if len(R)>1]
    replaces = [L + c + R[1:]           for L, R in splits if R for c in alphabet]
    inserts = [L + c + R               for L, R in splits for c in alphabet]
    return set(deletes + transposes + replaces + inserts)

def edits2(word, alphabet):
    "All edits that are two edits away from `word`."
    return (e2 for e1 in edits1(word, alphabet) for e2 in edits1(e1, alphabet))

# Correct words of a sentence
def correctSentence(sentence, alphabet):
    corrections = [correction(word, alphabet) for word in sentence.split()]
    return (' '.join(corrections))

print(correctSentence('Dünizə gedun yorda ümami yaxınaşma', alphabet))
