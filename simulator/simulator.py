from email.base64mime import header_length
from simulator.simulation import Simulation
import matplotlib.pyplot as plt
import numpy as np
from helpers import to_euro, get_cmap

class Simulator():

    def run(self, price, costs, lookup_table_type='a', save_image=False, show_graph=True):
        order_quantities = [i + 1 for i in range(1,101)]
        fig, ax = plt.subplots()
        color_map = get_cmap(len(costs) + 1)

        for i in range(len(costs)):
            means = []
            stddevs = []
            for order_quantity in order_quantities:
                sim = Simulation(order_quantity=order_quantity, price=price, cost=costs[i], lookup_table_type=lookup_table_type)
                means.append(sim.mean)
                stddevs.append(sim.stddev)
            ax.plot(order_quantities, means, c=color_map(i), label=f"y = {to_euro(costs[i])}")

            # anotate max profit
            mean_max = max(means)
            x_pos = means.index(mean_max)
            x_max = order_quantities[x_pos]
            if mean_max >= 0:
                ax.plot(x_max, mean_max, 'o', color='black')
                ax.annotate(f'({x_max}, {to_euro(mean_max)})', xy=(x_max, mean_max+16), ha='center')


        ax.set_title(f'Ganancias medias por unidades pedidas (x = {to_euro(price)}) - Tipo {lookup_table_type.capitalize()}')
        ax.set_xlabel('s')
        ax.set_ylabel('Ganancia media')
        ax.yaxis.set_major_formatter('€{x:1.0f}')
        ax.legend(loc="upper right")
        ax.grid(linestyle = '--')
        fig.tight_layout()

        if save_image:
            plt.savefig(f'images/{lookup_table_type}_x={price}.png', dpi=400)
        
        if show_graph:
            plt.show()
    


    def run_iterations(self, iterations, price, cost, lookup_table_type='a', save_image=False, show_graph=True):
        order_quantities = [i + 1 for i in range(1,101)]
        fig, ax = plt.subplots()
        color_map = get_cmap(len(iterations) + 1)

        for i in range(len(iterations)):
            means = []
            stddevs = []
            for order_quantity in order_quantities:
                sim = Simulation(order_quantity=order_quantity, price=price, cost=cost, lookup_table_type=lookup_table_type, iterations=iterations[i])
                means.append(sim.mean)
                stddevs.append(sim.stddev)
            ax.plot(order_quantities, means, c=color_map(i), label=f"iteraciones = {iterations[i]:,}")


        ax.set_title(f'Ganancias medias por unidades pedidas (x = {to_euro(price)}, y = {to_euro(cost)}) - Tipo {lookup_table_type.capitalize()}')
        ax.set_xlabel('s')
        ax.set_ylabel('Ganancia media')
        ax.yaxis.set_major_formatter('€{x:1.0f}')
        ax.legend(loc="upper right")
        ax.grid(linestyle = '--')
        fig.tight_layout()

        if save_image:
            plt.savefig(f'images/{lookup_table_type}_x={price}.png', dpi=400)
        
        if show_graph:
            plt.show()
