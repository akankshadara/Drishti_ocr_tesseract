import PIL
from PIL import ImageFont
from PIL import Image
from PIL import ImageDraw

img=Image.new("RGBA", (800,1200),(256,256,256))

black = Image.open('black.jpg')
white = Image.open('white.jpg')

ar = [0,1,0,1,1,0]

for i in range(0, 6):
	if(ar[i]):
		img.paste(black, ( (i % 2) * 400, int(i / 2) * 400 ) )
	else:
		img.paste(white, ( (i % 2) * 400, int(i / 2) * 400 ) )

img.save('braille.jpg')