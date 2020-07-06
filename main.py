import argparse
from pathlib import Path

from PyPDF2 import PdfFileMerger, PdfFileReader


def main(directory, prefix, count, outfile):
    m = PdfFileMerger()

    for p in range(count):
        m.append(PdfFileReader(
            f'{directory}/{prefix}{p + 1}.pdf', 'rb'))

    m.write(outfile)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Compress images.')
    parser.add_argument('directory', type=str,
                        help='Directory containing PDFs')
    parser.add_argument('outfile', type=str,
                        help='Output PDF filepath')
    parser.add_argument("--prefix", "-p", type=str, default="",
                        help='Prefix to page number in filename')
    parser.add_argument("--count", "-c", type=int, default=0,
                        help='Number of pdf files')

    args = parser.parse_args()

    main(Path(args.directory), args.prefix, args.count, args.outfile)
