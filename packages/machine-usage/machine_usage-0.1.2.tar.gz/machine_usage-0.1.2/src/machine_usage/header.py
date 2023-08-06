from datetime import datetime
import getpass, platform, distro

from textual.app import Widget

from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.style import Style

# Header widget
class Header(Widget):
    def on_mount(self) -> None:
        self.width = 0
        self.height = 0
        self.set_interval(1.0, self.refresh)

        username = getpass.getuser()
        ustring = f"{username} @"
        node = platform.node()
        if node:
            ustring += f" [b]{platform.node()}[/]"

        ri = distro.os_release_info()
        system_list = [ri["name"]]
        if "version_id" in ri:
            system_list.append(ri["version_id"])
        system_string = " ".join(system_list)

        self.title = "Machine Usage"
        self.left_string = " ".join([ustring, system_string])
        self.style = Style(color="magenta", bold=True)

    def render(self) -> Panel:
        table = Table(show_header=False, expand=True, box=None, padding=0, highlight=True)
        if self.width < 100:
            table.add_column(justify="left", no_wrap=True, ratio=1)
            table.add_column(justify="right", no_wrap=True, ratio=1)
            table.add_row(self.title, datetime.now().strftime("%c"))
        else:
            table.add_column(justify="left", no_wrap=True, ratio=1)
            table.add_column(justify="center", no_wrap=True, ratio=1)
            table.add_column(justify="right", no_wrap=True, ratio=1)
            table.add_row(
                self.left_string, self.title,
                datetime.now().strftime("%c"),
                style=self.style
            )

        panel = Panel(
            table,
            border_style="cyan",
            box=box.SQUARE,
        )
        return panel

    async def on_resize(self, event) -> None:
        self.width = event.width
        self.height = event.height
