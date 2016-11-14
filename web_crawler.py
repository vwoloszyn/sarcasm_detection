

max_pages=27


def get_quotes(max_pages, tag, ):
	quotes=[]
	for i in xragne(max_pages):
		url="https://www.goodreads.com/quotes/tag/"+str(tag)+"?page="+str(i)+"&utf8=%E2%9C%93"
		from bs4 import BeautifulSoup
		soup=BeautifulSoup(url,'html.parser')
                soup=soup.find()
		#here you can use beatiful
		#http://www.pythonforbeginners.com/python-on-the-web/web-scraping-with-beautifulsoup

	return quotes



