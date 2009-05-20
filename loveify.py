import zipfile
import tarfile
import sys

infile = sys.argv[1]
outfile = sys.argv[2]
out = zipfile.ZipFile(outfile, 'w')
if zipfile.is_zipfile(infile):
	arch = zipfile.ZipFile(infile)
	names = arch.namelist()
	def open_file(name):
		return arch.open(name)
else:
	arch = tarfile.open(infile)
	names = arch.getnames()
	def open_file(name):
		return arch.extractfile(name)

for name in names:
	f = open_file(name)
	if f:
		n = name.split('/', 1)[1]
		if n:
			out.writestr(n, f.read())
		f.close()
arch.close()
out.close()