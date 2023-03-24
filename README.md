# pdbdiff
Compare two IXPs and print unique asn's per IX in csv to terminal

API Key must be stored in your environment. Instrutions can be found in the PeeringDB api documentation found here:
https://docs.peeringdb.com/howto/api_keys/

usage: pdbdiff.py IXP ID1 IXP ID2

example: pdbdiff.py 254 1207

IXP 254 - Total Unique ASNs: 52

398570,32798,4181,2734,15188,21832,40160,32261,33438,14593,393552,31939,46489,21928,20412,26253,5715,17306,62695,30081,400771,22822,62642,32184,714,15305,3300,2635,22616,6507,6122,36692,14701,26801,199524,55256,11711,54113,53828,16406,32281,19754,53766,21777,16832,23473,395354,15133,32035,11071,19165,399647

IXP 1207 - Total Unique ASNs: 43

13760,31834,32621,394594,14537,13765,14371,29831,26415,11961,8674,62887,4150,4556,395194,26156,398998,27400,1025,396037,3856,53454,13576,399029,55044,33302,21947,22995,64227,10242,30174,18451,7155,53597,26446,30688,36236,42,14570,13807,397142,393950,16552
