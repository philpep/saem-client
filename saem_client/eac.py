"""EAC-CPF records harvesting from SAEM-Ref OAI-PMH repository"""

from __future__ import print_function
from os import path

from lxml import etree

from . import _oai_client


def fetch_eac_records(url, output, verbose=False, limit=None):
    client = _oai_client(url, 'eac')

    records = client.listRecords(metadataPrefix='eac', set='authorityrecord')

    for idx, (header, reader, _) in enumerate(records):
        identifier = header.identifier()
        what, name = identifier.rsplit('/')[-2:]
        fname = '{0}_{1}.xml'.format(what, name)
        fpath = path.join(output, fname)
        if verbose:
            print('saving {0} to {1}'.format(identifier, fpath))
        tree = etree.ElementTree(reader._fields[0])
        with open(fpath, 'wb') as f:
            tree.write(f)
        if limit is not None and idx == limit:
            break
