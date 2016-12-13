"""Download EAC-CPF XML file by harvesting the SAEM-Ref OAI-PMH repository"""
from argparse import ArgumentParser
import os

from .eac import fetch_eac_records


parser = ArgumentParser(description=__doc__)
parser.add_argument('url', help='base URL of the OAI-PMH end point')
parser.add_argument('-o', '--output', default=os.getcwd(),
                    help='output directory (default to current directory)')
parser.add_argument('-v', '--verbose', action='store_true',
                    help='display progress information')
args = parser.parse_args()
fetch_eac_records(args.url, args.output, args.verbose)
