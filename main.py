import argparse
from pathlib import Path

from PyPDF2 import PdfFileMerger, PdfFileReader
from tqdm import tqdm


def main(directory: Path, outfile: Path):
    m = PdfFileMerger()

    for path in tqdm(tuple(directory.rglob("*.pdf"))):
        m.append(PdfFileReader(str(path), 'rb'))

    m.write(str(outfile))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compress images.')
    parser.add_argument('directory', type=Path,
                        help='Directory containing PDFs')
    parser.add_argument('outfile', type=Path,
                        help='Output PDF filepath')

    args = parser.parse_args()

    main(args.directory, args.outfile)
