# import statements
from PIL import Image, ImageOps, ImageFont, ImageDraw
from algorithms import *
import time

#constants
# TRUE means output
# will be in color
COLORMODE = False

# path of the image
IMAGEPATH = 'apple.jpeg'

# size of clumps
# smaller CLUMPSIZE
# means more squares 
# and smaller fonts
CLUMPSIZE = 8

# start time
start = time.time()

# load image
img = Image.open(IMAGEPATH)
# flip to correct orientation
img = ImageOps.exif_transpose(img)

# determine image dimensions 
xdim, ydim = img.size

# get pixels in image
pix = img.load()

# loop through all pixels and edit colors to 
# match standard colored pencil set colors
# ~1 minute for large image
for x in range(xdim):
    for y in range(ydim):
        pix[x,y] = getClosestPencilColor(pix, x, y)
#print("Converted to pencil colors.")
#print("after", str(time.time()-start), "seconds")

#clump colors
pix = clumpPixels(pix, xdim, ydim, CLUMPSIZE, COLORMODE)
#print("Clumped colors.")

#crop out excess
xexcess = xdim % CLUMPSIZE
yexcess = ydim % CLUMPSIZE

realxdim = xdim - xexcess
realydim = ydim - yexcess

img = img.crop((0, 0, realxdim, realydim))

#add corresponding numbers
fontsize = int(CLUMPSIZE * 0.8)
I1 = ImageDraw.Draw(img)
myFont = ImageFont.truetype('font.ttf', fontsize)
xclumps = int(xdim / CLUMPSIZE)
yclumps = int(ydim / CLUMPSIZE)
for w in range(xclumps):
    for h in range(yclumps):
        x = w * CLUMPSIZE + 1
        y = h * CLUMPSIZE + 1
        num = str(getNumber(pix, x, y))
        if(len(num) == 1):
            num = "0" + num
        I1.text((x, y), num, fill=ALTBLACK, font=myFont)
#print("Added numbers.")

outputstring = "OUTPUT" + str(IMAGEPATH)
img.save(outputstring)

end = time.time()
t = end - start

print("Runtime:", t, "seconds")
