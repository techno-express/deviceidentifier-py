#!/usr/bin/env python
from deviceidentifier.api import query

import os, sys, json

def main():
    # Sample showing how to look up data from a GSMA ICCID.

    if len(sys.argv) < 2:
        print 'Usage: provide a GSMA ICCID for a breakdown of data on it.'
        exit(-1)

    if not 'RI_DEVID_TOKEN' in os.environ:
        raise Exception( 'RI_DEVID_TOKEN API token environment variable not set; you must provde an API token' )

    number = sys.argv[1:][0]
    print json.dumps( query( os.environ['RI_DEVID_TOKEN'],gsma_iccid=number ), indent=4 )

if __name__ == '__main__':
    main()