#!/usr/bin/python3

import glob
#from pydub import AudioSegment
import pydub

filePath = '/media/CR/2019/Test/'
filePath = '/media/CR/2019/Sept27/927/'

wavFilePath = filePath + '*'
files = glob.glob( wavFilePath )
print( 'Processing files:', files )

for in_file in files:
    if not in_file.endswith( '.wav') :
        continue

    out_file = in_file.replace( '.wav', '.mp3' )
    print( 'Using file:', in_file, '  to create file:', out_file )

    # convert wav to mp3                                                            
    sound = pydub.AudioSegment.from_wav(in_file)
    sound.export(out_file, format='mp3')
