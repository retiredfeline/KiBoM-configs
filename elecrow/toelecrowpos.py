#!/usr/bin/env python3

"""Convert KiCad top POS file to Elecrow POS file"""

import sys
import argparse
import csv


def processfile(filename):
    """Process one CSV file"""
    with open(filename) as filehandle:
        reader = csv.DictReader(filehandle, fieldnames=[
            'Designator', 'Value', 'Footprint', 'Center-X(mm)', 'Center-Y(mm)', 'Rotation',
            'Layer'])
        writer = csv.DictWriter(sys.stdout, extrasaction='ignore', fieldnames=[
            'Designator', 'Footprint', 'Center-X(mm)', 'Center-Y(mm)', 'Layer', 'Rotation'])
        writer.writeheader()
        for row in reader:
            if row['Layer'] != 'Side':
                row['Layer'] = row['Layer'].capitalize() + 'Layer'
                writer.writerow(row)


def main():
    """Main program"""
    parser = argparse.ArgumentParser(
        description='Convert KiCad POS file to Elecrow POS file on stdout')
    parser.add_argument('filenames', metavar='file',
                        nargs='+', help='CSV file')
    args = parser.parse_args()
    for filename in args.filenames:
        try:
            processfile(filename)
        except IOError:
            print(f"Cannot open {filename}")


if __name__ == '__main__':
    main()
