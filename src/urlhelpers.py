import urllib

def retriveWebContent( address ):
	# Get a file-like object for the Python Web site's home page.
	f = urllib.urlopen(address)
	# Read from the object, storing the page's contents in 's'.
	s = f.read()
	f.close()
	
	return s#.decode('utf8')