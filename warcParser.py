import sys
import htmlreader as hr
import test

def main(argv):
	folder_path = argv[0]
	files = ""
	#TODO:: Get files into the folder

	html_page = test.test()
	html_page2 = test.test2()

	reader = hr.HtmlReader()
	
	reader.setHtmlPage(html_page)
	reader.proccess()
	reader.setHtmlPage(html_page2)
	reader.proccess()

	reader.close()


if __name__ == "__main__":
	main(sys.argv[1:])