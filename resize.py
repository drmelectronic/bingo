from PIL import Image

base = 'geometrydash'
for i in range(100):
    image = Image.open(f'{base}/800/{i + 1}.png')
    new_image = image.resize((100, 100))
    new_image.save(f'{base}/100/{i + 1}.png')