# Image Resizer

Works only with Python 3.6 or older.

Image resize could be used in two ways: resize image by scale (what means if
 old image was 100x200 and scale is 2, new would be 200x400, scale might be
 less then 1) or resize it by definition (make image with size of user's input)

```bash
$ python3 image_resize.py --help
usage: image_resize.py [-h] [-o OUTPUT] path_to_image {scale,define} ...

positional arguments:
  path_to_image         File path to image you want to resize.
  {scale,define}        choose the way how you want to change an image
    scale               change image by scale
    define              define width and/or height

optional arguments:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        File path where you want to store changed image.
$ python3 image_resize.py define -h
usage: image_resize.py path_to_image define [-h] [-w WIDTH] [-he HEIGHT]

optional arguments:
  -h, --help            show this help message and exit
  -w WIDTH, --width WIDTH
                        width of output image
  -he HEIGHT, --height HEIGHT
                        height of output image
$ python3 image_resize.py /home/hqhs/test.jpg define -w 2000
Image saved on path: /home/hqhs/test__2000x3003.jpg
$ python3 image_resize.py /home/hqhs/test.jpg scale 2
Image saved on path: /home/hqhs/test__638x958.jpg
```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
