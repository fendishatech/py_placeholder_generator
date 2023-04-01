import argparse
# Local Files
from placeholder_generator import PlaceholderGenerator


def main ():
    parser = argparse.ArgumentParser()

    # Add arguments.
    parser.add_argument('--width', '-w', help = "An integer number indicating the width of the generated placeholder.", type=int, default=0)
    parser.add_argument('--height', '-hg', help = "An integer number indicating the height of the generated placeholder.", type=int, default=0)
    parser.add_argument('--fill', '-f', help = "An string of named color or hexadecimal number indicating the height of the generated placeholder.", type=str)
    parser.add_argument('--text-color', '-tc', type=str, help='Color of the dimensions text')
    parser.add_argument('--text-size', '-ts', type=int, help='Font size of the dimensions text')
    parser.add_argument('--folder', '-fl',type=str, help='Folder created in the current directory')

    # Parse args.
    args = parser.parse_args()

    # TEST SECTION
    print(f"args => {args}")
    print(f"width => {args.width}")
    print(f"height => {args.height}")

    # Use Generator.
    generator = PlaceholderGenerator(
                    args.width,
                    args.height,
                    args.fill,
                    args.text_color,
                    args.text_size                    
                )
    
    generator.generate(args.folder,)

if __name__ == "__main__":
    main()