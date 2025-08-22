from scapy.all import sniff, IP, TCP, UDP
from collections import defaultdict
import time

traffic_stats = defaultdict(lambda: {"bytes": 0, "last_bytes": 0, "bps": 0})

def packet_handler(pkt):
    if IP in pkt:
        src = pkt[IP].src
        dst = pkt[IP].dst
        proto = "TCP" if TCP in pkt else "UDP" if UDP in pkt else "OTHER"
        length = len(pkt)

        key = (src, dst, proto)
        traffic_stats[key]["bytes"] += length

def start_sniffer(interface=None):
    sniff(prn=packet_handler, iface=interface, store=False)

def get_connection_bandwidth(interval=1):
    """Calculate bandwidth per connection in KB/s"""
    time.sleep(interval)
    conn_bw = []

    for key, stats in traffic_stats.items():
        diff = stats["bytes"] - stats["last_bytes"]
        kbps = diff / 1024 / interval
        stats["bps"] = kbps
        stats["last_bytes"] = stats["bytes"]

        if kbps > 0:  # show only active ones
            conn_bw.append({
                "src": key[0],
                "dst": key[1],
                "proto": key[2],
                "kbps": kbps
            })

    # Sort by bandwidth (top talkers first)
    conn_bw.sort(key=lambda x: x["kbps"], reverse=True)
    return conn_bw

