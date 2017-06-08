import os
from PIL import Image
from reportlab.pdfgen import canvas

def convert(chapter):
	outputFileName = os.path.join(chapter.outputDirectory, '') + chapter.name + '.pdf'
	if os.path.isfile(outputFileName): # PDF already exists
		print(outputFileName + " already exists")
		return
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

	imageFiles = [loadImage(x) for x in fileNames if x]

	# Create Output PDF
	
	newPDF = canvas.Canvas(outputFileName)

	# Create pages from image files and add them to the PDF
	for image in imageFiles:
		newPDF.setPageSize((image.width,image.height))
		newPDF.drawImage(image.filename,0,0)
		newPDF.showPage()

	newPDF.save()
	return


