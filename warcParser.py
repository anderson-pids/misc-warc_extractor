import sys
import htmlreader as hr
import test
import filemanager

def main(argv):
	folder_path = argv[0]

	#TODO:: Get files into the folder
	files = filemanager.GetFiles(folder_path, "warc.gz")
	print files;
	#TODO:: Get pages from warc.gz

	exit(0)
	#TODO:: Extract content from html pages and write into the file
	html_page = test.test()
	html_page2 = test.test2()

	reader = hr.HtmlReader()
	
	# for to add html pages
	reader.setHtmlPage(html_page)
	reader.proccess()
	reader.setHtmlPage(html_page2)
	reader.proccess()

	reader.close()


if __name__ == "__main__":
	main(sys.argv[1:])