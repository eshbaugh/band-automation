#! /usr/bin/python3

import glob
import os
import datetime
import shutil

inputDir = '/run/media/righttap/Samsung USB/Recordings/*'
outputDir = '/media/CR/2019/'

dd = datetime.datetime.today()

outputDir = outputDir + dd.strftime( '%m%d') + '/'

if not os.path.exists( outputDir ):
    os.mkdir( outputDir, 777 )

print( outputDir )

files = glob.glob( inputDir )
print ( files )

for inFile in files:
    if not inFile.endswith( '.wav') :
        continue
    print( inFile )
    print( 'Moving ', inFile, ' to ', outputDir )
    shutil.move( inFile, outputDir )

print( 'here' )
