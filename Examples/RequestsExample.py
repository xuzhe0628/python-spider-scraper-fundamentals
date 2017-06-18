import requests
from bs4 import BeautifulSoup # standard library for parsing html page

# header for simulating the browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "X-Requested-With": "XMLHttpRequest",
}

# creare a session to hold all browser information
gitSession = requests.Session()

# get the auth token from github login page
soup = BeautifulSoup(gitSession.get('https://github.com/login', 
    headers=headers).text,
    'html.parser')
# find the element containing the auth_token by selector
auth_token = soup.find("input", {"name": "authenticity_token"}).attrs['value']
print('auth_token: {}'.format(auth_token))

# prepare the login data using the auth token we got
payload = {
    "commit": "Sign in",
    "authenticity_token": auth_token,
    "login": "your login", # fill your username
    "password": "your password" # fill your password
}

# send a post request to session page to login
# we will need the session as Github request enable cookie and the session can
# help us to keep the cookie for different requests
login = gitSession.post('https://github.com/session', 
    data=payload)

# find my repo names by css selector
soup = BeautifulSoup(login.text, 'html.parser')
repos = soup.find_all("span", class_="repo")
for repo in repos:
    print(repo.text)