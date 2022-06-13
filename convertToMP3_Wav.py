# This will convert an mp3 to wav
# src and dst will have to be updated accoringly

from os import path
from pydub import AudioSegment

# file needed is src, the dest is dst
src = "vuela.m4a"
dst = "vuela.wav"

sound = AudioSegment.from_m4a(src)
sound.export(dst, format="wav")

print("hi")
