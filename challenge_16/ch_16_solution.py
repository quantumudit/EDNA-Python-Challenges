"""
Monthly Sales Visualization Script
==================================
Author: Udit Kumar Chatterjee
Email: quantumudit@gmail.com
==================================

This script creates a visual representation of monthly sales data for the year 2023.
It uses Matplotlib to generate a line plot of sales figures for each month and applies
the 'Cyberpunk' style for a unique visual effect. Sales data is provided in thousands of 
US dollars (USD) and is formatted with tick labels displaying the values in thousands 
with a '$' sign (e.g., "$35K"). The resulting plot is customized with titles, labels, 
and axis limits for clarity. Additionally, a gradient fill is added to enhance the visual impact.
"""

# Import necessary libraries
import matplotlib.pyplot as plt
import mplcyberpunk
from matplotlib.ticker import FormatStrFormatter

# List of months and corresponding sales numbers (in thousands USD)
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
sales = [25, 35, 32, 40, 38, 37, 48, 43, 34, 41, 45, 42]

# Apply the Cyberpunk style
plt.style.use("cyberpunk")


# Create a figure and axis
fig = plt.figure(figsize=(8, 5), facecolor='#EAEEF1')
ax = fig.add_subplot()

# Plot
ax.plot(months, sales, marker="o")

# Create a FormatStrFormatter for Y-axis labels
tick_fmt = FormatStrFormatter("$%dK")
ax.yaxis.set_major_formatter(tick_fmt)

# Customize the plot
ax.set_title("Monthly Sales Trend - 2023", pad=15, fontweight="heavy")
ax.set_xlabel("Months", labelpad=15, loc="center", fontweight="bold")
ax.set_ylabel("Sales", labelpad=15, loc="center", fontweight="bold")
ax.set_ylim(20, 50)

# Add a gradient fill to the plot
mplcyberpunk.add_gradient_fill(alpha_gradientglow=0.5)

# Save the figure
fig.savefig('./sales_trend_2023.png', dpi=200, orientation='landscape')
