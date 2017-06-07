import os
from PIL import Image
from PyPDF2 import PdfFileWriter

def convert(chapter):
	print("Converting " + chapter.inputDirectory)
	# Load Images
	imageNames = []
	for dirPath, dirNames, fileNames in os.walk(chapter.inputDirectory, topdown = True):
		if dirPath != chapter.inputDirectory: break # We're only concerned with the top level contents
		imageNames.extend(fileNames)

	if len(imageNames) < 1: # How did this happen?
		print("Error: Empty Chapter " + chapter.inputDirectory)
		return

	def loadImage(imageName):
		fileName, extension = os.path.splitext(imageName)
		image = None
		if extension.lower() == '.jpg':
			try:
				imageLocation = os.path.join(chapter.inputDirectory, '') + imageName
				image = Image.open(imageLocation)
			except Exception as e:
				print("Error opening image: " + imageLocation)
				print(e)
		else:
			print(extension.lower())
		return image

	imageFiles = [loadImage(x) for x in fileNames]

	# Create Output PDF
	newPDF = PdfFileWriter()

	# Create pages from image files and add them to the PDF
	for image in imageFiles:
		newPage = newPDF.addBlankPage(width = image.width, height = image.height)
		print(newPage.artBox)

	outputFileName = os.path.join(chapter.outputDirectory, '') + chapter.name
	outputFile = open(outputFileName, "wb")
	newPDF.write(outputFile)

	return


