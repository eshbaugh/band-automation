#!/usr/bin/python3

import glob
#from pydub import AudioSegment
import pydub

filePath = '/media/CR/2019/Sept27/927/'
minTrackLength = 150 # seconds (2.5 min)

wavFilePath = filePath + '*'
files = glob.glob( wavFilePath )

for in_file in files:
    if not in_file.endswith( '.wav') :
        continue

    out_file = in_file.replace( '.wav', '.mp3' )

    # convert wav to mp3                                                            
    sound = pydub.AudioSegment.from_wav(in_file)
    trackLength = len(sound)/1000
    if  trackLength < minTrackLength:
        print( 'Skipping file:', in_file, ' Track Length ', trackLength, ' is less than minium track length ', minTrackLength ) 
        continue

    print( 'Creating:', out_file, ' audio track length:', len(sound)/1000 , ' (sec)' )

    sound.export(out_file, format='mp3')