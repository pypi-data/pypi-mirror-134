from rich import box
from rich.panel import Panel
from rich.table import Table
from rich.text import Text
from rich.progress_bar import ProgressBar

from textual.app import Widget

from .collect_data import CollectData

# Widget containing total usage and usage ranking
class UserStat(Widget):
    def on_mount(self) -> None:
        self.set_interval(1, self.refresh)

    def gen_usage_bar(self) -> Panel:
        usage_data = CollectData("usage_data")

        cpu_count = 0
        process_count = 0
        for _, machine_usage in usage_data.items():
            cpu_count += int(machine_usage[2])
            process_count += int(machine_usage[5])
        load_percentage = process_count / cpu_count * 100

        usage_bar = Table(
            show_header=False,
            box=None,
            expand=True
        )

        usage_bar.add_column("title", no_wrap=True, width=11)
        usage_bar.add_column("progress_bar", no_wrap=True, ratio=100)
        usage_bar.add_column("percentage", no_wrap=True, width=5)

        usage_bar.add_row(
            Text("Total Usage", style=("bold red" if load_percentage > 80 else "bold #d75f5f")),
            ProgressBar(total=100,
            completed=load_percentage),
            Text(f"{load_percentage:.1f}%", style=("red" if load_percentage > 80 else ""))
        )
        usage_bar_panel = Panel(
            usage_bar,
            border_style=("bold red" if load_percentage > 80 else "bold #d75f5f")
        )
        return usage_bar_panel

    def gen_usage_table(self) -> Panel:
        usage_data = CollectData("usage_data")

        tasks_per_user = {}
        total_tasks = 0
        for _, machine_usage in usage_data.items():
            # Generate process overview
            processes = machine_usage[8]
            for user, tasks in processes.items():
                if user in tasks_per_user:
                    tasks_per_user[user] += len(tasks)
                    total_tasks += len(tasks)
                else:
                    tasks_per_user[user] = len(tasks)
                    total_tasks += len(tasks)

        usage_table = Table(
                    show_header=True,
                    header_style="bold dark_sea_green4",
                    box=box.SIMPLE_HEAVY,
                    border_style="dark_sea_green4",
                    expand=True,
                    highlight = True
                )

        usage_table.add_column("", no_wrap=True, width=9)
        usage_table.add_column("User", no_wrap=True, width=13)
        usage_table.add_column("Used %", no_wrap=True, width=11)

        sorted_tpu = sorted(tasks_per_user.items(), key=lambda item: item[1], reverse=True)
        for idx, (user, tasks) in enumerate(sorted_tpu, start=1):
            if idx <= 10:
                usage_percentage = tasks/total_tasks*100
                usage_table.add_row(
                    Text(f"{idx}."),
                    f"{user}",
                    Text(f"{usage_percentage:.0f}%", style="#00afaf")
                )

        usage_table_panel = Panel(
            usage_table,
            title="User Ranking",
            border_style="dark_sea_green4",
            highlight=True
        )
        return usage_table_panel

    def render(self) -> Panel:

        usage_bar = self.gen_usage_bar()
        usage_table = self.gen_usage_table()

        table = Table(
            show_header=False,
            box=box.SIMPLE_HEAVY,
            border_style="cyan",
            highlight=True,
            expand=True
        )
        table.add_column("main", no_wrap=True, width=11, justify='center')


        help_txt = (
            "Scroll down with j\n"
            "Scroll up with k\n"
            "Press q to exit"
        )

        help_panel = Panel(help_txt, style='bold')

        table.add_row(usage_bar)
        table.add_row(usage_table)
        table.add_row(help_panel)

        panel = Panel(
            table,
            title="Usage Overview",
            title_align="left",
            border_style="cyan",
            box=box.SQUARE,
        )

        return panel
