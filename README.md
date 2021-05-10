# SpellCheckerAzerbaijani
The SpellCheckerAzerbaijani project is designed to perform probabilistic and non-AI-based word corrections.

## Introduction
There is a huge shortage of algorithms, tools, and even sources for the Azerbaijani language. One of the fundamental use cases of algorithmic language models is spelling error corrections. Historically, spell-checking algorithms were based on probabilistic fixations of misspelled words. Newer approaches are context-based NLP algorithms. 

This project is only comprised of the most famous and fastest probabilistic algorithms. __NLP model can also be found in my repositories.__ To achieve the task, two famous algorithms have been applied. The first one is [Norvig's algorithm](http://www.norvig.com/spell-correct.html) and the second one is [SymSpell algorithm](https://github.com/wolfgarbe/SymSpell).

## Info
This project requires at least a basic understanding of how spell-checking algorithms works. As additional sources to Norvig's explanation and SymSpell documentation, you can use the following sources as a starting point.
- [Spell Checking Algorithm designs](https://towardsdatascience.com/spelling-correction-how-to-make-an-accurate-and-fast-corrector-dc6d0bcbba5f)
- [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)

## Design
SymSpell Algorithm is available as an open-source library for [Python](https://pypi.org/project/symspellpy/) and some other famous languages. Norvig's Algorithm is also available for many languages, to see details use the pre-given link.

In simplest generalization, algorithms' logic depends on the following steps:

- Initially, various transformations (e.g. transposes + replaces + inserts, etc.) have been applied to the misspelled word.
- Generated words are checked against vocabulary (not just raw words but words with affixes. e.g. raw-word: uşaq, with-affix: uşaqlarla).
- The words that are real (are found in vocabulary) are selected as candidates and their probabilities are calculated based on their usage frequency in language. The frequency list is formed using a large text corpus in the Azerbaijani language (see details in the Data section).

## Data
Three data sources are used for the project.
1. `alphabet.txt`: This is just simply Azerbaijani characters from the alphabet.
2. `referenceText.txt`: This is the large corpus of Azerbaijani text. It contains many articles, publications, and various other scraped open-source data. __To preserve the rights of sources, data scraping code pieces are not published.__ This text file is used to form the words' frequency list.
3. `frequency_list_aze.txt`: This file is formed using referenceText.txt and vocabulary.txt file where all words in Azerbaijani are listed. 
4. `vocabulary.txt`: __This file is also not shared due to copyright issues.__ There may be words that are not in referenceText.txt due to bias. For example, some words are extremely rarely used, or there may be dialectal or technical words that are not usually found in ordinary texts. Instead, a pickle file is formed to avoid direct sharing of the raw file. (Pickle file contains words from referenceText and vocabulary in non-raw format, the raw format of vocabulary is not included in the repository).

## Code
- `spellChecker.py` is the usage of Norvig's algorithms. You can use the `correct()` function to get spelling corrections for sentences or words.
- `spellCheckerSymSpell.py` is a usage of the SymSpell algorithm. Using the lookup function you can get spelling corrections.

### Examples
- `spellChecker.py`: Sending misspelled sentence ***Dünizin səthindakı üfüqq parlağlığ*** as an input. 
```
hf.correct('Dünizin səthindakı üfüqq parlağlığ', alphabet, frequencyList)
```
And the output is as follows:

!["Norvig's algorithm example usage"](screenshots/norvig.PNG?raw=true)

- `spellCheckerSymSpell.py` giving misspelled word ***ilım*** as an input, with maximum 2-distance edit.
```
hf.correct('Dünizin səthindakı üfüqq parlağlığ', alphabet, frequencyList)
```
And the output is as following:

!["SymSpell example usage"](screenshots/symspell.PNG?raw=true)

As seen in the screenshot, all corrections are correct except the last one, which is an unknown word that originates from having misspelled words in reference text.
## Conclusion and Notes
- To make faster predictions, you can store models (e.g. as pickle files) and load them whenever you use them, thus you would avoid feeding the model every time.  
- In case of editing the code for own custom usage, be careful about encoding. Not mentioning `utf-8` can cause a problem while processing Azerbaijani characters.
- For the SymSpell algorithm, in the `spellCheckerSymSpell.py` script, only one function (with simple parameters) is used for demo purposes. Check [documentation](https://symspellpy.readthedocs.io/en/latest/api/index.html)  for all usage scenarios.

## References
1. [Norvig's algorithm](http://www.norvig.com/spell-correct.html
2. [Spell Checking Algorithm designs](https://towardsdatascience.com/spelling-correction-how-to-make-an-accurate-and-fast-corrector-dc6d0bcbba5f)
3. [Levenshtein distance](https://en.wikipedia.org/wiki/Levenshtein_distance)
4. [SymSpell Python](https://pypi.org/project/symspellpy/)
5. [SymSpell documentation](https://symspellpy.readthedocs.io/en/latest/api/index.html)
