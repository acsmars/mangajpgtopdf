import os

class Chapter:
	"""
		A chapter of manga in a folder that should be converted to a single PDF
	"""
	name = "" # Name of this chapter and filename of the output
	inputDirectory = "" # The directory of the course images
	outputDirectory = "" # The generated file location
	def __init__(self, name, inputDirectory, outputDirectory):
		self.name = name
		self.inputDirectory = inputDirectory
		self.outputDirectory = outputDirectory[:-len(name)]
		print("Chapter | " + self.name + "\n\t" + self.inputDirectory + "\n\t" + self.outputDirectory)

class Collection:
	"""
		A collection of many chapters/collections with a name a relative location to the program root directory
		Approximately represents a manga or a volume of manga
	"""
	name = "" # Name of this collection and filename of the output directory
	subCollections = [] # List of collections contained in this collection
	chapters = [] # List of chapters contained in this collection
	inputDirectory = "" # The directory of chapters/collections to be processed
	outputDirectory = "" # The directory for chapter/collection output
	def __init__(self, name, inputDirectory, outputDirectory):
		self.name = name
		self.inputDirectory = inputDirectory
		self.outputDirectory = outputDirectory
		self.subCollections = []
		self.chapters = []
		print("Collection | " + self.name + "\n\t" + self.inputDirectory)
		self.parseSubDir()

	def parseSubDir(self):
		for dirPath, dirNames, fileNames in os.walk(self.inputDirectory, topdown = True):
			if dirPath != self.inputDirectory: break # We're only concerned with the top level contents
			for dirName in dirNames:
				nextInputDir = os.path.join(self.inputDirectory, '') + dirName
				nextOutputDir = os.path.join(self.outputDirectory, '') + dirName
				for subDirPath, subDirNames, subFileNames in os.walk(nextInputDir, topdown = True):
					if subDirPath != nextInputDir: break # We're only concerned with the top level contents
					if len(subDirNames) > 0:
						self.subCollections.append( Collection(dirName, nextInputDir, nextOutputDir) )
					if len(subFileNames) > 0:
						self.chapters.append( Chapter(dirName, nextInputDir, nextOutputDir) )

	def process(self):
		if not os.path.isdir(self.outputDirectory):
			os.mkdir(self.outputDirectory)

		jobList = []

		for collection in self.subCollections:
			jobList.extend(collection.process())

		jobList.extend(self.chapters)

		return jobList

