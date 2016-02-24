import warc

class WarcExtracter:
	path = ""
	pages = []

	def setFilePath(self, path):
		self.path = path

	def proccess(self):
		f = warc.open(self.path)
		for record in f:
			warc_type = record['warc-type']
			if(warc_type == "response"):
				payload = self.removeHeader(record.payload)
				self.pages.append(payload)

	def getPages(self):
		return self.pages

	def removeHeader(self, payload):
		page = payload.split("\n\n", 1)
		return page[1]

