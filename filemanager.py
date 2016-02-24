import glob, os


def GetFiles(path, extension):
	files = []
	os.chdir(path)
	ext = "*." + extension

	for file in glob.glob(ext):
		files.append(file)

	return files
