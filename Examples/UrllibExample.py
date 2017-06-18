import urllib.request
import re

# Regex to match the repo name
REPO_REGEX = re.compile(b'.*/(.*/python).*', re.IGNORECASE, )

pythonRepo = urllib.request.urlopen(
    'https://github.com/search?utf8=%E2%9C%93&q=python&type=')

# Save the response as a html file
# "wb" means the mode opening the file. "w" means open the file in write mode.
# "b" means open the file in binary mode.

with open('ResultPage.html', 'wb') as resultPage:
    resultPage.write(pythonRepo.read())

# Request the query again and find and print the repo name.
pythonRepo = urllib.request.urlopen(
    'https://github.com/search?utf8=%E2%9C%93&q=python&type=')

for line in pythonRepo:
    if REPO_REGEX.match(line):
        print(REPO_REGEX.match(line).group(1))