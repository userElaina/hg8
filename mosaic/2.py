from generate_mosaic import *


img=Image.open('1.bmp')


for lp in range(10):
    ar = np.asarray(img.copy(), dtype='uint8').copy()
    for i, j in np.ndindex(N,N):
        # print('iijj:',i,j)
        x1 = X + i*BOX_SIZE
        x2 = X + (i+1)*BOX_SIZE
        y1 = Y + j*BOX_SIZE
        y2 = Y + (j+1)*BOX_SIZE
        # print(x1,'-',x2,',',y1,'-',y2)
        

        ox0=x1//PIXEL_SIZE*PIXEL_SIZE
        oy0=y1//PIXEL_SIZE*PIXEL_SIZE
        ox1=ox0+PIXEL_SIZE
        oy1=oy0+PIXEL_SIZE
        ox2=ox1+PIXEL_SIZE
        oy2=oy1+PIXEL_SIZE
        ox3=ox2+PIXEL_SIZE
        oy3=oy2+PIXEL_SIZE

        lx=[ox0,ox0,ox0,ox1,ox1,ox1,ox2,ox2,ox2,]
        ly=[oy0,oy1,oy2,oy0,oy1,oy2,oy0,oy1,oy2,]
        w=9
        i=0
        cx=None
        while i<w:
            flg=False
            llx=[lx[i],lx[i],lx[i]+PIXEL_SIZE-1,lx[i]+PIXEL_SIZE-1]
            lly=[ly[i],ly[i]+PIXEL_SIZE-1,ly[i],ly[i]+PIXEL_SIZE-1]
            for j in range(len(llx)):
                c=ar[llx[j],lly[j]]
                # print(llx[j],lly[j],c)
                if c in (0,0xff):
                    ar[lx[i]:lx[i]+PIXEL_SIZE,ly[i]:ly[i]+PIXEL_SIZE]=c
                    flg=True
                else:
                    if (x1<=llx[j]<x2) & (y1<=lly[j]<y2):
                        # print('c:',c,end=',')
                        cx=c
            if flg:
                lx=lx[:i]+lx[i+1:]
                ly=ly[:i]+ly[i+1:]
                w-=1
            else:
                i+=1
        # print()

        if cx is None:
            print('win')
            continue
        # print(x1,y1)
        # print(lx,ly)
        ans=list()
        for i in range(1<<w):
            s=bin(i)[2:].zfill(w)
            for j in range(w):
                ar[max(x1,lx[j]):min(x2,lx[j]+PIXEL_SIZE),max(y1,ly[j]):min(y2,ly[j]+PIXEL_SIZE)]=0 if s[j]=='0' else 0xff
            # print(math.floor(ar[x1:x2, y1:y2].mean()))
            if math.floor(ar[x1:x2, y1:y2].mean())==cx:
                ans.append(i)

        # print(ans,cx)
        if len(ans)!=1 and lp<3:
            for j in range(w):
                ar[max(x1,lx[j]):min(x2,lx[j]+PIXEL_SIZE),max(y1,ly[j]):min(y2,ly[j]+PIXEL_SIZE)]=cx
        else:
            s=bin(ans[0])[2:].zfill(w)
            for j in range(w):
                ar[lx[j]:lx[j]+PIXEL_SIZE,ly[j]:ly[j]+PIXEL_SIZE]=0 if s[j]=='0' else 0xff

        # img=Image.fromarray(ar, mode='L')
        # img.show()
        # exit()

    img=Image.fromarray(ar, mode='L')
    img.show()
    img.save('2_'+str(lp)+'.bmp')
