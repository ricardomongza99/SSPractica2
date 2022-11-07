from simulator.data_generator import generate_table_a, generate_table_b, generate_table_c
from statistics import mean, stdev
import random

class Simulation():

    """ Runs simulation with refunds

    Attributes:
        mean (float): (class attribute) The profit mean calculated
        stddev (float): (class attribute) The standard deviation of the profits calculated
        s (int): Order quantity
        x (int): Price to sell unit
        y (int): Cost to buy unit
        iterations (int): How many times to run the simulation
        table ({'a', 'b', 'c'}): Distribution table type
    """

    def __init__(self, s, x, y, iterations=10_000, table='a'):
        self.__s = s
        self.__x = x
        self.__y = y
        self.__iterations = iterations

        if table == 'a':
            self.__table = generate_table_a(100)
        elif table == 'b':
            self.__table = generate_table_b(100)
        else:
            self.__table = generate_table_c(100)

        self.__run()
    
    """ Returns random demand count given a probability lookup table of any size """
    def __generate_demand(self):
        u = random.random()
        for i in range(len(self.__table)):
            if u < self.__table[i]:
                return i
        return len(self.__table) - 1
    

    def __calculate_profit(self, demand):
        total_cost = self.__y * self.__s
        if demand >= self.__s:
            return self.__x * self.__s - total_cost
        return self.__x * demand - total_cost

    def __run(self):
        profits = []
        for _ in range(self.__iterations):
            demand = self.__generate_demand()
            profit = self.__calculate_profit(demand)

            profits.append(profit)
        
        self.mean = mean(profits)
        self.stddev = stdev(profits)


class SimulationWithRefunds():

    """ Runs simulation with refunds

    Attributes:
        mean (float): (class attribute) The profit mean calculated
        stddev (float): (class attribute) The standard deviation of the profits calculated
        s (int): Order quantity
        x (int): Price to sell unit
        y (int): Cost to buy unit
        z (int): Amount to pay if did not sell all units
        iterations (int): How many times to run the simulation
        table ({'a', 'b', 'c'}): Distribution table type
    """

    def __init__(self, s, x, y, z, iterations=10_000, table='a'):
        self.__s = s
        self.__x = x
        self.__y = y
        self.__z = z
        self.__iterations = iterations

        if table == 'a':
            self.__table = generate_table_a(100)
        elif table == 'b':
            self.__table = generate_table_b(100)
        else:
            self.__table = generate_table_c(100)

        self.__run()
    
    """ Returns random demand count given a probability lookup table of any size """
    def __generate_demand(self):
        u = random.random()
        for i in range(len(self.__table)):
            if u < self.__table[i]:
                return i
        return len(self.__table) - 1
    
    def __calculate_profit(self, demand):
        total_cost = self.__y * self.__s
        if demand >= self.__s:
            return self.__x * self.__s - total_cost
        return self.__x * demand - self.__y * demand - min(self.__z, self.__y * (self.__s - demand))

    def __run(self):
        profits = []
        for _ in range(self.__iterations):
            demand = self.__generate_demand()
            profit = self.__calculate_profit(demand)

            profits.append(profit)
        
        self.mean = mean(profits)
        self.stddev = stdev(profits)
