import glob, os

def rename(dir, pattern, titlePattern, count=0):
	"""
	To rename every file in certain folder to make it five digit image.
	// if rename cause duplicate name, how? e.g. 2.jpg, 00000.jpg. rename of 2.jpg will cause replace of another one
	"""
	count = 0
	for pathAndFilename in glob.iglob(os.path.join(dir, pattern)):
		title, ext = os.path.splitext(os.path.basename(pathAndFilename))
		os.rename(pathAndFilename, os.path.join(dir, titlePattern % (count)))
		count += 1
	    

#SAMPLE RUNNING CODE:
dir = "F:\\term7\\CV\\ProjectTrail\\A_manualLabel\\Negative\\Negative"
pattern = r'*.jpg'
titlePattern = r'%05d.jpg'
count = 0
rename(dir, pattern, titlePattern, count=0)
