from rich import box
from rich.panel import Panel
from rich.style import Style
from rich.text import Text

from textual.app import Widget

from .collect_data import CollectData

class Info(Widget):
    def on_mount(self) -> None:
        self.set_interval(1, self.refresh)

    def render(self) -> Panel:
        log_date = CollectData("log_date")
        info = Text.assemble(
            (f"\nLast update: {log_date}\n(Updated every 5 min.)\n\n", "#d75f5f"),
            "The data table gives an overview of the available "
            "recourses on our local machines. On the progress bar "
            "the total load on the machines is reported. "
            "Let's see if we work enough!\n",
            justify="full"
        )

        return Panel(
                 # Text(info, justify="left", style=""),
                 info,
                 border_style="cyan",
                 box=box.SQUARE,
                 title="Local Machines",
                 title_align="left",
                 highlight=True
               )
