from watermark import Watermark
import argparse
import os


def apply_watermark(file_path, args):

    # Process an individual file
    image = Watermark(file_path)
    image.apply_text(args.text, tile=args.tile)

    if args.output_dir:
        output_file = os.path.join(args.output_dir, os.path.basename(file_path))
    else:
        output_file = file_path

    print("Saving " + output_file)
    image.save(output_file)

def main():

    valid_files = ['.jpg', '.png', '.gif']

    parser = argparse.ArgumentParser("Python-based Image Watermarker")
    parser.add_argument('files_or_dirs', nargs='+',
                        help='Files or directories on which to apply watermarks')
    parser.add_argument('-t', '--text', required=True, type=str, help='Text watermark to apply.')
    parser.add_argument('-l', '--tile', default=False, action='store_true',
                        help='Tile watermark multiple times across image')
    parser.add_argument('-o', '--output_dir', default=None,
                        help='Directory in which to place output files.  If not specified, the source files will be'
                             'replaced.')
    parser.add_argument('-q', '--quiet', default=False, action='store_true',
                        help='If specified, watermarking will be performed without any prompting.')

    args = parser.parse_args()

    for file_or_dir in args.files_or_dirs:
        if os.path.isfile(file_or_dir):
            apply_watermark(file_or_dir, args)
        if os.path.isdir(file_or_dir):
            for root, dirs, files in os.walk(file_or_dir):
                for image_file in files:
                    if os.path.splitext(image_file)[1] in valid_files:
                        apply_watermark(os.path.join(root, image_file), args)

    print("done.")

if __name__ == "__main__":
    main()

# watermarked = Watermark("C:\\Users\\svitale\\Downloads\\2015-06-12 14_29_58-Postman.png")
# watermarked.apply_text("\xa9 Vitale's Studio", tile=True)
# watermarked.save("C:\\Users\\svitale\\Downloads\\2015-06-12 14_29_58-Postman - watermark.png")
