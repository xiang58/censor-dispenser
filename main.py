### Project: Censor Dispenser
### Author: Daniel Xiang
### Version: 1.0.0
### Since: 2020-03-19

from censor_dispenser import *

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithms", "her", "herself"]

neg_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help","unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressing","concerning", "horrible", "horribly", "questionable"]


def main():
    # Censor email one
    email1 = open('email_one.txt', 'r').read()
    censored1 = censor1('learning algorithms', email1)
    with open('censored_email_one.txt', 'w') as file:
        file.write(censored1)

    # Censor email two
    email2 = open('email_two.txt', 'r').read()
    censored2 = censor2(proprietary_terms, email2)
    with open('censored_email_two.txt', 'w') as file:
        file.write(censored2)

    # Censor email three
    email3 = open('email_three.txt', 'r').read()
    censored3 = censor3(neg_words, proprietary_terms, email3)
    with open('censored_email_three.txt', 'w') as file:
        file.write(censored3)

    # Censor email four
    email4 = open('email_four.txt', 'r').read()
    censored4 = censor4(neg_words, proprietary_terms, email4)
    with open('censored_email_four.txt', 'w') as file:
        file.write(censored4)


if __name__ == "__main__":
    main()
