import requests
import re


# Read Book Class which I'll utilize to encapsulate the reading and parsing of the text
class ReadBook():

    # Class intailaizer
    def __init__(self, link, web):
        self.link = link
        self.web = web
        self.text = ""
        self.character_count = 0
        self.word_count = 0
        self.sentance_count = 0
        self.word_length_average = 0
        self.sentance_length_average = 0
        self.cari = 0

    # Method - process a specific book for the ARI data
    def read_book(self):
        self.text = self.read_in_text(self.web)
        self.character_count, self.word_count  = self.parse_text_into_counts(self.text)
        self.sentance_count = self.parse_text_in_sentance_count(self.text)
        self.word_length_average  = self.compute_word_length_average()
        self.sentance_length_average = self.compute_sentance_length_average()
        self.cari = self.compute_automated_readability_index()

    # Method - processes the stext from web site or from a file on disk
    def read_in_text(self, web):
        if web:
            response = requests.get(self.link)
            response.encoding = 'utf-8' # set encoding to utf-8
            text = response.text
        else:
            with open('raven.txt', 'r', encoding='utf-8') as file:
                text = file.read()
        return text

    # Method - parse the text from site or disk into a word count dictionary
    def parse_text_into_counts(self, text):
        regex = r'\w+'
        wordlist=re.findall(regex, text)
        character_count = 0
        word_count = 0

        for word in wordlist:
            word = word.lower()
            character_count += len(word)
            word_count += 1
                
        return character_count, word_count

    # Method - break the text in to sectances and count them
    def parse_text_in_sentance_count(self, text):
        regex = r'\b[!?.]'
        sentance_end_punputation_list=re.findall(regex, text)
        return len(sentance_end_punputation_list)

    # Method - averages word lengths against the overall character count
    def compute_word_length_average(self):
        return self.character_count/self.word_count

    # Method - averages sentance lengths against the overall word count
    def compute_sentance_length_average(self):
        return self.word_count/self.sentance_count

    # Method - Computes the reability of a specific piece of text
    def compute_automated_readability_index(self):
        cari = (4.71 * self.word_length_average) + (0.5*self.sentance_length_average) - 21.43
        return cari


# This class handles the books and url associations
class ProjectGutenbergBooks():
    def __init__(self):
        self.books_available_with_urls = {
        "The Ambassadors From Venus": "https://www.gutenberg.org/files/64045/64045-0.txt", 
        "Swordsman of Lost Terra": "https://www.gutenberg.org/files/64044/64044-0.txt",
        "Enchantress of Venus": "https://www.gutenberg.org/files/64043/64043-0.txt", 
        "Nuori Suomi I-III: Novelleja ja kertomuksia suomalaisilta kirjailijoilta": "http://www.gutenberg.org/cache/epub/64042/pg64042.txt",
        "Dogtown": "https://www.gutenberg.org/files/64041/64041-0.txt", 
        "The Girl's Own Paper": "https://www.gutenberg.org/files/64040/64040-0.txt", 
        "The Blue Balloon: A Tale of the Shenandoah Valley": "https://www.gutenberg.org/files/64039/64039-0.txt",
        "Uit den Kunstschat der Bakongos": "https://www.gutenberg.org/files/64038/64038-0.txt", 
        "Das Leben Jesu. English": "https://www.gutenberg.org/files/64037/64037-0.txt", 
        "Black Pawl": "https://www.gutenberg.org/files/64036/64036-0.txt"
        }
        self.books_and_index_number = []

    # Method - output the list for books to select
    def output_book_options_for_computing_ari(self):
        for k, v in self.books_available_with_urls.items():
            self.books_and_index_number.append(k)

        print("<<-=-=-=-=-= List of books to choose from =-=-=-=-=-=-=->>")
        for i in range(len(self.books_and_index_number)):
            print(f"Select \"{i}\" for Book Title: \"{self.books_and_index_number[i]}\"")
        print("<<-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=>>\n")


    # Method - returns a book url from and index
    def get_book_url_with_index(self, index):
        key_name = self.books_and_index_number[index]
        return self.books_available_with_urls[key_name]

    # Method - returns book name from an index
    def get_book_name_with_index(self, index):
        return self.books_and_index_number[index]
            

#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Functions below are for REPL and Runtime code
#-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Function - handles the text from user to exit the REPL
def quit_or_continue():
    while True:
        quit = input("To quit type [quit, stop or exit] or just press the \"Return key\" to continue: ")
        quit = quit.lower()
        if quit in ['q', 'quit', 's', 'stop', 'e', 'exit']:
            return True
        else:
            return False


# Function - asks the user enters an index for the book they want to process
def what_book_to_process(books):
    while True:
        number = input("Type the number of the book you want to compute the Automated Readability Index (ARI) on: ")
        if number.isdigit() and (0 <= int(number) < len(books.books_and_index_number)):
            return int(number)

# Function - process a book and prints out all the details about it Automated Readability Index (ARI).
def select_a_book_to_compute():
    books = ProjectGutenbergBooks()
    books.output_book_options_for_computing_ari()
    book_index = what_book_to_process(books)
    book_url = books.get_book_url_with_index(book_index)
    book_reader = ReadBook(book_url, True)
    book_reader.read_book()
    print(f"Book Title: {books.get_book_name_with_index(book_index)}")
    print(f"Sentance Count: {book_reader.sentance_count}")
    print(f"Word Count: {book_reader.word_count}")
    print(f"Character Count: {book_reader.character_count}")
    print(f"Computed Automated Readability Index (ARI): {book_reader.cari}")


# Function - Main processing loop which contains the app REPL
def main():
    print("\n\nWelcome Compute Automated Readability Index (ARI) 5000")
    quit = False
    while True:
        select_a_book_to_compute()
        quit = quit_or_continue()
        if quit:
            break

main()