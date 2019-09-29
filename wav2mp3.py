#!/usr/bin/python

import glob
from pydub import AudioSegment

filePath = "/media/CR/2019/Sept27/927/"

wavFilePath = filePath + "*.wav"
files = glob.glob( wavFilePath )

for in_file in files:
    out_file = in_file.replace( ".wav", ".mp3" )
    print( in_file, out_file )


# convert wav to mp3                                                            
sound = AudioSegment.from_wav(in_file)
sound.export(out_file, format="mp3")