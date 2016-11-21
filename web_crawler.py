# -*- coding: utf-8 -*-


"""
This is a crawler to get quotes by tags
Thaaks goodreads.com ;) 
"""

from bs4 import BeautifulSoup
import urllib2
import pandas as pd



#how to use beautifulsoup
#http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup

def StripTags(text):
        finished = 0
        text=text.split("//<![CDATA[")
        text=str(text[0].encode('utf-8'))
        text=text.split('―')
        text=str(text[0])
        return text
                    

def get_quotes(max_pages, tag, ):
	quotes=[]
	for i in xrange(max_pages):
		url="https://www.goodreads.com/quotes/tag/"+str(tag)+"?page="+str(i)+"&utf8=%E2%9C%93"
		print url
		page=urllib2.urlopen(url)
		soup = BeautifulSoup(page.read(),'html.parser')
		mydivs = soup.findAll("div", { "class" : "quoteText" })
		for div in mydivs:
			quotes.append(StripTags(div.text))
		

	return quotes


##################
if __name__ == "__main__":
	max_pages=2
	tag="sarcastic"
	dataset_output="sarcasm.csv"

	#crawling
	quotes = get_quotes(max_pages, tag)

	#saving to csv
	for q in quotes:
		print q


