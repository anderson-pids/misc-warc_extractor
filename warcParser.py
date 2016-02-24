import sys
import htmlreader as hr
import warcextracter as we
import filemanager


def extractContent(reader,page):
	reader.setHtmlPage(page)
	reader.proccess()
	

def extractPages(path):
	extractor = we.WarcExtracter()
	extractor.setFilePath(path)
	extractor.proccess();

	return extractor.getPages()

def main(argv):
	folder_path = argv[0]
	start_files = argv[1]
	pages = []
	#Get files into the folder
	files = filemanager.GetFiles(folder_path, "warc.gz")

	#Get pages from warc.gz
	for path in files:
		pages = extractPages(path)

	#Get content from html pages and write into files
	reader = hr.HtmlReader(start_files)
	for page in pages:
		extractContent(reader,page)
	reader.close()


# argv[0] ==> path_dataset
# argv[1] ==> initial number of file output
if __name__ == "__main__":
	main(sys.argv[1:])