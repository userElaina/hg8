

ans=[127,  98, 128, 120, 232, 117, 161,  82,  41, 141, 137, 137,  54, 109,  93,   9,  44,  57,  86, 153, 197,  16, 123, 252, 144,  71, 104, 156, 178, 116, 243,  99, 208, 183, 215, 139, 198, 245, 136,  38,  50, 254, 254, 109, 200, 240, 175, 155, 160,  54,  51,  36, 136, 153, 207, 233, 112, 207,   7,   0,  99, 181, 100,  91, 185, 225,  25,  47,  29, 219, 155, 140,  92, 182,   8, 210, 133,   5,  51, 229, 241, 144,  47,   7,   8, 177, 187,  46,  81, 178, 122, 255, 120, 183, 230,  95, 191, 210, 167, 160, 169, 200, 229, 236, 104, 238,   8, 228, 239,   2,  23, 221, 192, 105, 219, 162,  30,  11, 194, 187, 235, 102, 161,  31, 191, 130, 184, 130,  43, 147, 126, 216, 121, 126, 145,  97, 222, 135, 132, 150, 206,  42, 219,  38]

import win32gui as wg
import win32con as wc
import win32api as wa
import pyautogui as pag

import ctypes
import keyboard
from time import sleep as slp

def get_color(d:tuple,lu:tuple=(0,0))->int:
	pixel=ctypes.windll.gdi32.GetPixel(ctypes.windll.user32.GetDC(None),d[0]+lu[0],d[1]+lu[1])
	return int(pixel)

def ptinfo(pos:tuple):
	p=get_color(pos)
	print(pos,hex(p),end='   ')

def get_pos():
	l=list()
	while True:
		slp(1)
		l.append(list(wg.GetCursorPos()))
		for i in l[-3:]:
			ptinfo(i)
		print()

'''
get_pos()
[837, 1158] 0xf09729   [2814, 819] 0xf09729   [1671, 509] 0xf09729   
[2814, 819] 0xf09729   [1671, 509] 0xf09729   [1380, 605] 0x25cf9c   
[1671, 509] 0xf09729   [1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   
[1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   
[1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   
[1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   
[1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   
[1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   
[1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   
[1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   [1380, 605] 0x25cf9c   
[1380, 605] 0x24cd9a   [1380, 605] 0x24cd9a   [2927, 1859] 0xf09729   
[1380, 605] 0x24cd9a   [2927, 1859] 0xf09729   [2460, 1661] 0x141414   
[2927, 1859] 0xf09729   [2460, 1661] 0x141414   [2460, 1661] 0x141414   
[2460, 1661] 0x141414   [2460, 1661] 0x141414   [2460, 1661] 0x141414   
[2460, 1661] 0x141414   [2460, 1661] 0x141414   [2460, 1661] 0x141414   
[2460, 1661] 0x141414   [2460, 1661] 0x141414   [2460, 1661] 0x141414   
[2460, 1661] 0x141414   [2460, 1661] 0x141414   [2460, 1661] 0x141414   
[2460, 1661] 0x141414   [2460, 1661] 0x141414   [2460, 1661] 0x141414   
[2460, 1661] 0x141414   [2460, 1661] 0x141414   [2460, 1661] 0x141414   
[2460, 1661] 0x141414   [2460, 1661] 0x141414   [2460, 1661] 0x141414   
[2460, 1661] 0x1e1e1e   [2460, 1661] 0x1e1e1e   [2460, 1661] 0x1e1e1e   

'''

x0,y0=1380, 605
x11,y11=2460, 1661

xx=list()
yy=list()

for i in range(12):
    xx.append(x0+int(i*(x11-x0)/11))
    yy.append(y0+int(i*(y11-y0)/11))

# print(xx,yy)

sl=lambda :slp(0.01)

def mv(x,y,n):
    print(x,y)
    ctypes.windll.user32.SetCursorPos(x,y)
    sl()
    f(n)
    sl()

def f(n:int=1):
    for i in range(n):
        wa.mouse_event(wc.MOUSEEVENTF_LEFTDOWN|wc.MOUSEEVENTF_LEFTUP,0,0)
        sl()


slp(2)
for i in range(12):
    for j in range(12):
        mv(xx[j],yy[i],ans[i*12+j])
        # mv(xx[j],yy[i],0)
        # print(ans[i*12+j])
        slp(1)
