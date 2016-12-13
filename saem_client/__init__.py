"""Interact with a SAEM-Ref server"""

from oaipmh.client import Client
from oaipmh.metadata import MetadataRegistry, MetadataReader


def _oai_client(url, prefix):
    registry = MetadataRegistry()
    registry.registerReader(prefix, MetadataReader)
    if not url.endswith('/'):
        url += '/'
    url += 'oai'
    return Client(url, registry)


def _add_generic_arguments(parser):
    import os
    parser.add_argument('url', help='base URL of the SAEM-Ref instance')
    parser.add_argument('-o', '--output', default=os.getcwd(),
                        help='output directory (default to current directory)')
    parser.add_argument('--limit', type=int,
                        help='fetch at much LIMIT records')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='display progress information')


def main():
    from argparse import ArgumentParser
    from .eac import fetch_eac_records
    from .skos import fetch_concepts

    parser = ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers()
    eac_parser = subparsers.add_parser(
        'eac', help='download EAC-CPF authority records')
    eac_parser.set_defaults(func=fetch_eac_records)
    _add_generic_arguments(eac_parser)
    skos_parser = subparsers.add_parser(
        'skos', help='download a SKOS concept scheme')
    _add_generic_arguments(skos_parser)
    skos_parser.add_argument(
        'scheme', help='identifier of the concept scheme')
    skos_parser.set_defaults(func=fetch_concepts)
    args = parser.parse_args()
    func = args.func
    del args.func
    func(**vars(args))
