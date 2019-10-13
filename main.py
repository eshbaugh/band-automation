#! /usr/bin/python3

import datetime
import os
import glob
import shutil

class autoUtils:
	#######################################################################################
	# getOutputDir()  will compute a directory name based on the current year and date
	# then create the full path including a /source subdirectory at the lowest level 
	#######################################################################################
	def getOutputDir( self ):

		dd = datetime.datetime.today()
		self.outputDir = self.outputBaseDir + dd.strftime( '%Y/%m%d/') 

		if not os.path.exists( self.outputDir ):
			outputSourceDir = self.outputDir + 'source/' 
			print( 'Creating Directory path ', outputSourceDir )
			os.makedirs( outputSourceDir, 777 )
		

	##########################################################################
	#  Move *.wav files from source to destination, creating the destination 
	#  directory if necessary.
	##########################################################################

	def moveWaves( inputDir ):

		files = glob.glob( inputDir )
		print ( files )

		for inFile in files:
			if not inFile.endswith( '.wav') :
				continue
			print( 'Moving ', inFile, ' to ', self.outputDir )
			shutil.move( inFile, self.outputDir )

def main():
	au = autoUtils()
	au.outputBaseDir = '/media/CR/'
	au.getOutputDir()
	au.moveWaves( '/run/media/righttap/Samsung USB/Recordings/*' )

main()