from email.base64mime import header_length
from simulator.simulation import Simulation
import matplotlib.pyplot as plt
import numpy as np
from helpers import to_euro, get_cmap

class Simulator():



    def run_a(self, price, costs):
        order_quantities = [i + 1 for i in range(1,101)]
        fig, ax = plt.subplots()
        color_map = get_cmap(len(costs) + 1)

        for i in range(len(costs)):
            means = []
            stddevs = []
            for order_quantity in order_quantities:
                sim = Simulation(order_quantity=order_quantity, price=price, cost=costs[i])
                means.append(sim.mean)
                stddevs.append(sim.stddev)
            ax.plot(order_quantities, means, c=color_map(i), label=f"Cost = {to_euro(costs[i])}")

            # anotate max profit
            mean_max = max(means)
            x_pos = means.index(mean_max)
            x_max = order_quantities[x_pos]

            if mean_max >= 0:
                ax.annotate(f'({x_max}, {to_euro(mean_max)})', xy=(x_max, mean_max), xytext=(x_max+5, mean_max-150), arrowprops=dict(facecolor='black', shrink=0.01, headwidth=4, headlength=4, width=0.01))



        ax.set_title(f'Average Profits per Order Quantity (Price = {to_euro(price)})')
        ax.set_xlabel('Order Quantity')
        ax.set_ylabel('Average Profit')
        ax.yaxis.set_major_formatter('€{x:1.0f}')
        ax.legend(loc="upper left")
        ax.grid(linestyle = '--')
        fig.tight_layout()

        plt.show()