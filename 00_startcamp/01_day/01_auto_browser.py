# import webbrowser

# sites = ['www.google.com', 'www.naver.com', 'www.yahoo.com']

# idols = ['bts', 'nrg', 'hot', 'god']
# url = 'https://search.naver.com/search.naver?query='

# for idol in idols:
#     webbrowser.open(url + idol)


import requests

response = requests.get('https://www.naver.com/').status_code
print(response)