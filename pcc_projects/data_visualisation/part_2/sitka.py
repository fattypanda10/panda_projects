from datetime import datetime
import csv
import matplotlib.pyplot as plt

file_name = "./data_weather/death_valley_2018_simple.csv"
with open(file_name, "r") as f:
    reader = csv.reader(f)
    header = next(reader)
    rainfall, high_temp, low_temp, dates = [], [], [], []
    for i in reader:
        try:
            high = int(i[header.index("TMAX")])
            low = int(i[header.index("TMIN")])
            rain = float(i[header.index("PRCP")])
        except ValueError:
            print(f"missing value: {i[2]}")
        else:
            high_temp.append(high)
            low_temp.append(low)
            rainfall.append(rain)
            dates.append(datetime.strptime(i[header.index("DATE")], "%Y-%m-%d"))

plt.style.use("seaborn")
fig, ax = plt.subplots()
ax.plot(dates, high_temp, c="red", alpha=0.5)
ax.plot(dates, low_temp, c="blue", alpha=0.5)
# ax.plot(dates, rainfall, c='green', alpha=0.5) # rainfall
ax.fill_between(dates, high_temp, low_temp, facecolor="blue", alpha=0.1)
ax.set_title("Daily Temperatures", fontsize=18)
ax.set_xlabel("", fontsize=16)
fig.autofmt_xdate()
ax.set_ylim(0, 150)
ax.set_ylabel("Temperature (F)", fontsize=16)
ax.tick_params(axis="both", which="major", labelsize=16)
plt.show()
