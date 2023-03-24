#!/usr/bin/env python3
#Author: Brad Raymo (braymo)
#purpose: to compare two IXPs and provide a list of unique ASN's per IXP.
import os
import requests
import argparse
from tabulate import tabulate

API_KEY = os.environ.get("API_KEY")
auth = {"Authorization": "Api-Key " + API_KEY}

parser = argparse.ArgumentParser()
parser.add_argument('ix1_id', type=int, help='Numeric ID for the first IXP')
parser.add_argument('ix2_id', type=int, help='Numeric ID for the second IXP')
args = parser.parse_args()

# Retrieve data for the first IXP
url1 = f'https://www.peeringdb.com/api/netixlan?ix_id={args.ix1_id}&fields=asn&pretty'
response1 = requests.get(url1, headers=auth)

if response1.status_code != 200:
    print(f'Error: {response1.status_code}')
    exit(1)

asns1 = set()
for entry in response1.json()['data']:
    asn = entry.get('asn')
    if asn is not None:
        asns1.add(str(asn).replace('\n', ','))

# Retrieve data for the second IXP
url2 = f'https://www.peeringdb.com/api/netixlan?ix_id={args.ix2_id}&fields=asn&pretty'
response2 = requests.get(url2, headers=auth)

if response2.status_code != 200:
    print(f'Error: {response2.status_code}')
    exit(1)

asns2 = set()
for entry in response2.json()['data']:
    asn = entry.get('asn')
    if asn is not None:
        asns2.add(str(asn).replace('\n', ','))

# Compute unique ASNs for each IXP
unique_asns1 = asns1.difference(asns2)
unique_asns2 = asns2.difference(asns1)

# Print CSV to screen for each IXP
print(f'IXP {args.ix1_id} - Total Unique ASNs: {len(unique_asns1)}\n')
print(','.join(unique_asns1))

print(f'\nIXP {args.ix2_id} - Total Unique ASNs: {len(unique_asns2)}\n')
print(','.join(unique_asns2))
