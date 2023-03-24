# pdbdiff
Compare two IXPs and print unique asn's per IX in csv to terminal

API Key must be stored in your environment. Instrutions can be found in the PeeringDB api documentation found here:
https://docs.peeringdb.com/howto/api_keys/

usage: pdbdiff.py IXP ID1 IXP ID2

```
pdbdiff.py 254 1207

IXP Any2Denver - Total Unique ASNs: 52

20412,399647,62642,32035,3300,398570,14701,40160,11711,14593,21777,36692,53766,33438,32261,6122,714,5715,55256,46489,17306,15188,32798,15305,2734,53828,11071,199524,22822,26253,62695,54113,30081,16406,16832,2635,21832,4181,22616,21928,31939,6507,19754,32184,15133,26801,393552,32281,400771,19165,23473,395354

IXP Any2Denver - Total Unique ASNs: 43

396037,13807,7155,4150,13765,16552,64227,53597,398998,399029,26446,31834,13576,393950,21947,32621,10242,14537,62887,33302,394594,11961,13760,30174,3856,29831,1025,8674,397142,26156,55044,14371,27400,22995,395194,18451,26415,53454,14570,36236,42,4556,30688
```

