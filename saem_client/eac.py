"""Download and upload of EAC-CPF data."""

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


def upload_eac(instance, file):
    import requests
    from cwclientlib import cwproxy_for, cwproxy
    proxy = cwproxy_for(instance)
    headers = cwproxy.build_request_headers()
    headers['Content-Type'] = 'application/json'

    # XXX copy of CWProxy.post().
    params = {
        'url': proxy.build_url('/authorityrecord'),
        'headers': headers,
        'verify': proxy._ssl_verify,
        'auth': proxy.auth,
    }
    if proxy.timeout:
        params['timeout'] = proxy.timeout

    with open(file) as f:
        params['data'] = f
        response = requests.post(**params)

    print(response.json)
