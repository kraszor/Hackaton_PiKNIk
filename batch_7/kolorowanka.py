from PIL import Image
from statistics import mean

image = Image.open('sponge.jpg')

image_data = image.load()
height, width = image.size

for y in range(height):
    for x in range(width):
        r, g, b = image_data[y, x]
        new_r_list = []
        new_g_list = []
        new_b_list = []
        for i in range(0, 4):
            for j in range(0, 4):
                if 0 < y + i < height and 0 < x + i < width:
                    new_r, new_g, new_b = image_data[y + i, x + i]
                    new_r_list.append(new_r)
                    new_g_list.append(new_g)
                    new_b_list.append(new_b)

        if len(new_r_list) != 0 and len(new_g_list) != 0 and len(new_b_list) != 0:
            if (r - 5 > mean(new_r_list) or mean(new_r_list) < r + 5) or (g - 5 > mean(new_g_list) or mean(new_g_list) < g + 5) or (b - 5 > mean(new_b_list) or mean(new_b_list) < b + 5):
                image_data[y, x] = 255, 255, 255
            else:
                image_data[y, x] = 0, 0, 0


image.save('sponge2.jpg')

