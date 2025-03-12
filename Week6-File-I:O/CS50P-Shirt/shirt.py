import os
from sys import argv
import PIL
from PIL import Image, ImageOps

def merge(im1, im2):
    w = 600
    h = 600
    im = Image.new("RGBA", (w, h))

    im.paste(im1)
    im.paste(im2)

    return im



if len(argv) <= 2:
    print("Too few command-line arguments")
    exit(1)
elif len(argv) > 3:
    print("Too many command-line arguments")
    exit(1)
else:
    infile = argv[1].split(".")
    outfile = argv[2].split(".")
    if (infile[1] in ["jpg", "jpeg", "png"]) and infile[1] == outfile[1]:
        shirt = Image.open("shirt.png")
        try:
            with Image.open(argv[1]) as im:
                sqImg = ImageOps.fit(im, shirt.size)
                sqImg.paste(shirt, shirt)
                sqImg.save(argv[2])
        except FileNotFoundError:
            print("notFound")
            exit(1)
        except PIL.UnidentifiedImageError:
            print("Wrong image")
            exit(1)
        except ValueError:
            print("value")
            exit(1)
        except TypeError:
            print(type)
            exit(1)
        except OSError:
            print("Os")
    else:
        print("exit")
        exit(1)

#shirt (600,600)
#before1
#before2 (1200, 1600)