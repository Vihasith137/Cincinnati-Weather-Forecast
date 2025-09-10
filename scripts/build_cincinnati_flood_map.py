"""
Mock visualization of Cincinnati flood risk map.
Shows Ohio River floodplain + neighborhood labels + simulated risk points.
"""

import matplotlib.pyplot as plt
import numpy as np

# City outline (abstract polygon)
cincinnati_outline = np.array([
    [0,0], [10,0], [12,3], [11,7], [7,9], [3,8], [1,5], [0,0]
])

# Ohio River floodplain
ohio_river = np.array([
    [0,-0.5], [12,-0.5], [12,1.5], [0,1.5], [0,-0.5]
])

# Generate simulated flood risk points
np.random.seed(42)
n_points = 200
x = np.random.uniform(0, 12, n_points)
y = np.random.uniform(0, 9, n_points)
risk = np.exp(-(y-1.5)**2/4)

plt.figure(figsize=(10,7))
plt.fill(ohio_river[:,0], ohio_river[:,1], color="lightblue", alpha=0.6, label="Ohio River Floodplain")
plt.plot(cincinnati_outline[:,0], cincinnati_outline[:,1], color="black", linewidth=2)

sc = plt.scatter(x, y, c=risk, cmap="Blues", s=60, alpha=0.7)

# Neighborhood labels (mock positions)
neighborhoods = {
    "Downtown": (6, 2.5),
    "Over-the-Rhine": (6, 4.5),
    "Walnut Hills": (8.5, 5.5),
    "Westwood": (2, 6.5),
    "Avondale": (7, 6.8),
    "Price Hill": (3.5, 2.0),
    "Clifton": (5.5, 7.5)
}

for name, (nx, ny) in neighborhoods.items():
    plt.text(nx, ny, name, fontsize=9, weight="bold", ha="center", color="darkred")

plt.text(6, 0.5, "Ohio River", fontsize=11, color="navy", ha="center")

plt.colorbar(sc, label="Flood Risk (darker = higher)")
plt.title("Cincinnati Topographic Flood Risk Map (Mock Visualization)", fontsize=14)
plt.xlabel("Longitude (simulated)")
plt.ylabel("Latitude (simulated)")
plt.legend()
plt.tight_layout()
plt.savefig("images/cincinnati_flood_risk_map.png", dpi=150)
plt.show()
