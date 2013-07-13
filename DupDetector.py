"""
Detect duplicate files using MD5
"""

import argparse, os, pdb, hashlib

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("source", help = "Source folder")
	parser.add_argument("destination", help = "Destination")
	parser.add_argument("--ignore-name", dest = "ignoreName", action="store_true", help="cross check between files with different names")
	parser.add_argument("-d", "--delete", action="store_true", help="delete duplicate files")
	args = parser.parse_args()
	
	pdb.set_trace()
	
	fileList = {}
	
	for root, _, files in os.walk(args.source):
		for file in files:
			pdb.set_trace()
			h = hashlib.sha1()
			filePath = os.path.join(root, file)
			with open(filePath, "rb") as input:
				for chunk in iter(lambda: input.read(128 * h.block_size), b''):
					h.update(chunk)
			fileList[file] = h.digest()
	
	dupList = []
	
	for root, _, files in os.walk(args.destination):
		for file in files:
			if not args.ignoreName or not file in fileList:
				continue	#skip file with different names
			filePath = os.path.join(root, file)
			with open(filePath, "rb") as input:
				for chunk in iter(lambda: input.read(128 * h.block_size), b''):
					h.update(chunk)
			pdb.set_trace()
			if fileList[file] == h.digest():
				print "%s duplicate" % (filePath)
				dupList.append(file)
	
if __name__ == "__main__":
	main()