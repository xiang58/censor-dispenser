## Censor Dispenser V1.0.0 (2020-03-19)
This project implements several algorithms to censor target words in a given text.

#### Release Notes
- There are total four different emails to be censored, each given a specifc rule and a list of words for censoring.
- `censor1` only censors a specifc provided word or phrase from email one;
- `censor2` censors every word or phrase in a given list from email two; 
- Besides censoring any words from a given list in email three, `censor3` censors any occurance of a word from the "negative words" list after any “negative” word has occurred twice;
- `censor4` censors not only all of the words from given lists, but also censors any words in email four that come before and after a term from those lists.

*\* Project idea adopted from Codecademy* 
