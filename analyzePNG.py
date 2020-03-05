from PIL import Image

#This is a tool used to identify peaks in a mass spectrum which has been converted to .png. After being converted to .png a red line with thickness 1px was drawn along each peak on the spectrum.
#A blue line was then drawn along the X axis at 0.
# This script iterates through each blue pixel, left to right, and checks to see if there are red pixels above it. If there are, it checks to see how high those pixels go.
#Then it outputs these peaks.

blue = (63, 72, 204)
red = (237, 28, 36)


im = Image.open('spectra.png')
pix = im.load()
width, height = im.size
originx = 0
originy = height-1

ionlist = []
xcounter = 0
while xcounter < width-1:
    if pix[xcounter, originy-1] == red:
        ycounter = 1
        while pix[xcounter, originy-ycounter] == red:
            ycounter = ycounter +1
        ionlist.append([xcounter, ycounter])
        #print ("Adding ion at " + str(xcounter) + " " + str(ycounter))
    xcounter = xcounter +1

rel_ab = 100/(height-1)
m_z = (500/(width-1))

fragmentlist = []
fragmentcounter = 1
while fragmentcounter < len(ionlist)-1:
    masscharge = 500 + (float(ionlist[fragmentcounter][0])*m_z)
    relativeabundance = float(ionlist[fragmentcounter][1])*rel_ab
    fragmentlist.append([masscharge, relativeabundance])
    #print ("Fragment " + str(fragmentcounter) + ": " + str(masscharge) + "m/z " + str(relativeabundance)+ "rel. ab")
    fragmentcounter = fragmentcounter +1

for fragment in range(len(fragmentlist)-1):
    print(str(fragmentlist[fragment]))
