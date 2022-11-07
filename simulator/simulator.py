from email.base64mime import header_length
from simulator.simulation import Simulation, SimulationWithRefunds
import matplotlib.pyplot as plt
import numpy as np
from helpers import to_euro, get_cmap

class Simulator():

    def run(self, x, ys, table='a', iterations=10_000, save_image=False, show_graph=True):
        """ Runs Simulation with a given list of y (costs)

        Parameters:
            x (int): Price to sell unit
            ys ([int]): List of costs for to buy unit
            table ({'a', 'b', 'c'}): Distribution table type
            iterations (int): Number of iterations to run each Simulation
        """
        ss = [i + 1 for i in range(1,101)]
        fig, ax = plt.subplots()
        color_map = get_cmap(len(ys) + 1)

        for i in range(len(ys)):
            means = []
            stddevs = []
            for s in ss:
                sim = Simulation(s, x, ys[i], iterations, table)
                means.append(sim.mean)
                stddevs.append(sim.stddev)
            ax.plot(ss, means, c=color_map(i), label=f"y = {to_euro(ys[i])}")

            # anotate max profit
            mean_max = max(means)
            x_pos = means.index(mean_max)
            x_max = ss[x_pos]
            if mean_max >= 0:
                ax.plot(x_max, mean_max, 'o', color='black')
                ax.annotate(f'({x_max}, {to_euro(mean_max)})', xy=(x_max, mean_max+16), ha='center')


        ax.set_title(f'Ganancias medias por unidades pedidas (x = {to_euro(x)}) - Tipo {table.capitalize()}')
        ax.set_xlabel('s')
        ax.set_ylabel('Ganancia media')
        ax.yaxis.set_major_formatter('€{x:1.0f}')
        ax.legend(loc="upper left")
        ax.grid(linestyle = '--')
        fig.tight_layout()

        if save_image:
            plt.savefig(f'images/{table}_x={x}.png', dpi=400)
        
        if show_graph:
            plt.show()
    
    def run_iterations(self, iterations_set, x, y, table='a', save_image=False, show_graph=True):
        """
        Parameters:
            iterations_set ([int]): A list of different iterations to run for each Simulation
            x (int): Price to sell unit
            y (int): Cost to buy unit
            table ({'a', 'b', 'c'}): Distribution table type
        """
        order_quantities = [i + 1 for i in range(1,101)]
        fig, ax = plt.subplots()
        color_map = get_cmap(len(iterations_set) + 1)

        for i in range(len(iterations_set)):
            means = []
            stddevs = []
            for order_quantity in order_quantities:
                sim = Simulation(order_quantity, x, y, iterations_set[i], table)
                means.append(sim.mean)
                stddevs.append(sim.stddev)
            ax.plot(order_quantities, means, c=color_map(i), label=f"iteraciones = {iterations_set[i]:,}")


        ax.set_title(f'Ganancias medias por unidades pedidas (x = {to_euro(x)}, y = {to_euro(y)}) - Tipo {table.capitalize()}')
        ax.set_xlabel('s')
        ax.set_ylabel('Ganancia media')
        ax.yaxis.set_major_formatter('€{x:1.0f}')
        ax.legend(loc="upper right")
        ax.grid(linestyle = '--')
        fig.tight_layout()

        if save_image:
            plt.savefig(f'images/{table}_x={x}.png', dpi=400)
        
        if show_graph:
            plt.show()

    def run_refunds(self, x, y, zs, table='a', iterations=10_000, save_image=False, show_graph=True):
        """ Runs Simulation with a given list of y (costs)

        Parameters:
            x (int): Price to sell unit
            ys ([int]): List of costs for to buy unit
            z (int): Amount to pay if did not sell all
            table ({'a', 'b', 'c'}): Distribution table type
            iterations (int): Number of iterations to run each Simulation
        """
        ss = [i + 1 for i in range(1,101)]
        fig, ax = plt.subplots()
        color_map = get_cmap(len(zs) + 1)

        for i in range(len(zs)):
            means = []
            stddevs = []
            for s in ss:
                sim = SimulationWithRefunds(s, x, y, zs[i], iterations, table)
                means.append(sim.mean)
                stddevs.append(sim.stddev)
            ax.plot(ss, means, c=color_map(i), label=f"z = {to_euro(zs[i])}")

            # anotate max profit
            mean_max = max(means)
            x_pos = means.index(mean_max)
            x_max = ss[x_pos]
            if mean_max >= 0:
                ax.plot(x_max, mean_max, 'o', color='black')
                ax.annotate(f'({x_max}, {to_euro(mean_max)})', xy=(x_max, mean_max+16), ha='center')


        ax.set_title(f'Ganancias medias por unidades pedidas (x = {to_euro(x)}, y = {to_euro(y)}) - Tipo {table.capitalize()}')
        ax.set_xlabel('s')
        ax.set_ylabel('Ganancia media')
        ax.yaxis.set_major_formatter('€{x:1.0f}')
        ax.legend(loc="upper left")
        ax.grid(linestyle = '--')
        fig.tight_layout()

        if save_image:
            plt.savefig(f'images/{table}_x={x}.png', dpi=400)
        
        if show_graph:
            plt.show()