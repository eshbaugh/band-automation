#!/usr/bin/python3

import glob
from pydub import AudioSegment
from pydub import effects
import os

class soundConvert:
    def __init__( self ):
        print( "Sound convert class initialization method")

    ##########################################
    # wav to mp3 coversion
    #   input Directory
    #   output Directoy 
    #   minimum track legnth to convert  (in seconds)
    ##########################################

    def wav2mp3( self, inDir, outDir, minTrackLength = 150 ):
        wavFilePath = inDir + '*'
        files = glob.glob( wavFilePath )

        for inFile in files:
            if not inFile.endswith( '.wav') :
                continue

            filename = os.path.basename( inFile )
            outFile = outDir + filename.replace( '.wav', '.mp3' )

            # convert wav to mp3                                                            
            print( 'Computing track length for file:', inFile)
            sound = AudioSegment.from_wav(inFile)
            trackLength = len(sound)/1000
            if  trackLength < minTrackLength:
                print( 'Skipping mp3 conversion for file:', inFile, ' Track Length ', trackLength, '(sec) is less than minium track length ', minTrackLength, '(sec)' ) 
                continue

            print( 'Creating:', outFile, ' audio track length:', trackLength , '(sec)' )

            goodVolumeSound = effects.normalize( sound )
            goodVolumeSound.export(outFile, format='mp3')