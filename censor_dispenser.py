### Project: Censor Dispenser
### Author: Daniel Xiang
### Version: 1.0.0
### Since: 2020-03-19

import re
import nltk
from typing import List


def to_stars(words: str) -> str:
    """
    param word: a word or phrase
    || Return censored stars, which length corresponds to the word length.
    """
    words = words.split()
    result = []
    for word in words:
        stars = ''
        for char in word:
            stars += '*'
        result.append(stars)
    result = ' '.join(result)
    return result


def censor1(phrase: str, txt: str) -> str:
    """
    param phrase: word or phrase to be censored
    param txt: whole text
    || Retrun censored text.
    """
    if len(phrase) == 0: return txt
    censored = to_stars(phrase)
    return txt.replace(phrase, censored)


def censor2(word_list: List[str], txt: str) -> str:
    """
    param word_list: a list of words or phrases to be censored
    param txt: whole text
    || Retrun censored text.
    """
    if len(word_list) == 0: return txt
    for word in word_list:
        stars = to_stars(word)
        txt = re.sub(r'\b{}\b'.format(word), stars, txt, flags=re.IGNORECASE)
    return txt


def censor3(neg_words: List[str], pro_terms: List[str], txt: str) -> str:
    """
    param neg_words: a list of negative words to be censored
    param pro_terms: a list of proprietary terms to be censored
    param txt: whole text
    || Retrun censored text.
    """
    txt = censor2(pro_terms, txt)

    # First, we create a dictionary to hold position : word pair
    pos_word = {} 
    for word in neg_words:
        index = txt.lower().find(word)
        if index != -1:
            pos_word[index] = word

    # Next, we replace each word starting from the 2nd position
    sorted_pos = sorted(pos_word)
    for i in range(2, len(sorted_pos)):
        the_word = pos_word[sorted_pos[i]]
        stars = to_stars(the_word)
        txt = re.sub(r'\b{}\b'.format(the_word), stars, txt, flags=re.IGNORECASE)

    return txt


def censor4(neg_words: List[str], pro_terms: List[str], txt: str) -> str:
    """
    param neg_words: a list of negative words to be censored
    param pro_terms: a list of proprietary terms to be censored
    txt: the original text to be censored
    || Retrun censored text.
    """
    txt = censor2(neg_words + pro_terms, txt)
    tokens = nltk.word_tokenize(txt)

    j = 0
    while j < len(tokens):
        if '*' in tokens[j]:
            i = j - 1
            k = j + 1
            while i >= 0 and '*' not in tokens[i] and not tokens[i].isalnum(): 
                i -= 1
            while k < len(tokens) and '*' not in tokens[k] and not tokens[k].isalnum(): 
                k += 1

            if i >= 0:
                tokens[i] = to_stars(tokens[i])
            if k < len(tokens):
                tokens[k] = to_stars(tokens[k])

            j = k + 1

        else: j += 1

    my_ans = ' '.join(tokens).replace(' , ',', ').replace(' .','.').replace(' !','!').replace(' ?','?').replace(' : ',  ':').replace(" '", "'")
    return my_ans
