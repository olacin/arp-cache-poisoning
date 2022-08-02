# arp-cache-poisoning

ARP Cache Poisoning made with Scapy.

To run the attack:
```bash
python ./poisoner.py -g <gateway-ip> -t <target-ip>
```

A successful attack poisons the ARP cache of the victim, resulting in a table like this one:  

| IP         |        MAC        |
|------------|:-----------------:|
| 10.0.0.3   | DE:AD:BE:EF:CA:FE |
| 10.0.0.138 | DE:AD:BE:EF:CA:FE |

You can see that router and attacker have the same MAC on the victim ARP table.

## Dependencies

To install the dependencies you can run
```bash
pip install -r requirements.txt
```
