"""Text preprocessing helpers used by the training and inference pipeline."""

import nltk
import numpy as np
from nltk.stem.porter import PorterStemmer

# Stemmer used to normalize words before training and inference.
Stemmer = PorterStemmer()


def tokenize(sentence):
    """Split a sentence into individual words."""
    return nltk.word_tokenize(sentence)


def stem(word):
    """Reduce a word to its root form for matching."""
    return Stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    """Create a binary bag-of-words vector for the current sentence."""
    sentence_word = [stem(word) for word in tokenized_sentence]
    bag = np.zeros(len(words), dtype=np.float32)

    for idx, word in enumerate(words):
        if word in sentence_word:
            bag[idx] = 1

    return bag
