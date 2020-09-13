import zipfile,sys
#from zipfile import print_info

if len(sys.argv) == 2:
	with zipfile.ZipFile(sys.argv[1],'r') as zipf:
		print(zipf.printdir())
		zipf.extractall()
else:
	print('Usage {} zipfilename.zip'.format(sys.argv[0]))
