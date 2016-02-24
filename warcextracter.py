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
				self.pages.append(record.payload)

	def getPages():
		return self.pages

