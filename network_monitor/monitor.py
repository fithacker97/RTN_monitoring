import time
import psutil

def show_bandwidth():
    old = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
    while True:
        time.sleep(1)
        new = psutil.net_io_counters().bytes_sent + psutil.net_io_counters().bytes_recv
        bandwidth = (new - old) / 1024
        print(f"Bandwidth: {bandwidth} KB/s")
        old = new
if __name__ == "__main__":
    show_bandwidth()