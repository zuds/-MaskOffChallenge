import pysynth

##########################################################################
# MaskOffChallenge
##########################################################################

#this list iterates through the bridge of the song 3 times 
MaskOff = [
['d',4],['g',4],['f',4],['c',4],['f',4],['c',4],['d',4],['d',4],['a',4],
['f',4],['g',4],['a',4],['g',4],['f',4],['e',4],['d',4],
['d',4],['g',4],['f',4],['c',4],['f',4],['c',4],['d',4],['d',4],['a',4],
['f',4],['g',4],['a',4],['g',4],['f',4],['e',4],['d',4],
['d',4],['g',4],['f',4],['c',4],['f',4],['c',4],['d',4],['d',4],['a',4],
['f',4],['g',4],['a',4],['g',4],['f',4],['e',4],['d',4]
]

if __name__ == "MaskOffChallenge.py":
    print()
    print("Creating Mask Off by Future...")
    print()

    #This turns my list into a .wav file using the function inherited from pysynth
    make_wave(MaskOff, fn = "MaskOff.wav")

