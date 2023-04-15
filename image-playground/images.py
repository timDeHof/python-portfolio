from PIL import Image, ImageFilter

img = Image.open("./Pokedex/bulbasaur.jpg")
filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save("blur-Bublasaur.png", "png")