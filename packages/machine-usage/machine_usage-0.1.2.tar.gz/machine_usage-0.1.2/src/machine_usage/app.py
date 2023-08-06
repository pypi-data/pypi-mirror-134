from textual import events
from textual.app import App

from .header import Header
from .info import Info
from .user_stat import UserStat
from .procs_list import ProcsList, scroll_position, rows_in_table
from .collect_data import CollectData

# Central textual app
class App(App):
        async def on_mount(self, event: events.Mount) -> None:

            grid = await self.view.dock_grid(edge="left")

            grid.add_column(fraction=35, name="left")
            grid.add_column(fraction=65, name="right")

            grid.add_row(size=3, name="topline")
            grid.add_row(size=10, name="top")
            grid.add_row(fraction=10, name="center")
            grid.add_row(fraction=1, name="bottom")

            grid.add_areas(
                area0="left-start|right-end,topline",
                area1="left,top",
                area2="left,center-start|bottom-end",
                area3="right,top-start|bottom-end",
            )

            grid.place(
                area0=Header(),
                area1=Info(),
                area2=UserStat(),
                area3=ProcsList()
            )

        async def action_scroll_down(self) -> None:
            usage_data = CollectData('usage_data')
            rows = len(usage_data)

            global scroll_position
            if scroll_position[0] < rows - rows_in_table[0] / 2:
                scroll_position[0] = scroll_position[0] + 1

        async def action_scroll_up(self) -> None:
            global scroll_position
            if scroll_position[0] > 0:
                scroll_position[0] = scroll_position[0] - 1

        async def on_load(self, _):
            await self.bind("q", "quit", "quit")
            await self.bind("j", "scroll_down", "action")
            await self.bind("k", "scroll_up", "action")
