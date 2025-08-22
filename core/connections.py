import psutil

def list_connections():
    connections = psutil.net_connections(kind="inet")
    active = []
    for conn in connections:
        if conn.status == "ESTABLISHED":
            active.append({"laddr": f"{conn.laddr.ip}: {conn.laddr.port}", "raddr": f"{conn.raddr.ip}: {conn.raddr.port}" if conn.raddr else None, "pid": conn.pid})
    return active


