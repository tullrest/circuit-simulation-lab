import csv
import matplotlib.pyplot as plt
from pathlib import Path

project_dir = Path(__file__).resolve().parent.parent

loads = []
powers = []
delays = []

with open(project_dir / "results" / "full_results.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # skip header

    for row in reader:
        if not row:
            continue
        loads.append(float(row[0]))
        powers.append(float(row[1]))
        delays.append(float(row[2]))

# Power graph
plt.figure(figsize=(8, 5))
plt.plot(loads, powers, marker="o")
plt.xlabel("Load Capacitance (fF)")
plt.ylabel("Average Power (nW)")
plt.title("Load Capacitance vs Average Power")
plt.grid(True)
plt.savefig(project_dir / "images" / "power_vs_load.png", dpi=300, bbox_inches="tight")
plt.close()

# Delay graph
plt.figure(figsize=(8, 5))
plt.plot(loads, delays, marker="o")
plt.xlabel("Load Capacitance (fF)")
plt.ylabel("Propagation Delay (ps)")
plt.title("Load Capacitance vs Propagation Delay")
plt.grid(True)
plt.savefig(project_dir / "images" / "delay_vs_load.png", dpi=300, bbox_inches="tight")
plt.close()

print("Graphs saved!")
print("Created: power_vs_load.png")
print("Created: delay_vs_load.png")
