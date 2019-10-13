#! /usr/bin/python3

import datetime
import os
import glob
import shutil
from wav2mp3 import soundConvert

class autoUtils:

	def __init__( self ):
		# Initialization code goes here
		print( 'In constructor for auto utils')

	#######################################################################################
	# getOutputDir()  will compute a directory name based on the current year and date
	# then create the full path including a /source subdirectory at the lowest level 
	#######################################################################################
	def getOutputDir( self, outputBaseDir ):

		dd = datetime.datetime.today()
		outputDir = outputBaseDir + dd.strftime( '%Y/%m%d/') 

		if not os.path.exists( outputDir ):
			outputSourceDir = outputDir + 'source/' 
			print( 'Creating Directory path ', outputSourceDir )
			os.makedirs( outputSourceDir, 777 )

		return outputDir
		

	##########################################################################
	#  Move *.wav files from source to destination, creating the destination 
	#  directory if necessary.
	##########################################################################
	def moveWaves( self, inputDir, outputDir, copyNoDelete = True ):

		print( inputDir )

		files = glob.glob( inputDir + '*' )
		print( files )

		for inFile in files:
			if not inFile.endswith( '.wav') :
				continue
			if copyNoDelete:
				print( 'Copying ', inFile, ' to ', outputDir )
				shutil.copy( inFile, outputDir )
			else:
				print( 'Moving ', inFile, ' to ', outputDir )
				shutil.move( inFile, outputDir )


def main():
	au = autoUtils()
	outputBaseDir = '/media/CR/'
	inputDir = '/run/media/righttap/Samsung USB/Recordings/' 
	inputDir = '/media/CR/2019/test/'
	outputDir = au.getOutputDir( outputBaseDir )
	au.moveWaves( inputDir, outputDir + 'source/' ) 
	
	sc = soundConvert( outputDir, "JUNK")
	sc.wav2mp3()

# Python 3 style of __name__ == '__main__'
main()