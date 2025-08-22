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




from core.stats import get_bandwidth
if __name__ == "__main__":
    while True:
        speed = get_bandwidth()
        print(f"Current Bandwidth: {speed:.2f} KB/s")





from core.capture import start_sniffer

if __name__ == "__main__":
    print("Starting packet sniffer...( press Ctrl+C to stop)")
    start_sniffer(interface="eth0")




from core.connections import list_connections

if __name__ == "__main__":
    print("active connection:")
    for c in list_connections():
        print(c)


from ui.cli import start_cli 

if __name__ == "__main__":
    start_cli()