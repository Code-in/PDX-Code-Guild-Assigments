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
def print_a_page_of_quotes(keyword, page_count, last_count):
    print(f"{last_count} quotes associated with {keyword} - page {page_count}")

# Function - Ask the user for input to print next page of quotes or exit
def print_next_or_quit():
    while True:
        action = input("Enter 'next page' or 'done': ")
        action = action.lower()
        if action in ['np', 'n', 'next page', 'd', 'done']:
            if action in ['np', 'n', 'next page']:
                return True
            else:
                return False

# Function - for the lab17 coding exercise which provides the version 2 output
def lab17_verion2():
    qotd = QuoteOfTheDay()
    keyword = ''
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    while True:
        keyword = input("Enter a keyword to search for in quotes: ")
        if keyword.isascii():
            break

    if not keyword == '':
        list_of_quotes = qotd.get_list_of_quotes_for_keyword(keyword)
        quote_counts = 0
        page_count = 1
        action = True
        while True:
            if quote_counts < len(list_of_quotes) and action:
                
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                last_count = 0
                quotes_per_page = 10
                if quote_counts + 10 > len(list_of_quotes):
                    last_count = len(list_of_quotes)
                    quotes_per_page = len(list_of_quotes) - quote_counts
                else:
                    last_count = quote_counts + 10

                print_a_page_of_quotes(keyword, page_count, quotes_per_page)
                for i in range(quote_counts, last_count):
                    print(f"Quote {i + 1}: {list_of_quotes[i]}")
                print("-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-")
                # increment our conditionals
                quote_counts += 10
                page_count += 1

                # Lets not ask if the list of quotes have all been printed.
                if quote_counts < len(list_of_quotes):
                    action = print_next_or_quit()
                else:
                    break  # Where done let's get out of here
            else:
                break # Where done let's get out of here
         

# Function - Main processing function where you can easily set what version of the code you want to utilize
def main():
    #lab17_verion2()
    lab17_verion2()


# Execute the main() function
main()