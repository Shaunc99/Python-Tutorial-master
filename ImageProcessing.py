from PIL import Image
size= (128,128)
imagePath="c:\\shayan\\images\\ford"
img = Image.open(imagePath+".jpg")
img = img.save(imagePath+".png")
img = img.convert('grey')
img.save(imagePath+"-greyscale.png")
img.thumbnail(size)
img.save(imagePath+"-thumbnail.png")

img.show()