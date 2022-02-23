from PIL import Image, ImageFilter

img = Image.open('./pokedex/pikachu.jpg')
filtered_img = img.filter(ImageFilter.CONTOUR)
convert_img = img.convert('L')
convert_img.save('pikachu_convert.jpg')
convert_img.show()
filtered_img.save('pikachu_contour.jpg')

# print(img.format, img.size, img.mode)
# print(dir(img))/// 