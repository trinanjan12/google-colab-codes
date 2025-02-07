'''
    This code explains how to mount google drive in google colab session
    After mounting we can read data from the google drive directly and use it in the colab session
'''

# Load the Drive helper and mount
from google.colab import drive

# This will prompt for authorization.
drive.mount('/content/drive')

# After executing the cell above, Drive
# files will be present in "/content/drive/My Drive".

# This will show the files of your current drive,upload your data file like csv,txt in the root dir(home page) of your google drive
!ls "/content/drive/My Drive"

# To go to the google drive root dir
cd /content/drive/My Drive

# Now you can read your file from the current dir
# I had uploaded my txt file in my drive and now i can read that file

def load_doc(filename):
	# open the file as read only
	file = open(filename, 'r')
	# read all text
	text = file.read()
	# close the file
	file.close()
	return text

# load document
in_filename = 'republic_sequences.txt'
doc = load_doc(in_filename)
