import os

def convert(chapter):
	print("Converting " + chapter.inputDirectory)
	# Load Images
	imageNames = []
	for dirPath, dirNames, fileNames in os.walk(chapter.inputDirectory, topdown = True):
		if dirPath != chapter.inputDirectory: break # We're only concerned with the top level contents
		imageNames.extend(fileNames)

	for imageName in imageNames:
		print(os.path.join(chapter.inputDirectory, '') + imageName)



	return
