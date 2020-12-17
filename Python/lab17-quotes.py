import requests

class QuoteOfTheDay():
    # Method - inializer for the qotd site class
    def __init__(self):
        # Note: in real code you would never want to have this in your soure code or check it into a git repo.
        self.site_token = "855df50978dc9afd6bf86579913c9f8b"
        self.set_quote_of_the_day_url()
        self.set_quotes_url()
    
    # Method - returns the single quote url
    def get_qotd_url(self):
        return self.qotd_url
    
    # Method - return the quotes url
    def get_quotes_url(self):
        return self.quotes_url
    
    # Method - return the token string
    def get_qotd_string_token(self):
        return self.site_token

    # Method - set the base url for "quote of the day""
    def set_quote_of_the_day_url(self):
        self.qotd_url = 'https://favqs.com/api/qotd'

    # Method - set the base url for quotes
    def set_quotes_url(self):
        self.quotes_url = f"https://favqs.com/api/quotes"

    # Method - Get a single quotes from the favqs.com
    def get_quote_of_the_day_as_string(self):
        api_data = GetWebAPIData(self.get_qotd_url())
        api_output_dict = api_data.get_ouput()
        return api_output_dict['quote']['body']

    # Method - Get a list of quotes from the favqs.com for a specific keyword
    def get_list_of_quotes_for_keyword(self, keyword, page):
        self.set_quotes_url()
        api_data = GetWebAPIData(self.get_quotes_url(), self.get_qotd_string_token(), keyword, page)
        api_output_dict = api_data.get_ouput()
        quotes = api_output_dict['quotes']
        output = []
        for quote in quotes:
            output.append(quote['body'])
        return output


class GetWebAPIData():
    # Method - inializer for the Web API Response
    def __init__(self, url, token=None, keyword=None, page=1):
        if token != None:
            token_header = {'Authorization': f'Token token="{token}"'}
            if keyword != None:
                params = {'page':page, 'filter':keyword }
            self.response = requests.get(url, headers=token_header, params=params)
        else:
            self.response = requests.get(url)

        #print(self.response.url)
        self.response.encoding = 'utf-8' # set encoding to utf-8
        if 'text/plain' in self.response.headers['Content-Type']:
            self.output_type = 'text'
            self.output = self.response_text(self.response)
        elif 'application/json' in self.response.headers['Content-Type']:
            self.output_type = 'json'
            self.output = self.response_json(self.response)
        else:
            print("Content Type Not Supprted")

    # Method - returns the reponse text if the site returns text content
    def response_text(self, response):
        return response.text

    # Method - returns the reponse json if the site returns json content
    def response_json(self, response):
        return response.json()

    def get_ouput(self):
        return self.output


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Function and code for Lab 19 version 1
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Function - for the lab17 coding exercise which provides the version 1 output
def lab17_verion1():
    qotd = QuoteOfTheDay()
    print(qotd.get_quote_of_the_day_as_string())


#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
# Function and code for Lab 19 version 2
#=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=

# Function - Prints the header for the quotes as they are broken up over multiple pages
def print_stats_about_quotes(keyword, accum_page_count, quotes_per_page):
    print(f"{quotes_per_page} quotes associated with {keyword} - page {accum_page_count}")

# Function - for printing a range of quote from a list of quotes
def print_quotes(accum_quote_counts, quotes_per_page, list_of_quotes):
    for i in range(0, quotes_per_page):
        print(f"Quote {accum_quote_counts + i + 1}: {list_of_quotes[i]}")

# Function - Ask the user for input to print next page of quotes or exit
def print_next_or_quit():
    while True:
        action = input("Enter 'next page' or 'done': ")
        action = action.lower()
        if action in ['np', 'n', 'p', 'next page']:
            return False
        elif action in ['d', 'done', 'e', 'exit', 'q', 'quit']:
            return True

# Function - Ask the user for keyword for the qotd site for a specific kind of quotes  to retrieve
def get_keyword_from_user():
    keyword = None
    while True:
        keyword = input("Enter a keyword to search for in quotes: ")
        if keyword.isascii():
            return keyword


# Function - for the lab17 coding exercise which provides the version 2 output
def lab17_verion2():
    qotd = QuoteOfTheDay()
    keyword = None
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    if keyword == None:

        # Get the keyword for the qotd site from the user
        keyword = get_keyword_from_user()
        accum_quote_counts = 0
        accum_page_count = 1
        quotes_per_page = 0

        while True:
        
            # Get a page of quotes for a given keyword
            list_of_quotes = qotd.get_list_of_quotes_for_keyword(keyword, accum_page_count)

            # break out of the while loop if we have not quotes
            quotes_per_page = len(list_of_quotes)
            if quotes_per_page <= 0:
                break

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            # print info about the quotes
            print_stats_about_quotes(keyword, accum_page_count, quotes_per_page)

            # print the quotes for the current page.
            print_quotes(accum_quote_counts, quotes_per_page, list_of_quotes)
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            # # increment our counter conditionals
            accum_quote_counts += quotes_per_page
            accum_page_count += 1

            # # Lets now ask if the list of quotes have all been printed.
            if print_next_or_quit(): # if user decides to quit then we need to set action to false and break
                break

         

# Function - Main processing function where you can easily set what version of the code you want to utilize
def main():

    print("\n\n\n-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Quote of the day: ")   
    lab17_verion1()
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-\n\n\n")
    lab17_verion2()


# Execute the main() function
main()