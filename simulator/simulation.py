from simulator.data_generator import generate_table_a, generate_table_b, generate_table_c
from statistics import mean, stdev
import random


class Simulation():

    def __init__(self, order_quantity, price, cost, iterations=10_000, lookup_table_type='a'):
        self.__order_quantity = order_quantity
        self.__cost = cost
        self.__price = price
        self.__iterations = iterations

        if lookup_table_type == 'a':
            self.__lookup_table = generate_table_a(100)
        elif lookup_table_type == 'b':
            self.__lookup_table = generate_table_b(100)
        else:
            self.__lookup_table = generate_table_c(100)

        self.__run()
    
    """ Returns random demand count given a probability lookup table of any size """
    def __generate_demand(self):
        u = random.random()
        for i in range(len(self.__lookup_table)):
            if u < self.__lookup_table[i]:
                return i
        return len(self.__lookup_table) - 1
    
    def __calculate_profit(self, demand):
        costs = self.__cost * self.__order_quantity
        if demand >= self.__order_quantity:
            return self.__price * self.__order_quantity - costs
        return self.__price * demand -costs

    def __run(self):
        profits = []
        for _ in range(self.__iterations):
            demand = self.__generate_demand()
            profit = self.__calculate_profit(demand)

            profits.append(profit)
        
        self.mean = mean(profits)
        self.stddev = stdev(profits)


        