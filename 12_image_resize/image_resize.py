from PIL import Image
import argparse
import os.path
from fractions import Fraction


def load_image(img_filepath):
    if not os.path.isfile(img_filepath):
        error = "where's no file for this {} filepath".format(img_filepath)
        return None, error
    try:
        return Image.open(img_filepath), None
    except IOError:
        error = "Can't open file"
        return None, error


def change_image_by_scale(image, scale):
    new_width = int(image.size[0] * scale)
    new_height = int(image.size[1] * scale)
    return image.resize((new_width, new_height))


def change_image_by_definition(image, height, width):
    warning = ""
    if not height:
        old_width = image.size[0]
        old_height = image.size[1]
        scale = width / old_width
        height = int(old_height * scale)
    elif not width:
        old_width = image.size[0]
        old_height = image.size[1]
        scale = height / old_height
        width = int(old_width * scale)
    elif Fraction(image.size[0], image.size[1]) != Fraction(width, height):
        warning = "Output image would be with changed aspect ratio!"
    return image.resize((width, height)), warning


def change_name_for_output(size, path):
    file_name, file_extension = os.path.splitext(path)
    return "".join([file_name, "__{}x{}".format(size[0], size[1]),
                    file_extension])


def save_image(image, output_path, img_file_path):
    if not output_path:
        output_path = change_name_for_output(image.size, img_file_path)
    image.save(output_path)
    print("Image saved: {}".format(output_path))


def parse_input():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "path_to_image", type=str,
        help="File path to image you want to resize."
    )
    parser.add_argument(
        "-o", "--output", type=str,
        help="File path where you want to store changed image."
    )
    subparsers = parser.add_subparsers(
        help="choose the way how you want to change an image"
    )
    parser_scale = subparsers.add_parser(
        "scale", help="change image by scale"
    )
    parser_scale.add_argument(
        "scale_val", type=float,
        help="Input coefficient (could be less then zero)."
    )
    parser_definition = subparsers.add_parser(
        "define", help="define width and/or height"
    )
    parser_definition.add_argument(
        "-w", "--width", type=int,
        help="width of output image"
    )
    parser_definition.add_argument(
        "-he", "--height", type=int,
        help="height of output image"
    )
    args = parser.parse_args()
    if hasattr(args, "height") and not (args.height or args.width):
        error = "You must input at least one number: height or width (or " \
                "both)"
        return None, error
    if hasattr(args, "scale_val") and args.scale_val <= 0:
        error = "Scale must be bigger then zero!"
        return None, error
    return args, None


if __name__ == '__main__':
    error = ""
    args, error = parse_input()
    if error:
        print(error)
        exit()
    default_image, error = load_image(args.path_to_image)
    if error:
        print(error)
        exit()
    if hasattr(args, "scale_val"):
        output_image = change_image_by_scale(default_image, args.scale_val)
    else:
        output_image, warning = change_image_by_definition(default_image,
                                                  args.height, args.width)
        if warning:
            print(warning)
    save_image(output_image, args.output, args.path_to_image)
