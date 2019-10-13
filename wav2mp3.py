#!/usr/bin/python3

import glob
from pydub import AudioSegment
from pydub import effects

class soundConvert:
    def __init__( self, inDir, outDir ):
        self.inDir = inDir
        self.outDir = outDir
        self.minTrackLength = 150 # seconds (2.5 min)

    def wav2mp3( self ):
        wavFilePath = self.inDir + '*'
        files = glob.glob( wavFilePath )

        for in_file in files:
            if not in_file.endswith( '.wav') :
                continue

            # TODO Use output Directory as opposed to keeping all created files in the input directory
            out_file = in_file.replace( '.wav', '.mp3' )

            # convert wav to mp3                                                            
            print( 'Computing track length for file:', in_file)
            sound = AudioSegment.from_wav(in_file)
            trackLength = len(sound)/1000
            if  trackLength < self.minTrackLength:
                print( 'Skipping mp3 conversion for file:', in_file, ' Track Length ', trackLength, '(sec) is less than minium track length ', self.minTrackLength, '(sec)' ) 
                continue

            print( 'Creating:', out_file, ' audio track length:', trackLength , '(sec)' )

            goodVolumeSound = effects.normalize( sound )
            goodVolumeSound.export(out_file, format='mp3')