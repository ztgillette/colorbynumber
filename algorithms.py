from colors import *
from collections import Counter

# helper functions

def getNeighborColors(pix, x, y, xdim, ydim):
    #list of neighbor colors
    neighborColors = []

    # corners
    # top left
    if x > 0 and y > 0:
        neighborColors.append(pix[x-1, y-1])
    
    # top right
    if x < xdim-1 and y > 0:
        neighborColors.append(pix[x+1, y-1])

    # bottom left
    if x > 0 and y < ydim-1:
        neighborColors.append(pix[x-1, y+1])

    # bottom right
    if x < xdim-1 and y < ydim-1:
        neighborColors.append(pix[x+1, y+1])

    # edges
    # top
    if(y > 0):
        neighborColors.append(pix[x, y-1])

    # bottom
    if(y < ydim-1):
        neighborColors.append(pix[x, y+1])

    # left
    if(x > 0):
        neighborColors.append(pix[x-1, y])

    # right
    if(x < xdim-1):
        neighborColors.append(pix[x+1, y])

    return neighborColors

    
def getClosestPencilColor(pix, x, y):

    lowestscore = 255*4
    closestcolor = None
    currentscore = 255*4
    for color in COLORS:

        #calculate closeness score
        r, g, b = pix[x, y]
        r2, g2, b2 = color
        currentscore = abs(r-r2) + abs(g-g2) + abs(b-b2)

        #save if score is lower than lowest score
        if currentscore < lowestscore:
            lowestscore = currentscore
            closestcolor = color

    return closestcolor

def clumpPixels(pix_, xdim, ydim, clumpsize, colormode):

    # determine boundries of clump
    xclumps = int(xdim / clumpsize)
    yclumps = int(ydim / clumpsize)

    for w in range(xclumps):
        for h in range(yclumps):

            x = w * clumpsize
            y = h * clumpsize

            l = []
            #append all colors in clump
            for i in range(clumpsize):
                for j in range(clumpsize):
                    c = pix_[x+i,y+j]
                    l.append(c)

            #find most common color
            counter = Counter(l)
            mostPopularColor = counter.most_common(1)
            #print(mostPopularColor)

            # extract r, g, b info
            r = mostPopularColor[0][0][0]
            g = mostPopularColor[0][0][1]
            b = mostPopularColor[0][0][2]

            color = (r, g, b)

            # assign all pixels in clump that color value
            # or make a wall
            for i in range(clumpsize):
                for j in range(clumpsize):
                    if(i == 0 or i == clumpsize-1 or j == 0 or j == clumpsize-1):
                        pix_[x+i,y+j] = ALTBLACK
                    else:
                        if(i==1 and j==1):
                            pix_[x+i,y+j] = color
                        elif colormode == True:
                            pix_[x+i,y+j] = color
                        else:
                            pix_[x+i,y+j] = ALTWHITE
                    

    return pix_

def getNumber(pix, x, y):

    for i in range(len(COLORS)):
        if(pix[x, y] == COLORS[i]):
            return i

    return -1