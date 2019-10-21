#! /usr/bin/python3

import datetime
import os
import glob
import shutil
from soundFileConversion import soundConvert

class autoUtils:

	def __init__( self ):
		# Initialization code goes here
		print( 'In constructor for auto utils')

	#######################################################################################
	# createDateCodedOutputDirectory()  will compute a directory name based on the current year and date
	# then create the full path including a /source subdirectory at the lowest level 
	#######################################################################################
	def createDateCodedOutputDirectory( self, outputBaseDir ):

		dd = datetime.datetime.today()
		outputDir = outputBaseDir + dd.strftime( '%Y/%m%d/') 

		if not os.path.exists( outputDir ):
			outputSourceDir = outputDir + 'source/' 
			print( 'Creating Directory path ', outputSourceDir )
			os.makedirs( outputSourceDir, mode=0o777, exist_ok=True ) # 0o specificies Octal Numbering System

			# Makedirs crates the least dignificat directory(source in this case) with permission 
			# dr----x--t. 2 jerry jerry 4.0K Oct 14 20:33 source
			#os.chmod( outputDir, 0777, )

		return outputDir
		

	##########################################################################
	#  Move *.wav files from source to destination, creating the destination 
	#  directory if necessary.
	##########################################################################
	def moveFiles( self, inputDir, outputDir, extension = '.wav', copyNoDelete = False ):

		print( inputDir )

		files = glob.glob( inputDir + '*' )
		print( files )

		for inFile in files:
			if not inFile.endswith( extension ) :
				continue
			if copyNoDelete:
				print( 'Copying ', inFile, ' to ', outputDir )
				shutil.copy( inFile, outputDir )
			else:
				print( 'Moving ', inFile, ' to ', outputDir )
				shutil.move( inFile, outputDir )

	def printFiles( self, inPath ):
		for path, dirs, files in os.walk( inPath ):
			for ff in files:
				fullFilename = path + '/' + ff
				print( fullFilename ) 

	def printFiles( self, inPath ):
		for path, dirs, files in os.walk( inPath ):
			for ff in files:
				fullFilename = path + '/' + ff
				print( fullFilename ) 


def uploadWavOutputMP3():
	outputBaseDir = '/media/CR/'
	inputDir = '/run/media/righttap/Samsung USB/Recordings/' 

	au = autoUtils()
	outputDir = au.createDateCodedOutputDirectory( outputBaseDir )
	sourceDir = outputDir + 'source/'
	au.moveFiles( inputDir, sourceDir, '.wav' ) 
	
	sc = soundConvert( )
	sc.wav2mp3( sourceDir, outputDir )


def testWavToMP3():
	outputBaseDir = './tests/testOutput/' 
	inputDir = './tests/wavs/'

	au = autoUtils()

	if os.path.exists( outputBaseDir ):
		shutil.rmtree( outputBaseDir )

	print( "----------------- Initial Directory --------------")
	au.printFiles( './tests/' )

	outputDir = au.createDateCodedOutputDirectory( outputBaseDir )
	sourceDir = outputDir + 'source/'

	au.moveFiles( inputDir, sourceDir, '.wav', True ) 

	sc = soundConvert( )
	sc.wavToMP3( sourceDir, outputDir, 200 )

	print( "----------------- postConversion Directory --------------")
	au.printFiles( './tests/' )

def testMP3ToWav():
	outputBaseDir = './tests/testOutput/' 
	inputDir = './tests/mp3s/'

	au = autoUtils()

	if os.path.exists( outputBaseDir ):
		shutil.rmtree( outputBaseDir )

	print( "----------------- Initial Directory --------------")
	au.printFiles( './tests/' )

	outputDir = au.createDateCodedOutputDirectory( outputBaseDir )
	sourceDir = outputDir + 'source/'

	au.moveFiles( inputDir, sourceDir, '.mp3', True ) 

	sc = soundConvert( )
	sc.MP3ToWav( sourceDir, outputDir )

	print( "----------------- postConversion Directory --------------")
	au.printFiles( './tests/' )

def main():
#	testWavToMP3()

	testMP3ToWav()
#	uploadWavOutputMP3()

# Python 3 style of __name__ == '__main__'
main()
