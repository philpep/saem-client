"""Interact with a SAEM-Ref server"""

import os


def _oai_client(url, prefix):
    from oaipmh.client import Client
    from oaipmh.metadata import MetadataRegistry, MetadataReader

    registry = MetadataRegistry()
    registry.registerReader(prefix, MetadataReader)
    if not url.endswith('/'):
        url += '/'
    url += 'oai'
    return Client(url, registry)


def _add_generic_arguments(parser):
    parser.add_argument('url', help='base URL of the SAEM-Ref instance')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='display progress information')


def _add_oai_arguments(parser):
    _add_generic_arguments(parser)
    parser.add_argument('-o', '--output', default=os.getcwd(),
                        help='output directory (default to current directory)')
    parser.add_argument('--limit', type=int,
                        help='fetch at much LIMIT records')


def main():
    from argparse import ArgumentParser
    from .eac import fetch_eac_records, upload_eac
    from .skos import fetch_concepts

    parser = ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers()

    eac_parser = subparsers.add_parser(
        'eac-download', help='download EAC-CPF authority records')
    eac_parser.set_defaults(func=fetch_eac_records)
    _add_oai_arguments(eac_parser)

    skos_parser = subparsers.add_parser(
        'skos-download', help='download a SKOS concept scheme')
    skos_parser.set_defaults(func=fetch_concepts)
    _add_oai_arguments(skos_parser)
    skos_parser.add_argument(
        'scheme', help='identifier of the concept scheme')

    eac_upload = subparsers.add_parser(
        'eac-upload', help='upload an EAC-CPF file')
    eac_upload.set_defaults(func=upload_eac)
    _add_generic_arguments(parser)
    eac_upload.add_argument(
        'file', help='file path of the EAC-CPF file to upload')
    eac_upload.add_argument('--credentials-file', default='cubicweb.yaml',
                            help='credentials file, '
                            'should contains values for "id" and "secret"')

    args = parser.parse_args()
    func = args.func
    del args.func
    func(**vars(args))
