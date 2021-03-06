import sys
from PIL import Image
SCALE=[   '.',
    ',',
    ';',
    '!',
    'v',
    '1',
    'L',
    'F',
    'E',
    '$']

def GrayScale(image,im):
    pix=im.load()
    for i in range(im.size[0]):
        for j in range(im.size[1]):
            R=pix[i,j][0]
            G=pix[i,j][1]
            B=pix[i,j][2]
            grayscale=int(0.2126*R + 0.7152*G + 0.0722*B)
            pix[i,j]=(grayscale,grayscale,grayscale)
    im.save(image.split(".")[0]+"_grayscale.jpg")
    return pix

def Ascii(im,pix,scale=1):
    buffer=""
    for i in range(2*scale,im.size[1],4*scale):
        for j in range(scale,im.size[0],2*scale):
            gradient=0
            for k in range(-2*scale,1*scale):
                for l in range(-scale,scale):
                    gradient=gradient+pix[j+l,i+k][0]
            gradient=gradient/(6*scale*scale)
            if(gradient>=0 and gradient<25):
                buffer+=SCALE[0]
            if(gradient>=25 and gradient<50):
                buffer+=SCALE[1]
            if(gradient>=50 and gradient<75):
                buffer+=SCALE[2]
            if(gradient>=75 and gradient<100):
                buffer+=SCALE[3]
            if(gradient>=100 and gradient<125):
                buffer+=SCALE[4]
            if(gradient>=125 and gradient<150):
                buffer+=SCALE[5]
            if(gradient>=150 and gradient<175):
                buffer+=SCALE[6]
            if(gradient>=175 and gradient<200):
                buffer+=SCALE[7]
            if(gradient>=200 and gradient<225):
                buffer+=SCALE[8]
            if(gradient>=225 and gradient<255):
                buffer+=SCALE[9]
        buffer+="\n"
    return buffer

def main():
    image=str(sys.argv[1])
    scale=int(sys.argv[2])
    im=Image.open(image)
    file=open(image.split(".")[0]+".txt","w")
    pix=GrayScale(image,im)

    file.write(Ascii(im,pix,scale))
    file.close()

if __name__ == "__main__":
   main()
