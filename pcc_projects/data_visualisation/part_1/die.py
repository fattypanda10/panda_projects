from random import randint
from math import prod
from typing import Callable
from plotly.graph_objs import Bar, Layout
from plotly import offline


class Die:
    def __init__(self, num_sides=6):
        self.num_sides = num_sides

    def roll(self):
        return randint(1, self.num_sides)


def get_roll_freq(
    num_die: int, num_sides: list[int], num_rolls: int, operation: Callable = sum
) -> dict:
    if len(num_sides) == num_die:
        die = [Die(num_sides[i]) for i in range(num_die)]
        max_roll_val = operation([i.num_sides for i in die])
        die_rolls = [
            operation([die[i].roll() for i in range(num_die)]) for i in range(num_rolls)
        ]
        freq_count = {i: die_rolls.count(i) for i in range(num_die, max_roll_val + 1)}
        return freq_count


def plot_bar(freq: dict, file_name: str) -> None:
    x_vals = list(freq.keys())
    data = [Bar(x=x_vals, y=list(freq.values()))]
    x_axis_config = {"title": "Result", "dtick": 1}
    y_axis_config = {"title": "Frequency of Result"}
    my_layout = Layout(title="Bar Plot", xaxis=x_axis_config, yaxis=y_axis_config)
    offline.plot({"data": data, "layout": my_layout}, filename=file_name + ".html")


plot_bar(
    get_roll_freq(num_die=2, num_sides=[6, 6], num_rolls=1000, operation=sum),
    "bar_plotly",
)
