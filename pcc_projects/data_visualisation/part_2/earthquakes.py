import json

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

with open("./data_earthquakes/eq_data_30_day_m1.json", "r") as f:
    eq_data = json.load(f)

meta_title = eq_data["metadata"]["title"]
eq_dict = eq_data["features"]
eq_mags = [i["properties"]["mag"] for i in eq_dict]
eq_longs = [i["geometry"]["coordinates"][0] for i in eq_dict]
eq_lats = [i["geometry"]["coordinates"][1] for i in eq_dict]
eq_titles = [i["properties"]["title"] for i in eq_dict]

# mapping the eq
# data = [Scattergeo(lon=eq_longs, lat=eq_lats)]
data = [
    {
        "type": "scattergeo",
        "lon": eq_longs,
        "lat": eq_lats,
        "text": eq_titles,
        "marker": {
            "size": [5 * mag for mag in eq_mags],
            "color": eq_mags,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Magnitude"},
        },
    }
]
my_layout = Layout(title=meta_title)

fig = {"data": data, "layout": my_layout}
offline.plot(fig, filename="global_earthquakes.html")
