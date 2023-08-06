#!/usr/bin/env python3

import argparse
import csv

def main():
    parser = argparse.ArgumentParser(
        description="Tool to remove districts from a block equivalency csv.")
    parser.add_argument(
        'blocks.csv',
        type=argparse.FileType('r'),
        help="Requires BLOCKID and DISTRICT fields.")
    parser.add_argument(
        '--districts',
        type=str,
        help="List of districts to remove separated by commas.")
    parser.add_argument(
        'output-blocks.csv',
        type=argparse.FileType('w'),
        help="Output file for the block equivalency file with the districts removed.")

    args = parser.parse_args()

    districts = args.districts.split(',')

    with vars(args)['output-blocks.csv'] as outputFile, vars(args)['blocks.csv'] as inputFile:
        writer = csv.DictWriter(
            outputFile,
            fieldnames=['BLOCKID','DISTRICT'])
        writer.writeheader()
        reader = csv.DictReader(inputFile)
        for row in reader:
            if row['DISTRICT'] not in districts:
                writer.writerow({
                    'DISTRICT': row['DISTRICT'],
                    'BLOCKID' : row['BLOCKID']
                    })
main()
