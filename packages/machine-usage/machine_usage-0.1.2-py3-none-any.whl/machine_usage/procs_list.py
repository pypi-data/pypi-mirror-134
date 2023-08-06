from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from textual.app import Widget

from .collect_data import CollectData
from . import __version__

global scroll_position
scroll_position = [0]

global rows_in_table
rows_in_table = [15]


# Process list Widget
class ProcsList(Widget):

    async def on_resize(self, event) -> None:
        self.width = event.width
        self.height = event.height

    def on_mount(self) -> None:
        self.transition_1 = 100
        self.transition_2 = 70
        self.width = self.transition_1 + 1
        self.height = self.transition_1 + 1

        self.set_interval(0.1, self.refresh)

        self.PrintProcList()
        self.set_interval(0.1, self.PrintProcList)

    def PrintProcList(self) -> None:
        usage_data = CollectData('usage_data')

        table = Table(
            show_header=True,
            header_style="bold #d75f5f",
            padding=(1,0,0,3),
            # box=box.ROUNDED,
            # show_lines=True,
            # border_style="white",
            box=box.SIMPLE_HEAVY,
            border_style="cyan",
            highlight=True,
            expand=True,
            caption = f"Scroll: {scroll_position[0] / (len(usage_data) - rows_in_table[0]) * 100:.0f}%"
        )
        table.add_column(
            "Machine \nroom",
            no_wrap=True,
            width=11
        )
        if not self.width < self.transition_2:
            table.add_column(
                "Master \n",
                no_wrap=True,
                width=10,
                style='dark_sea_green4'
            )
        if not self.width < self.transition_1:
            table.add_column(
                "Connections\n",
                width=14
            )
        table.add_column(
            "Used \ntotal/CPUs",
            no_wrap=True,
            width=10
        )
        table.add_column(
            "Tasks \nper user",
            width = 23,
            no_wrap=True
        )

        for idx, (machine, machine_usage) in enumerate(usage_data.items()):

            # Extract usage data
            location = machine_usage[1]
            master = machine_usage[3]
            connections = list(machine_usage[4].keys())
            process_count = machine_usage[5]

            # Generate process overview
            processes = machine_usage[8]
            user_overview = {}
            for user, tasks in processes.items():
                tmp = []
                for task in tasks:
                    if task[2] != 'tracker+':
                        tmp.append(task[2])
                    else:
                        process_count -= 1
                if tmp != []:
                    user_overview[user] = ", ".join([f"{tmp.count(task)}*{task}" for task in set(tmp)])


            # Determine cpu_usage
            cpu_count = machine_usage[2]
            cpu_usage = f"{process_count} / {cpu_count}"

            if scroll_position[0] <= idx < rows_in_table[0] + scroll_position[0]:
                if self.width < self.transition_2:
                    table.add_row(
                            f"\n{machine} \n{location}",
                            Text(cpu_usage,  style=("#d75f5f" if process_count > 6 else "")),
                            Text(str(user_overview).replace("',", "',\n"))
                    )
                elif self.width < self.transition_1:
                    table.add_row(
                            f"{machine} \n{location}",
                            master,
                            Text(cpu_usage,  style=("#d75f5f" if process_count > 6 else "")),
                            Text(str(user_overview).replace("',", "',\n"))
                    )
                else:
                    table.add_row(
                            f"{machine} \n{location}",
                            master,
                            ", ".join(connections),
                            Text(cpu_usage,  style=("#d75f5f" if process_count > 6 else "")),
                            Text(str(user_overview).replace("',", "',\n"))
                    )

        self.panel = Panel(
                table,
                title="Usage per Machine",
                title_align="left",
                subtitle="machine_usage " + __version__,
                subtitle_align="right",
                border_style="cyan",
                box=box.SQUARE,
        )

        self.refresh()

    def render(self) -> Panel:
        return self.panel
