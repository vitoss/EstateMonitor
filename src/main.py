from urlhelpers import *
from htmlhelpers import *
from mailhelpers import * 
import shelve
import hashlib

# Our function to get the MD5 hash of a string
def getMD5Hash(textToHash=None):
    return hashlib.md5(textToHash).hexdigest()

#TODO - py.config
gumtreeAdress = "http://krakow.gumtree.pl/f-Nieruchomosci-dom-mieszkanie-wynajme-Mieszkanie-2-pokoje-1-lazienka-W0QQAQ5fDwellingTypeZflatQQAQ5fNumberBathroomsZ10QQAQ5fNumberRoomsZ2QQCatIdZ9008QQmaxPriceZ1Q20300QQminPriceZ900"
szybkoAddress = "http://szybko.pl/index.php?nav1=search&search_mode=full&area=&action=search&type=rent&heading=yes&footer=yes&db=&keywords_desc=true&cities=krak%F3w&suburbs=&area_min=29&area_max=50&estate_type%5B%5D=0&area=0&street=&rooms_count=2&price_min=900&price_max=1300&startdate=-1&keywords=&free_number="

sites = [ { "address": gumtreeAdress, "linkSelector" : ".resultsTableSB .hgk a" }, 
		  { "address": szybkoAddress, "linkSelector" : ".listUNIT .div2 a.nagl" } 
		  ]
		  
rawkeywords = [ u"stoigniewa", u"heltmana", u"pańska", u"wola duchacka", 
				u"bonark", u"plaszów", u"kurdwan", u"siemomysła", u"gipsowa", 
				u"dworcow", u"wielick",  u"piaski nowe"]
				
encodeWithUtf = lambda key : key.encode('utf8')
keywords = map(encodeWithUtf, rawkeywords)

receivers = ["vitotao@gmail.com", "kicia.panterka@gmail.com"]

dbFilename = "readedAds.dat"
db = shelve.open(dbFilename)

matchedSites = []

for site in sites:
	content = retriveWebContent(site["address"])
	hrefs = getLinkHrefs( content, site["linkSelector"] )
	
	#travers through all pages and search for keywords
	
	for href in hrefs:
		content = retriveWebContent( href.encode('utf8') )
		
		if hasAnyKeywords( content, keywords ) == True:
			hashedKey = getMD5Hash(href.encode('utf8'))
			if not db.has_key(hashedKey):
				matchedSites.append( href )
				db[hashedKey] = "done"

#sending email
if len(matchedSites) > 0:
	for receiver in receivers:
		sendEmail( "wwdaemon@gmail.com", receiver, "Raport mieszkaniowy", 
				u"Odpowiedzi na slowa kluczowe:" + u", ".join(rawkeywords) + u"\r\n\r\n" + 
				u"\r\n".join(matchedSites) )
				
#cleaning up
db.close()