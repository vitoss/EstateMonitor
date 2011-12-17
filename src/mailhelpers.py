import smtplib

def sendEmail( fromaddr, toaddrs, subject, msg ):
	# Credentials (if needed)
	username = 'wwdaemon'
	password = 'p3r!od0nog'
	
	#preparing content
	content = u"Subject: " + subject + "\r\n" 
	content += u"From: Uniżony Sługa Gniot<wwdaemon@gmail.com>\r\n"
	content += u"To:"+toaddrs+"\r\n\r\n"
	content += msg
	content = content.encode('utf8')
	
	
	# The actual mail send
	server = smtplib.SMTP('smtp.gmail.com:587')
	server.starttls()
	server.login(username,password)
	server.sendmail(fromaddr, toaddrs, content)
	server.quit()