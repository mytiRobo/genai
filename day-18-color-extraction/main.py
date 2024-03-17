#need debugging
import colorgram

rgb_colors = []
colors = colorgram.extract('day-18-color-extraction\img.png', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(new_color)