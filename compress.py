import zipfile,zlib,sys,os
#from zipfile import print_info

if len(sys.argv) > 2:
	with zipfile.ZipFile(sys.argv[1], 'w' , zipfile.ZIP_DEFLATED) as zf:
		for file in sys.argv:
			if file == sys.argv[0]:
				continue
			if file == sys.argv[1]:
				continue
			if os.path.isdir(file) :
				for root,dirs,files in os.walk(file):
					for f in files:
						zf.write(os.path.join(root,f))
			else:
				zf.write(file)

	with zipfile.ZipFile(sys.argv[1],'r') as zipf:
		print(zipf.printdir())
else:
	print('Usage {} zipfilename.zip files ... ...'.format(sys.argv[0]))
