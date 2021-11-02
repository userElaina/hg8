
from array2gif import write_gif  # version: 1.0.4
import librosa  # version: 0.8.1
import numpy  # version: 1.19.5

f=open('31.log','w')

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


from PIL import Image



im=Image.open('30/30_127.png')
im.load()

# im = Image.new('RGB', image.size, (255, 255, 255))
# im.paste(image, mask=image.split()[3])
im=numpy.array(im)

# print(ar)
a=[0]*32
ar=list()
for i in range(65):
    ar.append(list())

for _m,i in enumerate(im):
    if _m&1:
        continue
    for _n,j in enumerate(i):
        if _n&3!=3:
            continue
        if j:
            a[_n>>2]+=1
            ar[_n>>2].append(' ')
        else:
            ar[_n>>2].append('#')
    lg(''.join([' ' if j else '#' for _n,j in enumerate(i) if _n&1]))


lg([(i<<1)+min_db for i in a])
for i in ar:
    lg(''.join(i))