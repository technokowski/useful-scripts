# This will convert an mp3 to wav
# src and dst will have to be updated accoringly

import os
from pydub import AudioSegment

# file needed is src, the dest is dst
# src = "vuela.m4a"
# dst = "vuela.wav"

def type_stripper(file):
    new_file = file[:-4]
    return(new_file)

def type_stripper_flac(file):
    new_file = file[:-5]
    return(new_file)

directory = os.getcwd()

for i in os.listdir(directory):
    print(i)
    if i.endswith(".m4a"):
        print(type(i))
        print(i)
        print("this file ends with .m4a")
        sound = AudioSegment.from_file(i, "m4a")
        sound.export(type_stripper(i) + ".wav", format="wav")

    elif i.endswith(".mp3"):
        print(type(i))
        print(i)
        print(f"this file ends with .mp3 and is named {i}")
        sound = AudioSegment.from_file(i, "mp3")
        sound.export(type_stripper(i) + ".wav", format="wav")

    elif i.endswith(".flac"):
        print(f"this file ends with .flac and is named {i}")
        sound = AudioSegment.from_file(i, "flac")
        sound.export(type_stripper_flac(i) + ".wav", format="wav")


# sound = AudioSegment.from_file(src, "m4a")
# sound.export(dst, format="wav")

print("hi")
