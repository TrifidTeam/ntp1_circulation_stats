ntp1_circulation_stats
===========

Message from the Trifid Team
----------------------------    
This is a quick script to parse the `get_token_holders` Neblio API endpoint and return the total circulating supply and number of unique addresses holding Trifid (TRIF).

If this tool has been helpful please donate NEBL and/or NTP1 tokens to our Dev Team Wallet:
NMi41ze2XnxJrMNGtSGheGqLR3h4dabREW

Requirements
---------------------------- 
This was written in python for other coding purposes and you will need a few packages - if you use python you probably already have most/all of these, but to prevent any ModuleNotFound issues you should run:
```
pip install ast copy logging multiprocessing urllib3 sys six datetime json mimetypes os re tempfile
```

You will also need `swagger_client` as posted from the Neblio team. The `swagger_client` included is configured to communicate with Mainnet.

Python 3.4+ is recommended for this script.
