import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
dates = pd.date_range(start="2025-09-01", periods=7)
rainfall = np.random.uniform(0.5, 3.5, len(dates))
overflows = np.random.randint(10, 60, len(dates))

trend_df = pd.DataFrame({
    "Date": dates,
    "Rainfall (inches)": rainfall,
    "Sewer Overflows": overflows
})

fig, ax1 = plt.subplots(figsize=(10, 6))
ax1.plot(trend_df["Date"], trend_df["Rainfall (inches)"], marker="o", color="tab:blue", label="Rainfall")
ax1.set_xlabel("Date")
ax1.set_ylabel("Rainfall (inches)", color="tab:blue")
ax1.tick_params(axis="y", labelcolor="tab:blue")

ax2 = ax1.twinx()
ax2.plot(trend_df["Date"], trend_df["Sewer Overflows"], marker="s", linestyle="--", color="tab:red", label="Overflows")
ax2.set_ylabel("Sewer Overflows", color="tab:red")
ax2.tick_params(axis="y", labelcolor="tab:red")

plt.title("7-Day Rainfall vs Sewer Overflow Trend (Cincinnati)", fontsize=14)
fig.tight_layout()
plt.savefig('images/rainfall_sewer_overflow.png')
plt.show()
