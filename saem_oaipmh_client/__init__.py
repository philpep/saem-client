"""Download EAC-CPF XML file by harvesting the SAEM-Ref OAI-PMH repository"""


def _add_generic_arguments(parser):
    import os
    parser.add_argument('url', help='base URL of the OAI-PMH end point')
    parser.add_argument('-o', '--output', default=os.getcwd(),
                        help='output directory (default to current directory)')
    parser.add_argument('--limit', type=int,
                        help='fetch at much LIMIT records')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='display progress information')


def main():
    from argparse import ArgumentParser
    from .eac import fetch_eac_records
    parser = ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers()
    eac_parser = subparsers.add_parser(
        'eac', help='download EAC-CPF authority records')
    _add_generic_arguments(eac_parser)
    skos_parser = subparsers.add_parser(
        'skos', help='download a SKOS concept scheme')
    _add_generic_arguments(skos_parser)
    skos_parser.add_argument(
        'scheme', help='identifier of the concept scheme')
    args = parser.parse_args()
    fetch_eac_records(**vars(args))
