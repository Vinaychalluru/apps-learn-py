import json
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches
import random


with open("../assets/dict-master-data.json", "r") as dict_fp:
    dict_data = json.load(dict_fp)
    # print(type(dict_data))


def find_meaning(user_word):
    user_word = user_word.lower()
    word_not_found = ["Sorry. '%s' is not found" % user_word]
    if user_word in dict_data:
        return dict_data[user_word]
    elif user_word.title() in dict_data:
        return dict_data[user_word.title()]
    elif user_word.upper() in dict_data:
        return dict_data[user_word.upper()]
    else:
        # Finding the Close Matches
        match_words = get_close_matches(user_word, dict_data.keys(), 2, 0.6)
        match_flag = "Y"
        while match_flag == "Y" and len(match_words) > 0:
            for w in match_words:
                match_flag = input(
                    "Do you mean %s ? Enter Y for Yes :" % w).upper()
                if match_flag == "Y":
                    return dict_data[w]
            else:
                return word_not_found
        else :
            return word_not_found


# Custom function find_meaning2 implements a costly or inefficient way
def find_meaning2(user_word):
    user_word = user_word.lower()
    word_not_found = ["Sorry. '%s' is not found" % user_word]
    if user_word in dict_data:
        return dict_data[user_word]
    else:
        max_ratio = 0.0
        # match_words = []

        # Not efficient Way - Going through each key in the dict and comparing the ratio
        for k in dict_data:
            k_ratio = SequenceMatcher(None, user_word, k).ratio()
            if k_ratio > max_ratio:
                # match_words.append(k)
                match_word = k
                max_ratio = k_ratio

        if max_ratio != 0.0:
            # user_ask_flag = input("Do you mean %s ? Enter Y for Yes:" % match_words[0])
            user_ask_flag = input(
                "Do you mean %s ? Enter Y for Yes :" % match_word)
            user_ask_flag = user_ask_flag.upper()
            if user_ask_flag == "Y":
                # return dict_data[match_words[0]]
                return dict_data[match_word]
            else:
                return word_not_found
        else:
            return word_not_found


exit_msgs = ("Thank you!", "Have a Great Day!",
             "Bye. Enjoy your Day!", "Bye. Wish you luck!", "Happy Learning!")
lookup_flag = "Y"
while lookup_flag == "Y":
    print("\n".join(find_meaning(input('Enter a word to Lookup:'))))
    # Custom function find_meaning2 implements a costly or inefficient way
    # print("\n".join(find_meaning2(input('Enter a word to Lookup:'))))
    print()
    lookup_flag = input('Lookup another word? Enter Y for Yes:').upper()
else:
    print(random.choice(exit_msgs))
