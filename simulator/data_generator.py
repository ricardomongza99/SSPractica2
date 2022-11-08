import time, random
from statistics import mean

"""
Creates lookup table for uniform distribution
Example: size=100 -> [0.01, 0.02, 0.03,..., 1]
"""
def generate_table_a(size):
    table = [0] * size
    table[0] = 1.0 / size
    for i in range(1, size):
        table[i] = round(table[i-1] + 1.0 / size, 2)
    return table

def generate_table_b(size):
    max = (size * (size + 1)) / 2
    table = [0] * size
    table[0] = 1.0 / max
    for i in range(1, size):
        table[i] = table[i-1] + (i + 1) / max
    return table

def generate_table_c(size):
    max = size * size / 4
    table = [0] * size
    for i in range(1, int(size/2)):
        table[i] = table[i-1] + i / max
    for i in range(int(size/2), size):
        table[i] = table[i-1] + (size - i) / max
    return table

\








class DataGeneratorEfficiencyChecker():

    def __generate_demand(self, table):
        u = random.random()
        for i in range(len(table)):
            if u < table[i]:
                return i
        return len(table) - 1

    def __generate_demand_bin_search(self, table):
        u = random.random()

        left = 0
        right = len(table) - 1

        while (left < right):
            mid = (left + right) // 2

            if u == table[mid]:
                return mid
            elif u < table[mid]:
                right = mid - 1
            else:
                left = mid + 1
        
        return left
  
    def run(self, iterations = 10_000):
        
        table = generate_table_a(100)

        non_efficient_times = []
        for _ in range(iterations):
            start = time.time()
            self.__generate_demand(table)
            end = time.time()
            non_efficient_times.append(end - start)

        efficient_times = []
        for _ in range(iterations):
            start = time.time()
            self.__generate_demand_bin_search(table)
            end = time.time()
            efficient_times.append(end - start)

        print('Busqueda Binaria de Tabla C')
        print(f'No eficiente: {mean(non_efficient_times):.20f}s')
        print(f'Eficiente:    {mean(efficient_times):.20f}s')





        


