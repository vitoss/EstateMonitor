from lib.BeautifulSoup.BeautifulSoup import BeautifulSoup 
from lib.soupselect import select

def getLinkHrefs( content, selector ):
	soup = BeautifulSoup(content)
	getHrefFromLink = lambda link : link["href"]
	links = select( soup, selector )
	return map( getHrefFromLink, links )
	
def hasAnyKeywords( content, keywords ):
	content = content.lower()
	
	for keyword in keywords:
		if hasKeyword( content, keyword ) == True:
			return True

def hasKeyword( content, keyword ):
	if content.find( keyword ) != -1:
		return True
	else:
		return False
		
def makeHtmlLinkPage( hrefs ):
	content = u"<html><head><title>Oferty mieszkań</title></head><body>Oferty: <ul>"
	for href in hrefs:
		content += u"<li><a href=\""+href+u"\">"+href+u"</a></li>";
	
	content += u"</ul></body></html>";
	
	return content.encode('utf8')
		