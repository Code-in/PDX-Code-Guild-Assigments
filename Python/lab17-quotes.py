import requests

class QuoteOfTheDay():
    # Method - inializer for the qotd site class
    def __init__(self, keyword=None):
        # Note: in real code you would never want to have this in your soure code or check it into a git repo.
        self.site_token = "855df50978dc9afd6bf86579913c9f8b"
        self.keyword_url = None
        if keyword != None:
            self.keyword = keyword
            self.keyword_url = f"https://favqs.com/api/quotes?page=<page>&filter={keyword}"
        self.qotd_url = 'https://favqs.com/api/qotd'
    
    # Method - returns the single quote url
    def get_qotd_url(self):
        return self.qotd_url
    
    # Method - return the keyword url
    def get_keyword_url(self):
        return self.keyword_url
    
    # Method - return the token string
    def get_qotd_string_token(self):
        return self.site_token

    # Method - set the base url for the keyword request less the token
    def set_keyword(self, keyword):
        self.keyword = keyword
        self.keyword_url = f"https://favqs.com/api/quotes?page=<page>&filter={keyword}"

    # Method - Get a single quotes from the favqs.com
    def get_quote_of_the_day_as_string(self):
        api_data = GetWebAPIData(self.get_keyword_url())
        api_output_dict = api_data.get_ouput()
        return api_output_dict['quote']['body']

    # Method - Get a list of quotes from the favqs.com for a specific keyword
    def get_list_of_quotes_for_keyword(self, keyword):
        self.set_keyword(keyword)
        api_data = GetWebAPIData(self.get_keyword_url(), self.get_qotd_string_token())
        api_output_dict = api_data.get_ouput()
        quotes = api_output_dict['quotes']
        output = []
        for quote in quotes:
            output.append(quote['body'])
        return output


class GetWebAPIData():
    # Method - inializer for the Web API Response
    def __init__(self, url, token=None):
        if token != None:
            token_header = {'Authorization': f'Token token="{token}"'}
            self.response = requests.get(url, headers=token_header)
        else:
            self.response = requests.get(url)

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


# Function - for the lab17 coding exercise which provides the version 1 output
def lab17_verion1():
    qotd = QuoteOfTheDay()
    print(qotd.get_quote_of_the_day_as_string())


# Function - Prints the header for the quotes as they are broken up over multiple pages
def print_stats_about_quotes(keyword, page_count, last_count):
    print(f"{last_count} quotes associated with {keyword} - page {page_count}")

# Function - for printing a range of quote from a list of quotes
def print_quotes(accum_quote_counts, range_count, list_of_quotes):
    for i in range(accum_quote_counts, range_count):
        print(f"Quote {i + 1}: {list_of_quotes[i]}")

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

# determines how many quotes can be displayed
def how_many_quotes_to_show(accum_quote_counts, num_of_quote_per_page, len_of_list_quotes):
    if accum_quote_counts + num_of_quote_per_page > len_of_list_quotes: # check to see how many quotes are left and if we have enough to do a full
        range_count = len_of_list_quotes
        quotes_per_page = len_of_list_quotes - accum_quote_counts # we don't have enough quotes to do a full page of quotes so only process what's let
    else:
        range_count = accum_quote_counts + num_of_quote_per_page # we have enough quotes to do a full page so let set range to a full page count
    return range_count, quotes_per_page

# Function - for the lab17 coding exercise which provides the version 2 output
def lab17_verion2():
    qotd = QuoteOfTheDay()
    keyword = None
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

    if keyword == None:

        # Get the keyword for the qotd site from the user
        keyword = get_keyword_from_user()

        # Retrieve the list of quotes from the qotd site using the users keyword
        list_of_quotes = qotd.get_list_of_quotes_for_keyword(keyword)
        
        # setup counter conditionals
        len_of_list_quotes = len(list_of_quotes)
        num_of_quote_per_page = 10
        accum_quote_counts = 0
        accum_page_count = 1
        quotes_per_page = 10
        range_count = 0

        while True:
                
            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
            # determine how many quotes can be displayed
            range_count, quotes_per_page = how_many_quotes_to_show(accum_quote_counts, num_of_quote_per_page, len_of_list_quotes)

            print_stats_about_quotes(keyword, accum_page_count, quotes_per_page) # print info about the quotes

            print_quotes(accum_quote_counts, range_count, list_of_quotes) # print the quotes for the current page.

            print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")

            # increment our counter conditionals
            accum_quote_counts += num_of_quote_per_page
            accum_page_count += 1

            # Lets now ask if the list of quotes have all been printed.
            if accum_quote_counts > len_of_list_quotes or print_next_or_quit(): # if user decides to quit then we need to set action to false and break
                break

         

# Function - Main processing function where you can easily set what version of the code you want to utilize
def main():
    #lab17_verion2()
    lab17_verion2()


# Execute the main() function
main()