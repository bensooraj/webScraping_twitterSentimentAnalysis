# Importing all necessary libraries
from bs4 import BeautifulSoup

############################## ** Note ** ####################
# The following import need not be performed.               ##
# I am just letting them stay :D                            ##
from urllib.request import urlopen                          ##
##############################################################

from selenium import webdriver
import codecs

# Custom library I've written to pull, store, analyse relevant tweets and returns the sentiment
import tweetSearchAndAnalysis

# Web scraping function
# As the web-page layout of each wepgage is different the following 
# function/module is relevant only for "http://m.imdb.com/feature/bornondate"

def imdbWebScraping():
    nameOfCelebrities = []
    celebrityKeyValue = {}
    counter = 0

    BASE_URL = "http://m.imdb.com/feature/bornondate" # As given in the problem statement
    
	# The page content is dynamic, so, a webdriver is required to emulate a browser
	# environment and run the javascript functions.
    driver = webdriver.Firefox()
    #driver.save_screenshot('screen.png')
    driver.get(BASE_URL)

    html = driver.page_source
    #driver.close()

    # I couldn't download lxml for python 3.4, therefore, I am using the 
	# "html5lib" module to parse the html file
	soup = BeautifulSoup(html, "html5lib")
    boccat = soup.find("section", "posters list")
    bornDate = boccat.findChild("h1").text

    celebrityNameList = []

    for i in boccat.findAll("a", "poster "):

        # for 0 <= n < 10, celebrityKeyValue is of the form
		# celebrityKeyValue{n: {"celebrityName": "text value",
		#                       "celebrityImg": "text value",
		#                       "profession": "text value",
		#                       "bestMovie": "text value",
		#                       "tSentiment": "Positive/Negative/Neutral" <== This is calculated in the main module
		#                      }
		#                   }
		#
		celebrityKeyValue[counter] = {}
        
        # Name of the celebrity
		celebrityName = i.find("span", "title").text
        celebrityNameList.append(celebrityName)
        celebrityKeyValue[counter]["celebrityName"] = celebrityName

        # Celebrity's image link: "*.jpg"
		celebrityKeyValue[counter]["celebrityImg"] = i.img["src"]

        # Parsing Profession and the Best Movie
		profession, bestMovie = i.find("div", "detail").text.split(",")

        # Profession
		celebrityKeyValue[counter]["profession"] = profession

        # Best Movie
		celebrityKeyValue[counter]["bestMovie"] = bestMovie

        counter += 1

    # Return a list of Celebrity names and key-value dict containing all celebrity details
	return nameOfCelebrities, celebrityKeyValue

if __name__ == '__main__':

    # Scrape the website and celevrity details (as a key-value dict)
	nameOfCelebrities, celebrityKeyValue = imdbWebScraping()
    
    # Define a handle(object) for class "tweetSearchAndAnalysis" within the 
	# module "tweetSearchAndAnalysis". This handle will be used for obtaining the
	# twitter sentiment by the celebrity name
	celebrity = tweetSearchAndAnalysis.tweetSearchAndAnalysis()

    # Final output will be stored at "finalOutput.txt"
	outputFile = codecs.open("finalOutput.txt", 'w', "utf-8")
    
	# Loop to printout the o/p of the form
	# 1.	Name of the celebrity:
	# 2.	Celebrity Image:
	# 3.	Profession:
	# 4.	Best Work:
	# 5.	Overall Sentiment on Twitter: Positive, Negative or Neutral
    for i in range(10):

        celebrityName = celebrityKeyValue[i]["celebrityName"]
        celebrity.tweetSearch(celebrityName)
        
		# Overall sentiment on twitter is calculated from within
		# the loop for each celebrity
		celebrityKeyValue[i]["tSentiment"] = celebrity.tweetSentimentAnalysis()

        outputFile.write("Name of the celebrity: " + celebrityKeyValue[i]["celebrityName"] + "\n")
        outputFile.write("Celebrity Image: " + celebrityKeyValue[i]["celebrityImg"] + "\n")
        outputFile.write("Profession: " + celebrityKeyValue[i]["profession"] + "\n")
        outputFile.write("Best Work: " + celebrityKeyValue[i]["bestMovie"] + "\n")
        outputFile.write("Overall Sentiment on Twitter: " + celebrityKeyValue[i]["tSentiment"] + "\n")
        outputFile.write("\n\n")

    outputFile.close()
        

    
    

    
