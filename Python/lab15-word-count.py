

import requests
import re

def read_in_text():
    response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
    response.encoding = 'utf-8' # set encoding to utf-8

    regex = r'\w+'
    wordlist=re.findall(regex, response.text)
    #print(wordlist)
    word_count_dict = {}

    for word in wordlist:
        #print(word.lower())
        word = word.lower()
        if word in word_count_dict:
            word_count_dict[word] += 1
        else:
            word_count_dict[word] = 1
    #print(word_count_dict)
    return word_count_dict

def get_word(word_count_dict):
    while True:
        word = input("What word would you like to determine the occruance for: ")
        if word in word_count_dict:
            return word
        else:
            print(f"There are 0 occurances of the {word} in our text")

def specific_word_count(word, word_count_dict):
    return word_count_dict[word]


def version2(word_count_dict):
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_count_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(len(words), 10)):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

def version3(word_count_dict):
    while True:
        word = get_word(word_count_dict)
        count = specific_word_count(word, word_count_dict)
        print(f"There are {count} occurances of the {word} in our text")






def main():
    print("Welcome Word Count 5000")
    word_count_dict = read_in_text()

    version2(word_count_dict)
    version3(word_count_dict)

main()