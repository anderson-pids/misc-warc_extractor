from bs4 import BeautifulSoup

class HtmlReader:
	document_id = 0
	file_id = 0
	page = ""
	document = ""
	docs_per_file = 1000

	def __init__(self, file_id):
		self.file_id = int(file_id)
		self.file_out = open(str(self.file_id),'w')

	def setHtmlPage(self, htmlPage):
		self.page = htmlPage

	def proccess(self):
		soup = BeautifulSoup(self.page)

		# kill all script and style elements
		for script in soup(["script", "style"]):
		    script.extract()    # rip it out
		# get text
		text = soup.get_text()
		# break into lines and remove leading and trailing space on each
		lines = (line.strip() for line in text.splitlines())
		# break multi-headlines into a line each
		chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
		# drop blank lines
		text = ' '.join(chunk for chunk in chunks if chunk)

		self.writeDocument(text)

	def writeDocument(self, doc):		
		if(self.document_id < self.docs_per_file):
			text = ("[" + str(self.file_id) + "]_" + str(self.document_id) + " #\t" + doc + "\n").encode('utf-8')
			self.file_out.write(text)
			self.document_id = self.document_id + 1
		else:
			self.file_out.close()
			print "Created file: ", str(self.file_id)
			self.file_id = self.file_id + 1
			self.file_out = open(str(self.file_id),'w')

			self.document_id = 0
			text = ("[" + str(self.file_id) + "]_" + str(self.document_id) + " #\t" + doc + "\n").encode('utf-8')
			self.file_out.write(text)
			self.document_id = self.document_id + 1

	def close(self):
		self.file_out.close()
		print "Created file: ", str(self.file_id)

			
