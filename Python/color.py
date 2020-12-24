
import requests


import colorama
colorama.init()


class QuoteAPI:
    def __init__(self):
        self.qotd_url = 'https://favqs.com/api/qotd'
    
    def get_qotd(self):
        response = requests.get(self.qotd_url)
        data = response.json()
        quote = {
            'body': data['quote']['body'],
            'author': data['quote']['author'],
            'tags': data['quote']['tags']
        }
        return quote
    





quote_api = QuoteAPI() # instantiation, invoking the initializer to create an instance (object) of the class (blueprint)
print(quote_api.qotd_url)

qotd = quote_api.get_qotd()
print(colorama.Fore.BLUE + '"' + qotd['body'] + '"' + colorama.Fore.CYAN + ' - ' + qotd['author'] + colorama.Style.RESET_ALL)
print(colorama.Style.DIM + ', '.join(qotd['tags']))
print(colorama.Style.RESET_ALL)
print(colorama.Fore.RED + colorama.Style.DIM + 'hello' + colorama.Style.NORMAL + 'hello' + colorama.Style.BRIGHT + 'hello')










