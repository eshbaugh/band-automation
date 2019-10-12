#! /usr/bin/python3

##########################################################################
#  Move *.wav files from source to destination, creating the destination 
#  directory if necessary.
##########################################################################

import glob
import os
import datetime
import shutil

inputDir = '/run/media/righttap/Samsung USB/Recordings/*'
outputDir = '/media/CR/'

dd = datetime.datetime.today()
outputDir = outputDir + dd.strftime( '%Y/%m%d') + '/source/'

if not os.path.exists( outputDir ):
    print( 'Creating Directory ', outputDir )
    os.makedirs( outputDir, 777 )

files = glob.glob( inputDir )
print ( files )

for inFile in files:
    if not inFile.endswith( '.wav') :
        continue
    print( inFile )
    print( 'Moving ', inFile, ' to ', outputDir )
    shutil.move( inFile, outputDir )
