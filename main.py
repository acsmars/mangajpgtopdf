import argparse
import inputParser
import converter

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Convert JPG Directories into PDFs')
	parser.add_argument('inputDirectory', type=str)
	parser.add_argument('outputDirectory', type=str)
	args = parser.parse_args()

	print("Parsing Input Directory")
	rootCollection = inputParser.Collection(args.inputDirectory, args.inputDirectory, args.outputDirectory)
	jobList = rootCollection.process()

	print("Converting...")
	converter.convert(jobList[0])
