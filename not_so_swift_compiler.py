from src.start_compiler import start_compiler

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Not so swift compiler.')
    parser.add_argument('--f_input',
                        help='path to input file...',  required=True)
    parser.add_argument('--out',  default="./",
                        help='path to output dir...')

    args = parser.parse_args()

    start_compiler(input_file_name=args.f_input, output_dir=args.out)
