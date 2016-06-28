from backend import *
import sys

b = backend()
b.load_repo("turtle")
#print str(sys.argv)
b.set_current_file_name(str(sys.argv[1]))
a = b.get_diff()
