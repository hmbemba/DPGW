from colour import Color


class MyColor:
    def get(colorname, alpha = 255):
        vals = [value*255 for value in Color(colorname).rgb]
        vals.append(alpha)
        return vals

if __name__ == "__main__":
    ...