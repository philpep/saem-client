"""SKOS concepts harvesting from SAEM-Ref OAI-PMH repository"""
from __future__ import print_function

import os
from os import path

from lxml import etree

from . import _oai_client


def fetch_concepts(url, scheme, output, from_date=None, until_date=None,
                   verbose=False, limit=None):
    client = _oai_client(url, 'rdf')
    records = client.listRecords(metadataPrefix='rdf',
                                 set='concept:in_scheme:{0}'.format(scheme),
                                 from_=from_date, until=until_date)

    outdir = path.join(output, scheme.replace('/', '-'))
    if not path.isdir(outdir):
        os.makedirs(outdir)

    for idx, (header, reader, _) in enumerate(records):
        identifier = header.identifier()
        what, name = identifier.rsplit('/')[-2:]
        fname = '{0}_{1}.xml'.format(what, name)
        fpath = path.join(outdir, fname)
        if verbose:
            print('saving {0} to {1}'.format(identifier, fpath))
        tree = etree.ElementTree(reader._fields[0])
        with open(fpath, 'wb') as f:
            tree.write(f)
        if limit is not None and idx == limit:
            break
