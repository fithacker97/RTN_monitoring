from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from rich.layout import Layout
from time import sleep

from core.stats import get_bandwidth
from core.connections import list_connections


def render_dashboard():
    layout = Layout()

    # Split main screen into 2 parts
    layout.split(
        Layout(name="upper", ratio=2),
        Layout(name="lower", ratio=1)
    )

    # ---- Bandwidth Panel ----
    download, upload = get_bandwidth()

    bw_table = Table(title="📡 Bandwidth Usage", expand=True)
    bw_table.add_column("Type", style="cyan", no_wrap=True)
    bw_table.add_column("Speed (KB/s)", style="green")

    bw_table.add_row("⬇️ Download", f"{download:.2f}")
    bw_table.add_row("⬆️ Upload", f"{upload:.2f}")

    # Progress bars (relative scale, assume max ~1MB/s for demo)
    prog = Progress()
    prog.add_task("Download", total=1024, completed=download)
    prog.add_task("Upload", total=1024, completed=upload)

    layout["upper"].update(
        Panel.fit(
            f"{bw_table}\n{prog.renderable}",
            title="🌐 Network Status",
            border_style="bold magenta"
        )
    )

    # ---- Connections Panel ----
    conns = list_connections()

    conn_table = Table(title="🔗 Active Connections", expand=True)
    conn_table.add_column("Local", style="yellow")
    conn_table.add_column("Remote", style="cyan")
    conn_table.add_column("PID", style="green")

    for c in conns[:5]:  # show only top 5
        conn_table.add_row(c["laddr"], str(c["raddr"]), str(c["pid"]))

    layout["lower"].update(
        Panel(conn_table, title="🔍 Connections", border_style="bold blue")
    )

    return layout


def start_cli():
    with Live(render_dashboard(), refresh_per_second=1, screen=True) as live:
        while True:
            live.update(render_dashboard())
            sleep(1)

