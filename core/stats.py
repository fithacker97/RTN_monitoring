import psutil
import time

def get_bandwidth(interval=1):
    old = psutil.net_io_counters()
    time.sleep(interval)
    new = psutil.net_io_counters()

    download = (new.bytes_recv - old.bytes_recv) / 1024  # KB/s
    upload = (new.bytes_sent - old.bytes_sent) / 1024   # KB/s

    return download, upload 