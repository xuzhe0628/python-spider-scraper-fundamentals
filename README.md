# Python Web crawler and scraper fundamentals

## Content
1. Web crawl and scraper
2. GET and POST
3. Capture web via urllib
4. Powerful requests
5. Introduction to scrapy

### Web crawler and scraper
http://stackoverflow.com/questions/3207418/crawler-vs-scraper

A crawler get web pages from a starting page based one some rules or conditions. It downloads whatever it found.

A scraper extracts data from pages that we downloaded by a crawler, so that we can store them into databases or other data management systems.

### HTTP, GET and POST
https://www.w3schools.com/tags/ref_httpmethods.asp

The Hypertext Transfer Protocol (HTTP) is designed to enable communications between clients and servers. HTTP works as a request-response protocol between a client and server. A web browser may be the client, and an application on a computer that hosts a web site may be the server.

Two commonly used methods for a request-response between a client and server are: GET and POST.

* GET - Requests data from a specified resource
* POST - Submits data to be processed to a specified resource

#### The GET Method
Note that the query string (name/value pairs) is sent in the URL of a GET request:

`/test/demo_form.php?name1=value1&name2=value2`

Some other notes on GET requests:
* GET requests can be cached
* GET requests remain in the browser history
* GET requests can be bookmarked
* GET requests should never be used when dealing with sensitive data
* GET requests have length restrictions
* GET requests should be used only to retrieve data

#### The POST Method
Note that the query string (name/value pairs) is sent in the HTTP message body of a POST request:
`POST /test/demo_form.php HTTP/1.1
Host: w3schools.com
name1=value1&name2=value2`

Some other notes on POST requests:
* POST requests are never cached
* POST requests do not remain in the browser history
* POST requests cannot be bookmarked
* POST requests have no restrictions on data length

### Capture web via urllib


### Powerful requests


### Introduction to scrapy


### Introduction to Selenium
