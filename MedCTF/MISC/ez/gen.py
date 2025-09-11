from PIL import Image, ImageDraw, ImageFont
img = Image.new("RGB", (300, 200), color="black")
draw = ImageDraw.Draw(img)
font = ImageFont.load_default(size=20)

# real flag MED{Imag3_magIc_Is_r3Ally_Aw3s0m3!}

draw.text((100, 80), "MED{Imag3_magIc_Is_r3Ally_Aw3s0m3!}", font=font, fill="white")
img = img.rotate(180)

img.save("flag.png")