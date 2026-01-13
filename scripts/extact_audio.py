from audacity_converter import Converter

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Converts an audacity file to .wav format"
    )

    parser.add_argument("file_path", type=str, help="Path to audacity file")
    parser.add_argument(
        "output_path",
        type=str,
        help="Path to extracted data in .wav file",
    )

    args = parser.parse_args()

    converter = Converter(path=args.file_path)
    converter.extract_audio(args.output_path)
