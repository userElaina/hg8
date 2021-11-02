#!/usr/bin/env python3

from array2gif import write_gif  # version: 1.0.4
import librosa  # version: 0.8.1
import numpy  # version: 1.19.5

f=open('flag.log','w')

def lg(*args):
    s=' '.join([str(i) for i in args])
    f.write(s+'\n')
    return s

def pt(*args):
    s=lg(*args)
    print(s)
    return s

num_freqs = 32
quantize = 2
min_db = -60
max_db = 30
fft_window_size = 2048
frame_step_size = 512
window_function_type = 'hann'
red_pixel = [255, 0, 0]
white_pixel = [255, 255, 255]
sample_rate = 22050


import os
from PIL import Image, ImageSequence

pth='flag.gif'
dirname=pth.split('.')[0]
os.makedirs(dirname,exist_ok=True)


im = Image.open(pth)


_i=0
spectrogram=list()
for frame in ImageSequence.Iterator(im):

    im=numpy.array(frame)
    a=[0]*32

    for _m,i in enumerate(im):
        if _m&1:
            continue
        for _n,j in enumerate(i):
            if _n&3!=3:
                continue
            a[_n>>2]+=j

    spectrogram.append([float((i<<1)+min_db) for i in a])
    # lg(str(_i).zfill(3),[(i<<1)+min_db for i in a])
    _i+=1

spectrogram=numpy.array(spectrogram).transpose()

_l=[i for i in spectrogram.transpose()]
pt(len(spectrogram),len(_l),type(spectrogram))
_n=120
for i in _l[120:140]:
    lg(str(_n).zfill(3),[int(j) for j in i])
    _n+=1
lg()

_s=librosa.db_to_power(spectrogram)

pt(len(_s),len(_l),type(_s))
_l=[i for i in _s.transpose()]
_n=120
for i in _l[120:140]:
    lg(str(_n).zfill(3),[int(j) for j in i])
    _n+=1
lg()

y=librosa.feature.inverse.mel_to_audio(
    _s,
    sample_rate,
    # n_mels=num_freqs,               # 32        number of mel bins
    n_fft=fft_window_size,          # 2048      FFT window size
    hop_length=frame_step_size,     # 512       hop size
    window=window_function_type     # 'hann'    window function
)
import soundfile
soundfile.write('flag.wav',y,sample_rate)

flag{634971243582}