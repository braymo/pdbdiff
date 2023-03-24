#!/usr/bin/env python3
#Author: Brad Raymo (braymo)
#purpose: to compare two IXPs and provide a list of unique ASN's per IXP.
import os
import requests
import argparse
import sys
API_KEY = os.environ.get("API_KEY")
from tabulate import tabulate
#data = [[uniq_asn_list]]
auth = {"Authorization": "Api-Key " + API_KEY}
import csv


parser = argparse.ArgumentParser()
parser.add_argument('--ix-list', type=str, help='List of numeric IX IDs to be used in the script', required=True)
args = parser.parse_args()

ixes = [ix.strip() for ix in args.ix_list.split(',')]

def ix_members(ixid):

    members = {}
    r = requests.get('https://www.peeringdb.com/api/ixlan/{}'.format(ixid), headers=auth)

    if r.status_code != 200:
        print(r.text)
        sys.exit(1)
    ixl_data = r.json()


    for member in ixl_data['data'][0]['net_set']:
        members[member['asn']] = member['name']

    return members

ix_nets = {}
for ix in ixes:
    ix_nets[ix] = ix_members(ix)

asns = {}
for k in ix_nets:
    net1 = ix_nets[k]
    for asn in net1:
        name = net1[asn]
        if asn not in asns:
            asns[asn] = {'name': name, 'ixes': {}}
        asns[asn]['ixes'][k] = True

# Here we create a new dict where the key is the IX id and the value is a list of all ASNs in the IX.
data = {}
for ix in ixes:
    data[ix] = []
    for asn in [ x for x in asns if len(asns[x]['ixes']) == 1 ]:
        if ix in asns[asn]['ixes']:
            data[ix].append(asn)

# Here we iterate over our list of IX ids so we can pull the list of asns we generated previously so we can use them for comparison to find out if it's unique to this IX.
for ix in ixes:
    uniq_asn_list = []
    # Iterating over the ASNs in our new dict here.
    for asn in data[ix]:
        # I create a counter to be used later on. It will increment if an ASN is found to be in another IX, making it NOT unique.
        count = 0
        # Iterate over the list of IXs again so we can compare their ASN lists'.
        for _ix in ixes:
            # We don't want to compare against the IX that we know they're in so we skip it.
            if _ix == ix:
                continue
            # We find an ASN that's in the current IX and in another so it's NOT unique. Increment the counter.
            if asn in data[_ix]:
                count += 1
        # We will know if an ASN is unique if its count is 0 because it will not have been found in the other IXs, thus not have a greater number per our logic.
        if count == 0:
            uniq_asn_list.append(asn)
    print("\n\nThe following ASNs are unique to IX ID %s\n\n"% ix)
    #for asn in uniq_asn_list:
        #print(asn)
    print(",".join(str(asn) for asn in uniq_asn_list))
