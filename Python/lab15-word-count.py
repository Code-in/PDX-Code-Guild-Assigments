

import requests
import re

# processes the stext from web site or from a file on disk
def read_in_text(web):
    if web:
        response = requests.get('https://www.gutenberg.org/files/62897/62897-0.txt')
        response.encoding = 'utf-8' # set encoding to utf-8
        text = response.text
    else:
        with open('raven.txt', 'r', encoding='utf-8') as file:
            text = file.read()
    return text

# parse the text from site or disk into a word count dictionary
def parse_text(text):
    regex = r'\w+'
    wordlist=re.findall(regex, text)
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

# Ask the user for a word and give back the number of occurances in our text
def get_word(word_count_dict):
    while True:
        word = input("What word would you like to determine the occruance for: ")
        if word in word_count_dict:
            return word
        else:
            print(f"There are 0 occurances of the {word} in our text")

# get back the word count for a specific word in the word_count_dict  ionary
def specific_word_count(word, word_count_dict):
    return word_count_dict[word]

# this is the lab exercise for version 2
def version2(word_count_dict):
    # word_dict is a dictionary where the key is the word and the value is the count
    words = list(word_count_dict.items()) # .items() returns a list of tuples
    words.sort(key=lambda tup: tup[1], reverse=True)  # sort largest to smallest, based on count
    for i in range(min(len(words), 10)):  # print the top 10 words, or all of them, whichever is smaller
        print(words[i])

# handle the text from user to exit the REPL
def quit_or_continue():
        quit = input("To quit type [quit, stop or exit]: ")
        quit = quit.lower()
        if quit in ['q', 'quit', 's', 'stop', 'e', 'exit']:
            return True
        else:
            return False

# this is the lab exercise for version 3
def version3(word_count_dict):
    word = get_word(word_count_dict)
    count = specific_word_count(word, word_count_dict)
    print(f"There are {count} occurances of the {word} in our text")

# Ask the user if they want to read text from web site or from disk
def read_text_from_disk_or_web():
    while True:
        word = input("Do you want to read \"The Raven\" from disk or web[d - Disk or w - Web]: ")
        word = word.lower()
        if word in ['w', 'web']:
            return True
        if word in ['d', 'disk']:
            return False

# Main processing loop which contains the app REPL
def main():
    print("Welcome Word Count 5000")
    quit = False
    web = read_text_from_disk_or_web()
    text = read_in_text(web)
    word_count_dict = parse_text(text)
    version2(word_count_dict)
    while True:
        version3(word_count_dict)
        quit = quit_or_continue()
        if quit:
            break

main()