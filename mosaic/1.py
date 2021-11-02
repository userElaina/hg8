from generate_mosaic import *


img=Image.open('1.bmp')

ar = np.asarray(img.copy(), dtype='uint8').copy()
for i, j in np.ndindex(7,6):
    x1 = X + i*BOX_SIZE
    x2 = X + (i+1)*BOX_SIZE
    y1 = Y + j*BOX_SIZE
    y2 = Y + (j+1)*BOX_SIZE

    cx=ar[x2-1,y2-1]
    print(x2,y2,cx)

    ox0=x1//PIXEL_SIZE*PIXEL_SIZE
    oy0=y1//PIXEL_SIZE*PIXEL_SIZE
    ox1=ox0+PIXEL_SIZE
    oy1=oy0+PIXEL_SIZE
    ox2=ox1+PIXEL_SIZE
    oy2=oy1+PIXEL_SIZE
    ox3=ox2+PIXEL_SIZE
    oy3=oy2+PIXEL_SIZE

    c00=ar[ox0,oy0]
    ar[ox0:ox1,oy0:oy1]=c00
    c01=ar[ox0,oy1]
    ar[ox0:ox1,oy1:oy2]=c01
    c02=ar[ox0,oy2]
    ar[ox0:ox1,oy2:oy3]=c02
    c10=ar[ox1,oy0]
    ar[ox1:ox2,oy0:oy1]=c10
    c20=ar[ox2,oy0]
    ar[ox2:ox3,oy0:oy1]=c20

    for i in range(16):
        s=bin(i)[2:].zfill(4)
        ar[ox1:ox2,oy1:oy2]=0 if s[-1]=='0' else 0xff
        ar[ox1:ox2,oy2:oy3]=0 if s[-2]=='0' else 0xff
        ar[ox2:ox3,oy1:oy2]=0 if s[-3]=='0' else 0xff
        ar[ox2:ox3,oy2:oy3]=0 if s[-4]=='0' else 0xff
        if math.floor(ar[x1:x2, y1:y2].mean())==cx:
            break


img=Image.fromarray(ar, mode='L')
img.show()
img.save('2.bmp')

# ar = np.asarray(img.copy(), dtype='uint8').copy()
# for i, j in np.ndindex(2,3):
#     x1 = X + (N-1-i)*BOX_SIZE
#     x2 = X + (N-i)*BOX_SIZE
#     y1 = Y + (N-1-j)*BOX_SIZE
#     y2 = Y + (N-j)*BOX_SIZE

#     print(x1-1,y1-1)
#     cx=ar[x1,y1]

#     ox0=x1//PIXEL_SIZE*PIXEL_SIZE
#     oy0=y1//PIXEL_SIZE*PIXEL_SIZE
#     ox1=ox0+PIXEL_SIZE
#     oy1=oy0+PIXEL_SIZE
#     ox2=ox1+PIXEL_SIZE
#     oy2=oy1+PIXEL_SIZE
#     ox3=ox2+PIXEL_SIZE
#     oy3=oy2+PIXEL_SIZE

#     c22=ar[ox3-1,oy3-1]
#     ar[ox2:ox3,oy2:oy3]=c22
#     c21=ar[ox3-1,oy2-1]
#     ar[ox2:ox3,oy1:oy2]=c21
#     c20=ar[ox3-1,oy1-1]
#     ar[ox2:ox3,oy0:oy1]=c20
#     c12=ar[ox2-1,oy3-1]
#     ar[ox1:ox2,oy2:oy3]=c12
#     c02=ar[ox1-1,oy3-1]
#     ar[ox0:ox1,oy2:oy3]=c02

#     for i in range(16):
#         s=bin(i)[2:].zfill(4)
#         ar[ox0:ox1,oy0:oy1]=0 if s[-1]=='0' else 0xff
#         ar[ox1:ox2,oy0:oy1]=0 if s[-2]=='0' else 0xff
#         ar[ox0:ox1,oy1:oy2]=0 if s[-3]=='0' else 0xff
#         ar[ox1:ox2,oy1:oy2]=0 if s[-4]=='0' else 0xff
#         if math.floor(ar[x1:x2, y1:y2].mean())==cx:
#             break

# img=Image.fromarray(ar, mode='L')
# img.show()
# img.save('3.bmp')
