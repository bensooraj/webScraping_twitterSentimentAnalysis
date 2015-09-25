# Edureka Python Project Documentation

## Problem Statement
IMDB provides a list of celebrities born on the current date. Below is the link:
http://m.imdb.com/feature/bornondate

Get the list of these celebrities from this webpage using web scraping (the ones that are displayed i.e top 10). You have to extract the below information:

1.	Name of the celebrity
2.	Celebrity Image
3.	Profession
4.	Best Work

Once you have this list, run a sentiment analysis on twitter for each celebrity and finally the output should be in the below format

1.	Name of the celebrity:
2.	Celebrity Image:
3.	Profession:
4.	Best Work:
5.	Overall Sentiment on Twitter: Positive, Negative or Neutral

Hint: Use IMDB scrapping sample example as reference for scraping the mentioned web page. For sentiment analysis use the Twitter sentiment code as reference.

Please Note That I Am Using Python 3.4

## Tools and Packages Used

•	Version: Python 3.4 [VERY IMPORTANT]
•	Tweepy  Tweepy is an open-sourced, hosted on GitHub, and enables Python to communicate with the Twitter platform and use its API. Here's the documentation.

•	Codecs  The codecs module provides stream and file interfaces for transcoding data in your program. In this project I use the module for storing the tweets as Unicode text. Here's the documentation.

•	String (punctuation)  To strip the tweets of all punctuations.

•	BeautifulSoup  Beautiful Soup provides a few simple methods and Pythonic idioms for navigating, searching, and modifying a parse tree using Python parsers like lxml and html5lib. It automatically converts incoming documents to Unicode and outgoing documents to UTF-8. Here's the documentation.

•	Selenium  The webdriver kit emulates a web-browser (I chose FireFox) and executes the JS scripts to load the dynamic  content.

## Challenges Faced during the project

### Tweepy has an issue with Python 3

Error message: 
 TypeError: Can't convert 'bytes' object to str implicitly inside: tweepy\streaming.py

Solution:  
Can be found at https://github.com/tweepy/tweepy/issues/615. In streaming.py: I changed line 161 to

self._buffer += self._stream.read(read_len).decode('ascii')

and line 171 to

self._buffer += self._stream.read(self._chunk_size).decode('ascii')

and then reinstalled.

### The IMDB website has dynamic content:

Reference: 
http://fruchter.co/post/53164489086/python-headless-web-browser-scraping-on-amazon

Description:
Had to use the Selenium’s webdriver to emulate a Firefox browser and execute the JS functions which dynamically fetches the details of celebrities born on the current day.


