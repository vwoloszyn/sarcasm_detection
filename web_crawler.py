# -*- coding: utf-8 -*-


"""
This is a crawler to get quotes by tags
Thaaks goodreads.com ;) 
"""




from BeautifulSoup import BeautifulSoup
import urllib2
import pandas as pd

#how to use beautifulsoup
#http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup

def StripTags(text):
     finished = 0
     while not finished:
         finished = 1
         start = text.find("<")
         if start >= 0:
             stop = text[start:].find(">")
             if stop >= 0:
                 text = text[:start] + text[start+stop+1:]
                 finished = 0
     return text

def get_quotes(max_pages, tag, ):
	quotes=[]
	for i in xrange(max_pages):
		url="https://www.goodreads.com/quotes/tag/"+str(tag)+"?page="+str(i)+"&utf8=%E2%9C%93"
		print url
		page=urllib2.urlopen(url)
		soup = BeautifulSoup(page.read())
		mydivs = soup.findAll("div", { "class" : "quoteText" })
		for div in mydivs:
			quotes.append(StripTags(div.text))
		

	#return quotes


##################
if __name__ == "__main__":
	max_pages=27
	tag="sarcastic"
	dataset_output="sarcasm.csv"

	#crawling
	quotes = get_quotes(max_pages, tag)

	#saving to csv
	pd.DataFrame(quotes).to_csv(dataset_output)


